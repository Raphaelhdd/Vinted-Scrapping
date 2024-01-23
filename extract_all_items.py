# Import necessary libraries and modules
import extract_token
import extract_user_information
import extract_sold_products
import extract_current_products
import json
import pandas as pd

# Define column names for the dataset
column_names = ['username', 'product_id', 'title_product', 'price', 'url', 'photo', 'email', 'gender', 'items_count',
                'followers', 'follows', 'feedback_count', 'positive_feedback', 'negative_feedback', 'neutral_feedback',
                'meeting_transactions', 'profile_photo', 'business_account', 'account_ban_date',
                'is_account_ban_permanent', 'is_publish_photos_agreed', 'expose_location', 'city', 'country_title',
                'is_hated', 'hates_you', 'view_profile', 'email_verification', 'facebook_verification',
                'google_verification', 'phone_verification', 'item_titles_advice', 'ratings_advice',
                'feedbacks_advice', 'item_title_dressing', 'item_size_dressing', 'item_creation_date_dressing',
                'item_boosted_dressing', 'item_updated_date_dressing', 'item_brand_dressing', 'item_price_dressing',
                'item_image_url_dressing', 'item_description_dressing']


# Function to extract sold products information
def sold_products(user_sold_products):
    """
    Extract information about sold products, including item titles, ratings, and feedback.

    Parameters:
    - user_sold_products: List of dictionaries representing sold products.

    Returns:
    - item_titles_advice: List of item titles in sold products.
    - ratings_advice: List of ratings associated with sold products.
    - feedbacks_advice: List of feedback comments associated with sold products.
    """
    item_titles_advice, ratings_advice, feedbacks_advice = [], [], []
    for product in user_sold_products:
        item_titles_advice.append(product['name_product_sold'])
        ratings_advice.append(product['description_product_sold'])
        feedbacks_advice.append(product['rating_feedback'])
    return item_titles_advice, ratings_advice, feedbacks_advice


# Function to extract current products information
def current_products(user_current_products):
    """
    Extract information about current products, including item details.

    Parameters:
    - user_current_products: List of dictionaries representing current products.

    Returns:
    - item_title_dressing: List of current item titles.
    - item_size_dressing: List of current item sizes.
    - item_creation_date_dressing: List of creation dates for current items.
    - item_boosted_dressing: List of boosted status for current items.
    - item_updated_date_dressing: List of update dates for current items.
    - item_brand_dressing: List of brands for current items.
    - item_price_dressing: List of prices for current items.
    - item_image_url_dressing: List of image URLs for current items.
    - item_description_dressing: List of descriptions for current items.
    """
    item_title_dressing, item_size_dressing, item_creation_date_dressing, item_boosted_dressing = [], [], [], []
    item_updated_date_dressing, item_brand_dressing, item_price_dressing = [], [], []
    item_image_url_dressing, item_description_dressing = [], []
    for product in user_current_products:
        item_title_dressing.append(product['title'])
        item_size_dressing.append(product['size'])
        item_creation_date_dressing.append(product['creation_date'])
        item_updated_date_dressing.append(product['updated_date'])
        item_brand_dressing.append(product['brand'])
        item_price_dressing.append(product['price'])
        item_image_url_dressing.append(product['image_url'])
        item_boosted_dressing.append(product['price'])
        item_description_dressing.append(product['description'])
    return item_title_dressing, item_size_dressing, item_creation_date_dressing, item_boosted_dressing, \
           item_updated_date_dressing, item_brand_dressing, item_price_dressing, \
           item_image_url_dressing, item_description_dressing


