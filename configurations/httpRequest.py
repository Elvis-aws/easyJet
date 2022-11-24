import requests
from utilities.readProperties import ReadConfig


class SiteMapRequest:

    @staticmethod
    def get_sitemap_data():
        url = ReadConfig.get_site_map_url()
        response = requests.get(url)
        return response
