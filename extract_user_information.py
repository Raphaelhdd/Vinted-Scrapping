import json
import traceback

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
        mail_member = json_data['user']['email'] if 'email' in json_data['user'] else 'N/A'
        gender = json_data['user']['gender'] if 'gender' in json_data['user'] else 'N/A'
        name_member = json_data['user']['login'] if 'login' in json_data['user'] else 'N/A'
        item_count = json_data['user']['item_count'] if 'item_count' in json_data['user'] else 'N/A'
        followers = json_data['user']['followers_count'] if 'followers_count' in json_data['user'] else 'N/A'
        follows = json_data['user']['following_count'] if 'following_count' in json_data['user'] else 'N/A'
        feedback_count = json_data['user']['feedback_count'] if 'feedback_count' in json_data['user'] else 'N/A'
        positive_feedback = json_data['user']['positive_feedback_count'] if 'positive_feedback_count' in json_data[
            'user'] else 'N/A'
        negative_feedback = json_data['user']['negative_feedback_count'] if 'negative_feedback_count' in json_data[
            'user'] else 'N/A'
        neutral_feedback = json_data['user']['neutral_feedback_count'] if 'neutral_feedback_count' in json_data[
            'user'] else 'N/A'
        meeting_transaction = json_data['user']['meeting_transaction_count'] if 'meeting_transaction_count' in \
                                                                                 json_data['user'] else 'N/A'
        user_photo = json_data['user'].get('photo', None)
        photo = user_photo['url'] if user_photo and 'url' in user_photo else 'N/A'
        business_account = json_data['user']['business_account'] if 'business_account' in json_data['user'] else 'N/A'
        account_ban_date = json_data['user']['account_ban_date'] if 'account_ban_date' in json_data['user'] else 'N/A'
        is_account_ban_permanent = json_data['user']['is_account_ban_permanent'] if 'is_account_ban_permanent' in \
                                                                                    json_data['user'] else 'N/A'
        is_publish_photos_agreed = json_data['user']['is_publish_photos_agreed'] if 'is_publish_photos_agreed' in \
                                                                                    json_data['user'] else 'N/A'
        expose_location = json_data['user']['expose_location'] if 'expose_location' in json_data['user'] else 'N/A'
        city = json_data['user']['city'] if 'city' in json_data['user'] else 'N/A'
        country_title = json_data['user']['country_title'] if 'country_title' in json_data['user'] else 'N/A'
        is_hated = json_data['user']['is_hated'] if 'is_hated' in json_data['user'] else 'N/A'
        hates_you = json_data['user']['hates_you'] if 'hates_you' in json_data['user'] else 'N/A'
        view_profile = json_data['user']['can_view_profile'] if 'can_view_profile' in json_data['user'] else 'N/A'

        # Verification details
        verification_mail = json_data['user']['verification']['email']['valid'] if 'verification' in json_data[
            'user'] and 'email' in json_data['user']['verification'] else 'N/A'
        verification_facebook = json_data['user']['verification']['facebook']['valid'] if 'verification' in json_data[
            'user'] and 'facebook' in json_data['user']['verification'] else 'N/A'
        verification_google = json_data['user']['verification']['google']['valid'] if 'verification' in json_data[
            'user'] and 'google' in json_data['user']['verification'] else 'N/A'
        verification_phone = json_data['user']['verification']['phone']['valid'] if 'verification' in json_data[
            'user'] and 'phone' in json_data['user']['verification'] else 'N/A'

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
        print(f"An error occurred in user: {e}")
        print("Traceback:")
        traceback.print_exc()

        # Print the values of relevant variables
        # ... (print other relevant variables)
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
