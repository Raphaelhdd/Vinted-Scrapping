import extract_user_information
import extract_token
import json
import time


def extract_sold_products(session, member_id):
    """
    Extracts information about products sold with feedback for a Vinted user.

    Args:
        session (requests.Session): Authenticated session with Vinted.
        member_id (int): The Vinted member ID.

    Returns:
        dict: Dictionary containing feedback information for sold products.
    """
    try:
        # Extract user information to get feedback count
        user_data = extract_user_information.extract_information_user(session, member_id)

        # Check if the user has feedback
        if user_data['feedback_count'] > 0:
            # Build API endpoint to fetch user feedbacks
            api_sold_products = f"https://www.vinted.fr/api/v2/user_feedbacks?user_id={member_id}&page=1&per_page=" \
                                f"{user_data['feedback_count']}&by=all"
            check_advice = session.get(api_sold_products)
            json_data = json.loads(check_advice.text)

            # Dictionary to store all feedback information
            all_feedback = {}

            # Iterate through each feedback
            for feedback in json_data['user_feedbacks']:
                id_feedback = feedback['id'] if 'id' in feedback else 'N/A'
                feedback_item_sold = feedback['item_title'] if 'item_title' in feedback else 'N/A'
                feedback_description = feedback['feedback'] if 'feedback' in feedback else 'N/A'
                rating_feedback = feedback['rating'] if 'rating' in feedback else 'N/A'

                # Store feedback information in a dictionary
                feedback_data = {
                    'feedback_item_sold': feedback_item_sold,
                    'feedback_description': feedback_description,
                    'rating_feedback': rating_feedback
                }

                # Add feedback information to the overall dictionary
                all_feedback[id_feedback] = feedback_data

                # Pause for 1 second to avoid rate limiting
                time.sleep(1)

            # Return the dictionary containing all feedback information
            return all_feedback

        else:
            print("This user has no feedback.")
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

    # Extract sold products feedback for the specified member ID
    feedback_data = extract_sold_products(session, member_id_to_search)

    # Print or process the extracted feedback information
    if feedback_data:
        print("Feedback Information:")
        for feedback_id, feedback_info in feedback_data.items():
            print(f"Feedback ID: {feedback_id}")
            for key, value in feedback_info.items():
                print(f"  {key}: {value}")
            print("\n")
