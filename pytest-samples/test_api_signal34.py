import requests
import json
import jsonpath
import urllib.parse

baseUrl = "https://signal34.com/"

# Test cases to test the Signal34 API functions

def test_fetch_contents_without_parameters():
    path = "api/v030/content/all/"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.numFound')[0] > 0


def test_fetch_contents_with_parameters():
    path = "api/v030/content/all/"
    params = {'page_number': 1, 'per_page': 10, 'sort': 'score desc'}
    params_str = urllib.parse.urlencode(params)
    response = requests.get(url=baseUrl+path, params=params_str)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.numFound')[0] > 0

def test_search_contents_without_parameters():
    path = "api/v030/tags/search/"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.numFound')[0] > 0


def test_search_contents_by_string():
    path = "api/v030/tags/search/"
    params = {'query': 'tags_str:("Apache")'}
    params_str = urllib.parse.urlencode(params)
    response = requests.get(url=baseUrl+path, params=params_str)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.numFound')[0] > 0


def test_search_contents_by_string_no_results():
    path = "api/v030/tags/search/"
    params = {'query': 'tags_str:("fake test string")'}
    params_str = urllib.parse.urlencode(params)
    response = requests.get(url=baseUrl+path, params=params_str)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.numFound')[0] == 0
