import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import utils.constants as C

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "regions"


def fetch_detailed_region(region_id):
    url = f"{C.BASE_URL}/regions/{region_id}"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to retrieve details for region {region_id}. Status code: {response.status_code}")
        return None


global_url = f"{C.BASE_URL}/regions"
response = requests.get(url=global_url)

if response.status_code == 200:
    regions_data = response.json()

    for region in regions_data:
        region_id = region['id']
        detailed_region_data = fetch_detailed_region(region_id)

        if detailed_region_data:
            db.collection(collection_name).document(
                str(region_id)).set(detailed_region_data)

            print(f"Stored data {region_id} in Firestore.")

else:
    print(
        f"Failed to retrieve regions data. Status code: {response.status_code}")
