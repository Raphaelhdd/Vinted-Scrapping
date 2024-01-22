import json
import extract_token

# Let's gather some information for the purpose of machine learning

def extract_information_user(session, member_id):
    """
    Extracts information about a Vinted user using their member ID.

    Args:
        session (requests.Session): Authenticated session with Vinted.
        member_id (int): The Vinted member ID.

    Returns:
        user_data: Information about the user or can be further processed as needed.
    """
    user_data = {}
    try:
        # Build the URL to fetch user information
        url = f"https://www.vinted.fr/api/v2/users/{member_id}?localize=false"

        # Make a GET request to retrieve user data
        request_session = session.get(url)

        # Parse the response as JSON
        json_data = json.loads(request_session.text)

        # Extract user information
        name_member = json_data['user']['login'] if 'login' in json_data['user'] else 'N/A'
        item_count = json_data['user']['item_count'] if 'item_count' in json_data['user'] else 'N/A'
        followers = json_data['user']['followers_count'] if 'followers_count' in json_data['user'] else 'N/A'
        follows = json_data['user']['following_count'] if 'following_count' in json_data['user'] else 'N/A'
        feedback_rate = json_data['user']['feedback_reputation'] if 'feedback_reputation' in json_data['user'] else 'N/A'
        feedback_count = json_data['user']['feedback_count'] if 'feedback_reputation' in json_data['user'] else 'N/A'
        meeting_transaction = json_data['user']['meeting_transaction_count'] if 'meeting_transaction_count' in \
                                                                                json_data['user'] else 'N/A'
        photo = json_data['user']['photo']['url'] if 'photo' in json_data['user'] and 'url' in json_data['user'][
            'photo'] else 'N/A'
        business_account = json_data['user']['business_account'] if 'business_account' in json_data['user'] else 'N/A'

        # Verification details
        verification_mail = json_data['user']['verification']['email']['valid'] if 'verification' in json_data[
            'user'] and 'email' in json_data['user']['verification'] and 'valid' in json_data['user']['verification'][
                                                                                       'email'] else 'N/A'
        verification_facebook = json_data['user']['verification']['facebook']['valid'] if 'verification' in json_data[
            'user'] and 'facebook' in json_data['user']['verification'] and 'valid' in json_data['user'][
                                                                                              'verification'][
                                                                                              'facebook'] else 'N/A'
        verification_google = json_data['user']['verification']['google']['valid'] if 'verification' in json_data[
            'user'] and 'google' in json_data['user']['verification'] and 'valid' in json_data['user']['verification'][
                                                                                          'google'] else 'N/A'
        verification_phone = json_data['user']['verification']['phone']['valid'] if 'verification' in json_data[
            'user'] and 'phone' in json_data['user']['verification'] and 'valid' in json_data['user']['verification'][
                                                                                        'phone'] else 'N/A'

        # Print or process the extracted information
        user_data = {
            'username': name_member,
            'items_count': item_count,
            'followers': followers,
            'follows': follows,
            'feedback_rate': feedback_rate,
            'feedback_count' : feedback_count,
            'meeting_transactions': meeting_transaction,
            'profile_photo': photo,
            'business_account': business_account,
            'email_verification': verification_mail,
            'facebook_verification': verification_facebook,
            'google_verification': verification_google,
            'phone_verification': verification_phone
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        user_data = None

    return user_data

if __name__ == '__main__':
    # Create a Vinted session with an authenticated token
    session = extract_token.vinted_session()

    # For educational purposes, let's consider a member with ID 1234
    # You can find the member ID in the URL after "https://www.vinted.fr/member/"
    member_id_to_search = 1234

    # Extract information for the specified member ID
    user_data = extract_information_user(session, member_id_to_search)

    # Print or process the extracted user information
    if user_data:
        print("User Information:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve user information.")
