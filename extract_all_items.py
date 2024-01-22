import extract_token
import json


def scrapping_annonces(session, keyword):
    keyword = keyword.replace(" ","%20")
    #limit the research to 800 itms
    try:
        url = f"https://www.vinted.fr/api/v2/catalog/items?page=1&per_page=800&search_text={keyword}&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=6"
        check = session.get(url)
        check.raise_for_status()
        json_data = json.loads(check.text)
        a = 1
        # for item in json_data['items']:
        #     try:
        #
        #         (login, email, gender, item_count, followers_count, following_count,
        #          feedback_count, positive_feedback_count, neutral_feedback_count,
        #          negative_feedback_count, account_ban_date, is_account_ban_permanent,
        #          is_publish_photos_agreed, expose_location, city, country_title, business_account,
        #          total_items_count, verification_email, verification_facebook, verification_google,
        #          verification_phone, is_hated, hates_you, can_view_profile, item_titles_advice,
        #          ratings_advice, feedbacks_advice, item_id_dressing, item_title_dressing,
        #          item_brand_dressing, item_size_dressing, item_price_dressing, item_created_dressing,
        #          item_description_dressing, photo, date_advert, description_advert) = scrapping_user(s, annonce['user'][
        #             'id'], annonce['id'])
        #         dataset_annonce = pd.DataFrame(
        #             [[annonce['id'], annonce['title'], annonce['price'], annonce['brand_title'], annonce['status'],
        #               annonce['url'], annonce['promoted'],
        #               annonce['size_title'], annonce['favourite_count'], annonce['photo']['url'], date_advert,
        #               description_advert,
        #               annonce['user']['id'], login, email, gender, item_count, followers_count, following_count,
        #               feedback_count, positive_feedback_count, neutral_feedback_count,
        #               negative_feedback_count, account_ban_date, is_account_ban_permanent,
        #               is_publish_photos_agreed, expose_location, city, country_title, business_account,
        #               total_items_count, verification_email, verification_facebook, verification_google,
        #               verification_phone, is_hated, hates_you, can_view_profile, item_titles_advice,
        #               ratings_advice, feedbacks_advice, item_id_dressing, item_title_dressing,
        #               item_brand_dressing, item_size_dressing, item_price_dressing, item_created_dressing,
        #               item_description_dressing, photo]],
        #             columns=['id_advert', 'title_advert', 'price', 'brand', 'etat', 'url_advert', 'promoted', 'taille',
        #                      'favourite_count', 'photo_advert', 'date_advert',
        #                      'description_advert', 'idUser', 'login', 'email', 'gender', 'item_count',
        #                      'followers_count', 'following_count',
        #                      'feedback_count', 'positive_feedback_count', 'neutral_feedback_count',
        #                      'negative_feedback_count', 'account_ban_date', 'is_account_ban_permanent',
        #                      'is_publish_photos_agreed', 'expose_location', 'city', 'country_title', 'business_account',
        #                      'total_items_count', 'verification_email', 'verification_facebook', 'verification_google',
        #                      'verification_phone', 'is_hated', 'hates_you', 'can_view_profile', 'item_titles_advice',
        #                      'ratings_advice', 'feedbacks_advice', 'item_id_dressing', 'item_title_dressing',
        #                      'item_brand_dressing', 'item_size_dressing', 'item_price_dressing',
        #                      'item_created_dressing',
        #                      'item_description_dressing', 'photo']
        #         )
        #         dataset_final = pd.concat([dataset_final, dataset_annonce], axis=0, ignore_index=True)
        #     except Exception as e_annonce:
        #         print(f"Une erreur s'est produite lors du scraping d'une annonce : {e_annonce}")
        #
        #     time.sleep(1)  # Attendre 1 seconde avant le prochain appel API pour les annonces

        # print(dataset_final.shape)

    except Exception as e:
        print(f"Une erreur s'est produite lors du scraping des annonces : {e}")


if __name__ == '__main__':
    session = extract_token.vinted_session()

    # For educational purposes, let's consider a keyword with Iphone 15
    keyword = "Iphone 15"
    scrapping_annonces(session,keyword)
