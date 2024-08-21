from utils.objects import WineInfo, WineryInfo, MerchantInfo
import utils.constants as C
import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore

if __name__ == "__main__":
    url = "https://www.vivino.com/api"
    params = {
        "region_ids[]": 650
    }
    headers = {
        "User-Agent": ""
    }

    cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Performs an initial request to get the number of records (wines)
    res = requests.get(f'{url}/explore/explore',
                       params=params,
                       headers=headers)

    if res.status_code == 200:
        n_matches = res.json()['explore_vintage']['records_matched']
        print(f'Number of matches: {n_matches}')

        # Iterates through the amount of possible pages
        for i in range(0, max(1, int(n_matches / C.RECORDS_PER_PAGE)) + 1):
            params['page'] = i

            # Performs the request and scraps the URLs
            res = requests.get(f'{url}/explore/explore',
                               params=params,
                               headers=headers)
            matches = res.json()['explore_vintage']['matches']

            # Iterates over every match
            for match in matches:
                wine_id = match['vintage']['wine']['id']

                doc_ref = db.collection('wines').document(str(wine_id))
                doc = doc_ref.get()

                if doc.exists:
                    print(f'Wine {wine_id} already exists, skipping.')
                    continue

                wine = WineInfo(wine_id, match['price'])
                wine.generate_wine_info()

                winery = WineryInfo(match['vintage']['wine']['winery']['id'])
                winery.generate_winery_info()

                merchant = MerchantInfo(match['price']['merchant_id'])
                merchant.generate_merchant_info()

                db.collection('wines').document(
                    str(wine.wine_id)).set(wine.wine_info, merge=True)
                db.collection('wineries').document(
                    str(winery.winery_id)).set(winery.winery_info, merge=True)
                db.collection('merchants').document(
                    str(merchant.merchant_id)).set(merchant.merchant_info, merge=True)

                print(f'Stored wine {wine.wine_id}')
