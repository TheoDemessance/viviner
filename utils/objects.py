import utils.constants as C
import requests

headers = {
    "User-Agent": ""
}


class MerchantInfo:
    def __init__(self, merchant_id) -> None:
        self.merchant_id = merchant_id
        self.merchant_info = {}
        self.base_url = C.BASE_URL

    def get_merchant_data(self):
        response = requests.get(
            f"{self.base_url}/merchants/{self.merchant_id}",
            headers=headers)
        return response.json()

    def generate_merchant_info(self):
        self.get_merchant_data()

        self.merchant_info = {
            "id": self.merchant_info.get('id'),
            "name": self.merchant_info.get('name'),
            "seo_name": self.merchant_info.get('seo_name'),
            "legal_name": self.merchant_info.get('legal_name'),
            "description": self.merchant_info.get('description'),
            "country": self.merchant_info.get('country'),
            "state": self.merchant_info.get('state'),
            "status": self.merchant_info.get('status'),
            "image": self.merchant_info.get('image'),
            "shipping_estimate": self.merchant_info.get('shipping_estimate'),
            "impressum_url": self.merchant_info.get('impressum_url'),
            "tos_url": self.merchant_info.get('tos_url'),
            "payment_options": self.merchant_info.get('payment_options'),
            "invoicing_settings": self.merchant_info.get('invoicing_settings'),
            "vc_clearing_system": self.merchant_info.get('vc_clearing_system'),
            "hidden": self.merchant_info.get('hidden')
        }

    def to_dict(self):
        return vars(self)


class WineryInfo:
    def __init__(self, winery_id) -> None:
        self.winery_id = winery_id
        self.winery_info = {}
        self.base_url = C.BASE_URL

    def get_winery_data(self):
        response = requests.get(f"{self.base_url}/wineries/{self.winery_id}",
                                headers=headers)
        self.winery_data = response.json()

    def generate_winery_info(self):
        self.get_winery_data()

        self.winery_info = {
            "id": self.winery_data.get('id'),
            "name": self.winery_data.get('name'),
            "seo_name": self.winery_data.get('seo_name'),
            "status": self.winery_data.get('status'),
            "review_status": self.winery_data.get('review_status'),
            "background_image": self.winery_data.get('background_image'),
            "statistics": {
                "ratings_count": self.winery_data.get('statistics', {}).get('ratings_count'),
                "ratings_average": self.winery_data.get('statistics', {}).get('ratings_average'),
                "labels_count": self.winery_data.get('statistics', {}).get('labels_count'),
                "wines_count": self.winery_data.get('statistics', {}).get('wines_count')
            },
            "region_id": self.winery_data.get('region', {}).get('id'),
            "business_name": self.winery_data.get('business_name'),
            "description": self.winery_data.get('description'),
            "specialists_notes": self.winery_data.get('specialists_notes'),
            "phone": self.winery_data.get('phone'),
            "email": self.winery_data.get('email'),
            "facebook": self.winery_data.get('facebook'),
            "instagram": self.winery_data.get('instagram'),
            "is_claimed": self.winery_data.get('is_claimed'),
            "twitter": self.winery_data.get('twitter'),
            "website": self.winery_data.get('website'),
            "winemaker": self.winery_data.get('winemaker'),
            "wine_maker": self.winery_data.get('wine_maker'),
            "address": {
                "title": self.winery_data.get('address', {}).get('title'),
                "name": self.winery_data.get('address', {}).get('name'),
                "street": self.winery_data.get('address', {}).get('street'),
                "street2": self.winery_data.get('address', {}).get('street2'),
                "neighborhood": self.winery_data.get('address', {}).get('neighborhood'),
                "city": self.winery_data.get('address', {}).get('city'),
                "zip": self.winery_data.get('address', {}).get('zip'),
                "state": self.winery_data.get('address', {}).get('state'),
                "country": self.winery_data.get('address', {}).get('country'),
                "company": self.winery_data.get('address', {}).get('company'),
                "phone": self.winery_data.get('address', {}).get('phone'),
                "external_id": self.winery_data.get('address', {}).get('external_id'),
                "residential": self.winery_data.get('address', {}).get('residential'),
                "vat_number": self.winery_data.get('address', {}).get('vat_number'),
                "vat_code": self.winery_data.get('address', {}).get('vat_code'),
                "addition": self.winery_data.get('address', {}).get('addition'),
            },
            "image": self.winery_data.get('image'),
            "location": self.winery_data.get('location'),
            "winery_group": self.winery_data.get('winery_group'),
            "first_wines": self.winery_data.get('first_wines'),
            "sponsored_entity_type": self.winery_data.get('sponsored_entity_type'),
            "sponsored_entity": self.winery_data.get('sponsored_entity')
        }

    def to_dict(self):
        return vars(self)


