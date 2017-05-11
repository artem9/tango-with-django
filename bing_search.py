import urllib
import os
import requests


def read_bing_key():
    """
    Reads the BING API key from a file called 'bing.key'.
    returns: a string which is either None, i.e. no key found, or with a key.
    Remember: put bing.key in your .gitignore file to avoid committing it!
    """
    # See Python Anti-Patterns - it's an awesome resource!
    # Here we are using "with" when opening documents.
    # http://docs.quantifiedcode.com/python-anti-patterns/maintainability/

    bing_api_key = None
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    key_file = os.path.join(cur_dir, 'bing.key')

    try:
        with open(key_file, 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key


def run_query(search_terms):
    """
    Given a string containing search terms (query),
    returns a list of results from the Bing search engine.
    """
    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError('Bing Key Not Found')

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': bing_api_key,
    }

    params = urllib.urlencode({
        # Request parameters
        'q': search_terms,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safesearch': 'Moderate',
    })

    results = []

    try:
        url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
        r = requests.get(url, params=params, headers=headers)
        json_response = r.json()
        for result in json_response['webPages']['value']:
            results.append({'title': result['name'],
                            'link': result['url'],
                            'summary': result['snippet']})

    except:
        print("Error when querying the Bing API")

    # Return the list of results to the calling function.
    return results


def main():
    text = raw_input()
    result = run_query(str(text))
    print (result)

if __name__ == '__main__':
    main()
