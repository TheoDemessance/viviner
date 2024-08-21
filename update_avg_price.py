from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("vinomate-9ddd21ae1bb3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

batch_size = 100
last_doc = None

while True:
    if last_doc:
        query = db.collection('wines').start_after(
            last_doc).limit(batch_size).stream()
    else:
        query = db.collection('wines').limit(batch_size).stream()

    docs = list(query)

    if not docs:
        break

    for doc in docs:
        total_amount = 0
        count = 0
        doc_data = doc.to_dict()

        for vintage in doc_data['vintages']:
            price = vintage.get('price', {})

            if price is not None:
                amount = price.get('amount')

                if amount is not None:
                    total_amount += amount
                    count += 1
            else:
                continue

        if count > 0:
            avg_price = total_amount/count

        else:
            avg_price = None

        doc.reference.update({"avg_price": avg_price})

        print(f'Updated doc {doc.id} with avg_price: {avg_price}')

    last_doc = docs[-1]
