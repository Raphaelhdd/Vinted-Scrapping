import json
import extract_token

def extract_information_user(session, member_id):
    """
    Extracts information about a Vinted user using their member ID.

    Args:
        session (requests.Session): Authenticated session with Vinted.
        member_id (int): The Vinted member ID.

    Returns:
        user_data: Information about the user or can be further processed as needed.
    """
    try:
        # Build the URL to fetch user information
        url = f"https://www.vinted.fr/api/v2/users/{member_id}?localize=false"

        # Make a GET request to retrieve user data
        request_session = session.get(url)

        # Parse the response as JSON
        json_data = json.loads(request_session.text)

        # Extract user information
        mail_member = json_data['user'].get('email', 'N/A')
        gender = json_data['user'].get('gender', 'N/A')
        name_member = json_data['user'].get('login', 'N/A')
        item_count = json_data['user'].get('item_count', 'N/A')
        followers = json_data['user'].get('followers_count', 'N/A')
        follows = json_data['user'].get('following_count', 'N/A')
        feedback_count = json_data['user'].get('feedback_count', 'N/A')
        positive_feedback = json_data['user'].get('positive_feedback_count', 'N/A')
        negative_feedback = json_data['user'].get('negative_feedback_count', 'N/A')
        neutral_feedback = json_data['user'].get('neutral_feedback_count', 'N/A')
        meeting_transaction = json_data['user'].get('meeting_transaction_count', 'N/A')
        photo = json_data['user']['photo'].get('url', 'N/A')
        business_account = json_data['user'].get('business_account', 'N/A')
        account_ban_date = json_data['user'].get('account_ban_date', 'N/A')
        is_account_ban_permanent = json_data['user'].get('is_account_ban_permanent', 'N/A')
        is_publish_photos_agreed = json_data['user'].get('is_publish_photos_agreed', 'N/A')
        expose_location = json_data['user'].get('expose_location', 'N/A')
        city = json_data['user'].get('city', 'N/A')
        country_title = json_data['user'].get('country_title', 'N/A')
        is_hated = json_data['user'].get('is_hated', 'N/A')
        hates_you = json_data['user'].get('hates_you', 'N/A')
        view_profile = json_data['user'].get('can_view_profile', 'N/A')

        # Verification details
        verification_mail = json_data['user']['verification']['email'].get('valid', 'N/A')
        verification_facebook = json_data['user']['verification']['facebook'].get('valid', 'N/A')
        verification_google = json_data['user']['verification']['google'].get('valid', 'N/A')
        verification_phone = json_data['user']['verification']['phone'].get('valid', 'N/A')

        # Print or process the extracted information
        user_data = {
            'username': name_member,
            'email': mail_member,
            'gender': gender,
            'items_count': item_count,
            'followers': followers,
            'follows': follows,
            'feedback_count': feedback_count,
            'positive_feedback': positive_feedback,
            'negative_feedback': negative_feedback,
            'neutral_feedback': neutral_feedback,
            'meeting_transactions': meeting_transaction,
            'profile_photo': photo,
            'business_account': business_account,
            'account_ban_date': account_ban_date,
            'is_account_ban_permanent': is_account_ban_permanent,
            'is_publish_photos_agreed': is_publish_photos_agreed,
            'expose_location': expose_location,
            'city': city,
            'country_title': country_title,
            'is_hated': is_hated,
            'hates_you': hates_you,
            'view_profile': view_profile,
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
