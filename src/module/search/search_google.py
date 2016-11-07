import json, requests

class SearchGoogle(object):

    def get_wikipedia_title(query):
        result = SearchGoogle.search(query, site_search="pt.wikipedia.org")

        return result[0]['title'].replace(" – Wikipédia, a enciclopédia livre", "")


    def search(query, site_search=None):
        url = 'https://www.googleapis.com/customsearch/v1'

        #?key=AIzaSyAEBYgBJS0IdcJGp89pxgae_q6qokO5c78&cx=014959246475138655477:gtpu-_eye04&q=hello'

        params = dict(
            key = "AIzaSyAEBYgBJS0IdcJGp89pxgae_q6qokO5c78",
            cx = "014959246475138655477:gtpu-_eye04",
            q = query
        )

        if site_search is not None:
            params['siteSearch'] = site_search

        data = requests.get(url=url,params=params)
        output = data.json()

        return output['items']