# Function to scrape announcements and populate the dataset
def scrapping_annonces(dataset_final, session, keyword):
    """
    Scrape Vinted announcements based on a given keyword and populate a dataset.

    Parameters:
    - dataset_final: DataFrame to store the collected data.
    - session: Vinted session for making API requests.
    - keyword: Keyword for searching announcements.

    Returns:
    None (Dataset is modified in-place).
    """
    # Replace spaces in the keyword with "%20"
    keyword = keyword.replace(" ", "%20")

    try:
        # Define the API URL for retrieving items
        api_all_items_keyword = f"https://www.vinted.fr/api/v2/catalog/items?page=1&per_page=800&search_text={keyword}&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=6"
        # Send a request to get all items based on the keyword
        all_items_request = session.get(api_all_items_keyword)
        json_data = json.loads(all_items_request.text)

        # Loop through each item in the response
        for item in json_data['items']:
            id_member = item['user']['id']
            user_data = extract_user_information.extract_information_user(session, id_member)
            user_sold_products = extract_sold_products.extract_sold_products(session, member_id=id_member,
                                                                             user_data=user_data)
            item_titles_advice, ratings_advice, feedbacks_advice = sold_products(user_sold_products)
            user_current_products = extract_current_products.extract_current_product(session, member_id=id_member,
                                                                                     user_data=user_data,
                                                                                     item_id=item['id'])
            item_title_dressing, item_size_dressing, item_creation_date_dressing, item_boosted_dressing, \
            item_updated_date_dressing, item_brand_dressing, item_price_dressing, \
            item_image_url_dressing, item_description_dressing = current_products(user_current_products)

            # Construct a dictionary with the collected data
            final_data = {
                'username': user_data['username'],
                'product_id': item.get('id', 'N/A'),
                'title_product': item.get('title', 'N/A'),
                'price': item.get('price', 'N/A'),
                'url': item.get('url', 'N/A'),
                'photo': item.get('photo', {}).get('url', 'N/A'),
                'email': user_data['email'],
                'gender': user_data['gender'],
                'items_count': user_data['items_count'],
                'followers': user_data['followers'],
                'follows': user_data['follows'],
                'feedback_count': user_data['feedback_count'],
                'positive_feedback': user_data['positive_feedback'],
                'negative_feedback': user_data['negative_feedback'],
                'neutral_feedback': user_data['neutral_feedback'],
                'meeting_transactions': user_data['meeting_transactions'],
                'profile_photo': user_data['profile_photo'],
                'business_account': user_data['business_account'],
                'account_ban_date': user_data['account_ban_date'],
                'is_account_ban_permanent': user_data['is_account_ban_permanent'],
                'is_publish_photos_agreed': user_data['is_publish_photos_agreed'],
                'expose_location': user_data['expose_location'],
                'city': user_data['city'],
                'country_title': user_data['country_title'],
                'is_hated': user_data['is_hated'],
                'hates_you': user_data['hates_you'],
                'view_profile': user_data['view_profile'],
                'email_verification': user_data['email_verification'],
                'facebook_verification': user_data['facebook_verification'],
                'google_verification': user_data['google_verification'],
                'phone_verification': user_data['phone_verification'],
                'item_titles_advice': item_titles_advice,
                'ratings_advice': ratings_advice,
                'feedbacks_advice': feedbacks_advice,
                'item_title_dressing': item_title_dressing,
                'item_size_dressing': item_size_dressing,
                'item_creation_date_dressing': item_creation_date_dressing,
                'item_boosted_dressing': item_boosted_dressing,
                'item_updated_date_dressing': item_updated_date_dressing,
                'item_brand_dressing': item_brand_dressing,
                'item_price_dressing': item_price_dressing,
                'item_image_url_dressing': item_image_url_dressing,
                'item_description_dressing': item_description_dressing
            }

            # Append the dictionary to the dataset
            dataset_final = dataset_final.append(final_data, ignore_index=True)

    except Exception as e:
        print(f"An error occurred while scraping announcements: {e}")


# Main function to execute the scraping process
if __name__ == '__main__':
    # Create a Vinted session
    session = extract_token.vinted_session()

    # Set a keyword for educational purposes (e.g., "campus 00s")
    keyword = "campus 00s"

    # Initialize an empty DataFrame to store the dataset
    dataset_final = pd.DataFrame(columns=column_names)

    # Execute the scraping function
    scrapping_annonces(dataset_final, session, keyword)

    # Save the final dataset to a CSV file
    dataset_final.to_csv('dataset_final.csv')
