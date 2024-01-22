import extract_user_information
import extract_token
import json
import time


def extract_current_product(session, member_id):
    """
    Extracts information about the current products listed by a Vinted user.

    Args:
        session (requests.Session): Authenticated session with Vinted.
        member_id (int): The Vinted member ID.

    Returns:
        dict: Dictionary containing information about the user's current products.
    """
    try:
        # Extract user information to get the total number of items
        user_data = extract_user_information.extract_information_user(session, member_id)

        # Check if the user has listed any products
        if user_data['items_count'] > 0:
            # Build API endpoint to fetch user's current products
            api_dressing = f"https://www.vinted.fr/api/v2/users/{member_id}/items?page=1&per_page={user_data['items_count']}&order=relevance"

            # Make a GET request to retrieve current products data
            check_dressing = session.get(api_dressing)
            check_dressing.raise_for_status()
            json_data_dressing = json.loads(check_dressing.text)

            # Dictionary to store information about all items
            all_items = {}

            # Iterate through each item
            for item in json_data_dressing["items"]:
                product_id = item.get('id', 'N/A')
                product_title = item.get('title', 'N/A')
                product_size = item.get('size', 'N/A')
                product_creation_date = item.get('created_at_ts', 'N/A')
                product_updated_date = item.get('description', 'N/A')
                product_brand = item.get('brand', 'N/A')
                product_price = item.get('original_price_numeric', 'N/A')
                product_img = item['photos'][0]['url'] if 'photos' in item and item['photos'] else 'N/A'
                product_boosted = item.get('promoted_internationally', 'N/A')

                # Store item information in a dictionary
                item_data = {
                    'title': product_title,
                    'size': product_size,
                    'creation_date': product_creation_date,
                    'updated_date': product_updated_date,
                    'brand': product_brand,
                    'price': product_price,
                    'image_url': product_img,
                    'boosted': product_boosted
                }

                # Add item information to the overall dictionary
                all_items[product_id] = item_data

                # Pause for 1 second to avoid rate limiting
                time.sleep(1)

            # Return the dictionary containing all item information
            return all_items

        else:
            print("This user has no listed products.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    # Create a Vinted session with an authenticated token
    session = extract_token.vinted_session()

    # For educational purposes, let's consider a member with ID 1234
    # You can find the member ID in the URL after "https://www.vinted.fr/member/"
    member_id_to_search = 1234

    # Extract information about the user's current products
    current_products = extract_current_product(session, member_id_to_search)

    # Print or process the extracted product information
    if current_products:
        print("Current Products Information:")
        for product_id, product_info in current_products.items():
            print(f"Product ID: {product_id}")
            for key, value in product_info.items():
                print(f"  {key}: {value}")
            print("\n")
    else:
        print("Failed to retrieve current product information.")
