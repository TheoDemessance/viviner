import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import utils.constants as C

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "grapes"


def fetch_detailed_grape(grape_id):
    url = f"{C.BASE_URL}/grapes/{grape_id}"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to retrieve details for grape {grape_id}. Status code: {response.status_code}")
        return None


global_url = f"{C.BASE_URL}/grapes"
response = requests.get(url=global_url)

if response.status_code == 200:
    grapes_data = response.json()

    for grape in grapes_data:
        grape_id = grape['id']
        detailed_region_data = fetch_detailed_grape(grape_id)

        if detailed_region_data:
            db.collection(collection_name).document(
                str(grape_id)).set(detailed_region_data)

            print(f"Stored data {grape_id} in Firestore.")

else:
    print(
        f"Failed to retrieve grapes data. Status code: {response.status_code}")
