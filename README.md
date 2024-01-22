# Educational Vinted API Interaction Example
This project serves as an educational example of interacting with the Vinted API using Python and the requests 
library. Please note that this code is intended for educational purposes only, and any actual use must comply with 
Vinted's terms of service.

## 1. Extract the Token - extract_token.py

The "extract_token.py" script is designed for educational purposes to facilitate the retrieval of authentication tokens from the Vinted website. The process involves establishing a connection to Vinted, extracting the token, and gaining insights into the token mechanism and authentication flow.

**Key Points:**
- **Educational Purpose:** This script is intended to enhance understanding, emphasizing that fetching tokens continuously may not be necessary as the token remains consistent.
- **Token Mechanism Exploration:** Users are encouraged to explore and comprehend the intricacies of the token retrieval process as part of their learning journey.
- **Terms of Service Awareness:** It is crucial to note that extracting tokens from websites without proper authorization is generally against the terms of service.
- **Responsible Use:** The educational exercise is intended to foster awareness and knowledge of the authentication process and should not be misused for unauthorized access or activities.

## 2. Extract Information from a User - extract_user_information.py

The "extract_user_information.py" script is specifically designed to gather comprehensive information about a Vinted user using their member ID. Leveraging the Vinted API, the script establishes an authenticated session and retrieves a variety of user details, providing valuable insights into their Vinted profile.

**Extracted Information:**
- User's login name
- Item count in their profile
- Number of followers
- Number of accounts they are following
- Feedback rate
- Count of meeting transactions
- Profile photo URL
- Business account status
- Verification details, including email, Facebook, Google, and phone verification

**Usage:**
1. **Setup Vinted Session:** Ensure dependencies are installed and run the script using an authenticated Vinted session obtained from the "extract_token" module.
2. **Specify Member ID:** Replace the placeholder member ID with the actual ID of the Vinted user you want to investigate.
3. **Run the Script:** Execute the script to retrieve and print the user's information.

**Important Note:**
- This script is intended for educational purposes only, and users are encouraged to respect Vinted's terms of service and policies.
- Responsible and ethical coding practices should be followed to ensure proper use of the provided tools and knowledge.

## 3. Extract Information about Sold product of a user - extract_sold_products.py
The "extract_sold_products.py" script is developed to gather information about products sold by a Vinted user, 
specifically focusing on feedback received for those transactions. Leveraging the Vinted API, the script establishes an 
authenticated session and retrieves details such as the item title, feedback description, and rating for each sold 
product.

1. **Educational Purpose:**
    - This script is designed for educational purposes to enhance understanding of the Vinted API and the 
    - feedback mechanism associated with sold products.

2. **Usage:**
    - To utilize the script, ensure you have the necessary dependencies installed, including the `extract_user_information` and `extract_token` modules.
    - Create a Vinted session with an authenticated token using the `extract_token.vinted_session()` function.
    - Specify the member ID of the Vinted user you want to investigate in the `member_id_to_search` variable.
    - Run the script to extract information about products sold by the specified user.
    - 
3. **Explanation**
    - A Vinted session is created using the `extract_token.vinted_session()` function to ensure authenticated access to the Vinted API.
    - The script utilizes the `extract_user_information` module to retrieve essential information about the specified Vinted user. This information includes the user's login name, item count, followers, follows, feedback rate, feedback count, meeting transactions, profile photo URL, business account status, and verification details.
    - The script then checks if the user has received feedback for sold products. If feedback is present, it constructs an API endpoint to fetch the user's feedback information.
    - The feedback information is retrieved and processed, including details such as the item title, feedback description, and rating for each sold product. The data is organized into a dictionary for further analysis or presentation.
    - To avoid rate limiting from the Vinted API, the script pauses for 1 second between each feedback request.

**Important Note:**
- This script is intended for educational purposes only, and users are encouraged to respect Vinted's terms of service and policies.
- Responsible and ethical coding practices should be followed to ensure proper use of the provided tools and knowledge.


## 4. Extract current items to sell from a user - extract_current_products.py

The "extract_current_products.py" script is developed to gather detailed information about the current items listed for sale by a Vinted user. It leverages the Vinted API, establishing an authenticated session to retrieve key details such as the product ID, title, size, creation date, updated date, brand, price, image URL, and boosted status for each item.

1. **Educational Purpose:**
    - This script is crafted for educational purposes, aiming to provide insights into the process of extracting information about a Vinted user's current listings.

2. **Usage:**
    - Before running the script, make sure to install the necessary dependencies, including the `extract_user_information` and `extract_token` modules.
    - Create a Vinted session with an authenticated token using the `extract_token.vinted_session()` function.
    - Specify the member ID of the Vinted user you want to investigate in the `member_id_to_search` variable.
    - Execute the script to extract detailed information about the user's current items for sale.

3. **Explanation:**
    - The script begins by establishing a Vinted session using the `extract_token.vinted_session()` function to ensure authenticated access to the Vinted API.
    - It utilizes the `extract_user_information` module to retrieve essential information about the specified Vinted user, including the user's login name, item count, followers, follows, feedback rate, feedback count, meeting transactions, profile photo URL, business account status, and verification details.
    - The script then checks if the user has listed any products for sale. If items are present, it constructs an API endpoint to fetch information about the user's current products.
    - Information about each item, including the product ID, title, size, creation date, updated date, brand, price, image URL, and boosted status, is retrieved and organized into a dictionary for further analysis or presentation.
    - To avoid rate limiting from the Vinted API, the script includes a 1-second pause between requests.

**Important Note:**
- This script is designed for educational purposes, and users are encouraged to adhere to Vinted's terms of service and policies.
- Ethical coding practices should be followed to ensure responsible use of the provided tools and knowledge.


## 5. Extract all the items from a key search - extract_all_items.py
