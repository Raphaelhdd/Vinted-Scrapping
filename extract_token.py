import cloudscraper


def vinted_session():
    """
        Create a session for interacting with Vinted using CloudScraper.

        This function creates a CloudScraper session, sets custom headers to mimic
        a legitimate user request, makes a GET request to the Vinted website to
        retrieve the CSRF token, extracts the CSRF token from the response text,
        and sets the extracted CSRF token in the headers for subsequent requests.

        Returns:
            cloudscraper.CloudScraper: A CloudScraper session configured for Vinted interactions.
        """
    # Create a CloudScraper session
    s = cloudscraper.create_scraper()

    # Set custom headers to mimic a legitimate user request
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.67 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    # Make a GET request to the Vinted website to retrieve the CSRF token
    req = s.get("https://www.vinted.fr/")

    # Extract the CSRF token from the response text
    csrf_token_index = req.text.find("CSRF_TOKEN")
    start_index = csrf_token_index + len("CSRF_TOKEN\":\"")
    end_index = req.text.find("\",", start_index)
    csrf_token_value = req.text[start_index:end_index]

    # Set the extracted CSRF token in the headers for subsequent requests
    s.headers['X-CSRF-Token'] = csrf_token_value

    return s

