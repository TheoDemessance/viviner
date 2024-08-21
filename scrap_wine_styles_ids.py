import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import utils.constants as C

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "wine-styles"


def fetch_detailed_wine_style(wine_style_id):
    url = f"{C.BASE_URL}/wine-styles/{wine_style_id}"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to retrieve details for wine type {wine_style_id}. Status code: {response.status_code}")
        return None


global_url = f"{C.BASE_URL}/wine-styles"
response = requests.get(url=global_url)

if response.status_code == 200:
    wine_styles_data = response.json()

    for wine_style in wine_styles_data:
        wine_style_id = wine_style['id']
        detailed_wine_style_data = fetch_detailed_wine_style(wine_style_id)

        if detailed_wine_style_data:
            db.collection(collection_name).document(
                str(wine_style_id)).set(detailed_wine_style_data)

            print(f"Stored data {wine_style_id} in Firestore.")

else:
    print(
        f"Failed to retrieve foods data. Status code: {response.status_code}")
