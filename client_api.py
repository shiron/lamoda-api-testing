import requests, json

class ClientAPI():

    def __init__(self, url):
        self.url = url
        self.recommend_url = 'get_product_product_recommendations'

    def get_recommendations(self, sku, **kw):

        data = {'sku': sku}
        # add additional arguments
        for key in kw:
            data[key] = kw[key]

        r = requests.post(self.url + self.recommend_url, data=json.dumps(data))
        return r.status_code, json.loads(r.text)
