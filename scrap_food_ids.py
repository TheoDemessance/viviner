import requests
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore
import utils.constants as C

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "foods"

global_url = f"{C.BASE_URL}/foods"
response = requests.get(url=global_url)

if response.status_code == 200:
    foods_data = response.json()

    for food in foods_data:
        db.collection(collection_name).document(
            str(food.get('id'))).set(food)

    print(f"Stored data {food.get('id')} in Firestore.")

else:
    print(
        f"Failed to retrieve foods data. Status code: {response.status_code}")
