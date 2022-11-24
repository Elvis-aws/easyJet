from configurations.httpRequest import SiteMapRequest


class TestSiteMap:

    def test_site_map_data(self):
        response = SiteMapRequest.get_sitemap_data()
        assert response.status_code == 200
        results = response.text
        publication_date = '2022-11-24T11:35:35+00:00'
        assert publication_date in results
        title = 'Who Will Headline the 2023 Glasto Festival?'
        assert title in results