class WineInfo:
    """_summary_
    """

    def __init__(self, wine_id, price) -> None:
        self.wine_id = wine_id
        self.wine_info = {}
        self.base_url = C.BASE_URL
        self.price_data = price

    def get_wine_data(self):
        response = requests.get(f"{self.base_url}/wines/{self.wine_id}",
                                headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_wine_taste_profile(self):
        response = requests.get(f"{self.base_url}/wines/{self.wine_id}/tastes",
                                headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_vintage_taste_profile(self, vintage_id):
        response = requests.get(
            f"{self.base_url}/vintages/{vintage_id}/tastes",
            headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_detailed_vintage_data(self, vintage_id):
        response = requests.get(f"{self.base_url}/vintages/{vintage_id}",
                                headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_reviews(self):
        response = requests.get(
            f"{self.base_url}/wines/{self.wine_id}/reviews",
            params={"limit": 9999},
            headers=headers)
        return response.json() if response.status_code == 200 else {}

    def get_price_data(self, vintage_id):
        response = requests.get(
            f"https://www.vivino.com/api/prices?vintage_ids[]={vintage_id}&language=fr",
            headers=headers
        )
        return response.json() if response.status_code == 200 else {}

    def generate_wine_info(self):
        wine_data = self.get_wine_data()
        review_data = self.get_reviews()
        wine_taste_profile = self.get_wine_taste_profile()

        self.wine_info = {
            "wine_id": wine_data['id'],
            "name": wine_data['name'],
            "seo_name": wine_data['seo_name'],
            "is_natural": wine_data.get('is_natural'),
            # Jointure sur collection type
            "type_id": wine_data.get('type_id'),
            # Besoin de scraper la winery au fil de l'eau
            "winery_id": wine_data.get('winery', {}).get('id'),
            # Jointure sur collection region
            "region_id": wine_data.get('region', {}).get('id'),
            "general_statistics": {
                "status": wine_data.get('statistics', {}).get('status'),
                "average_rating": wine_data.get('statistics', {}).get('ratings_average'),
                "ratings_count": wine_data.get('statistics', {}).get('ratings_count'),
                "labels_count": wine_data.get('statistics', {}).get('labels_count'),
                "vintages_count": wine_data.get('statistics', {}).get('vintages_count')
            },
            "rank": wine_data.get('rank'),
            "hidden": wine_data.get('hidden'),
            "taste": {
                "flavor": wine_taste_profile.get('flavor'),
                "structure": wine_taste_profile.get('structure')
            },
            "vintages": [],
            "reviews": review_data
        }

        vintages = wine_data.get('vintages', [])

        for i, vintage in enumerate(vintages):
            vintage_id = vintage['id']
            detailed_vintage_data = self.get_detailed_vintage_data(vintage_id)
            detailed_taste_profile = self.get_vintage_taste_profile(vintage_id)

            vintage_data = {
                "id": vintage_id,
                "seo_name": detailed_vintage_data.get('seo_name'),
                "year": detailed_vintage_data.get('year'),
                "name": detailed_vintage_data.get('name'),
                "statistics": {
                    "status": detailed_vintage_data.get('statistics', {}).get('status'),
                    'ratings_count': detailed_vintage_data.get('statistics', {}).get('ratings_count'),
                    'ratings_average': detailed_vintage_data.get('statistics', {}).get('ratings_average'),
                    'labels_count': detailed_vintage_data.get('statistics', {}).get('labels_count'),
                    'reviews_count': detailed_vintage_data.get('statistics', {}).get('reviews_count')
                },
                "organic_certification_id": detailed_vintage_data.get('organic_certification_id'),
                "certified_biodynamic": detailed_vintage_data.get('certified_biodynamic'),
                "description": detailed_vintage_data.get('description'),
                "wine_critic_reviews": detailed_vintage_data.get('wine_critic_reviews'),
                "awards": detailed_vintage_data.get('awards'),
                "ratings_distribution": detailed_vintage_data.get('ratings_distribution'),
                "ranking": {
                    "country": detailed_vintage_data.get('ranking', {}).get('country') if detailed_vintage_data.get('ranking') is not None else None,
                    "region": detailed_vintage_data.get('ranking', {}).get('region') if detailed_vintage_data.get('ranking') is not None else None,
                    "global": detailed_vintage_data.get('ranking', {}).get('global') if detailed_vintage_data.get('ranking') is not None else None,
                    "winery": detailed_vintage_data.get('ranking', {}).get('winery') if detailed_vintage_data.get('ranking') is not None else None
                },
                "recommended_drinking_window": detailed_vintage_data.get('recommended_drinking_window'),
                "wine_facts": detailed_vintage_data.get('wine_facts'),
                "winemaker": detailed_vintage_data.get('winemaker'),
                "wine_maker": detailed_vintage_data.get('wine_maker'),
                "grape_composition": detailed_vintage_data.get('grape_composition'),
                "taste": {
                    "flavor": detailed_taste_profile.get('flavor'),
                    "structure": detailed_taste_profile.get('structure')
                },
                "price": self.get_price_data(vintage_id).get('prices', {}).get('vintages', {}).get(str(vintage_id), {}).get('price')
            }

            if i == 0:
                detailed_wine_data = detailed_vintage_data.get('wine', {})
                self.wine_info['description'] = detailed_wine_data.get(
                    'description')
                self.wine_info['style_id'] = detailed_wine_data.get('style_id')
                self.wine_info['grapes'] = detailed_wine_data.get('grapes')
                self.wine_info['foods'] = detailed_wine_data.get('foods')
                self.wine_info['non_vintage'] = detailed_wine_data.get(
                    'non_vintage')
                self.wine_info['alcohol'] = detailed_wine_data.get('alcohol')
                self.wine_info['sweetness_id'] = detailed_wine_data.get(
                    'sweetness_id')
                self.wine_info['closure'] = detailed_wine_data.get('closure')
                self.wine_info['vintage_mask_raw'] = detailed_wine_data.get(
                    'vintage_mask_raw')
                self.wine_info['updated_at'] = detailed_wine_data.get(
                    'updated_at')
                self.wine_info['created_at'] = detailed_wine_data.get(
                    'created_at')
                self.wine_info['is_first_wine'] = detailed_wine_data.get(
                    'is_first_wine')

            self.wine_info['vintages'].append(vintage_data)

            total_amount = 0
            count = 0

            for vintage in vintage_data:
                price = vintage.get('price', {})
                amount = price.get('amount')

                if amount is not None:
                    total_amount += amount
                    count += 1

            if count > 0:
                avg_price = total_amount/count

            self.wine_info['avg_price'] = avg_price

    def to_dict(self):
        return vars(self)
