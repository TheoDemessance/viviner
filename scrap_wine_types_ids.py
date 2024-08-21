import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import utils.constants as C

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "wine-types"


global_url = f"{C.BASE_URL}/wine-types"
response = requests.get(url=global_url)

if response.status_code == 200:
    wine_types_data = response.json()

    for wine_style in wine_types_data:
        wine_style_id = wine_style['id']

        db.collection(collection_name).document(
            str(wine_style_id)).set(wine_style)

        print(f"Stored data {wine_style_id} in Firestore.")

else:
    print(
        f"Failed to retrieve wine type data. Status code: {response.status_code}")
