#поисковые частоты слов 

import requests
import urllib
import json
import operator
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):

    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://suggestqueries.google.com/complete/search?output=chrome&hl=en&q=" + query)
    results = json.loads(response.text)
    return results


search_term = "wintage"
results = get_results(search_term)
print(results)

def format_results(results):
    suggestions = []
    for index, value in enumerate(results[1]):
        suggestion = {'term': value, 'relevance': results[4]['google:suggestrelevance'][index]}
        suggestions.append(suggestion)
    return suggestions
formatted_results = format_results(results)
print(formatted_results)
