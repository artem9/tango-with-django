import json
import urllib, httplib


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
    try:
        with open('bing.key', 'r') as f:
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
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()

        json_response = json.loads(data)
        for result in json_response['webPages']['value']:
            results.append({'title': result['name'],
                            'link': result['url'],
                            'summary': result['snippet']})

        conn.close()
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
