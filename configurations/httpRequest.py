import requests
from configurations import constant


class SiteMapRequest:

    @staticmethod
    def get_sitemap_data():
        response = requests.get(constant.siteMapURL)
        return response
