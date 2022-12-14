from pageObjects.homePage import HomePage
from pageObjects.footballPage import FootballPage
from pageObjects.leaguesCupPage import LeaguesCupPage
from pageObjects.pemierLeaguePage import PremierLeaguePage
from pageObjects.scoresAndFixturesPage import ScoresAndFixturesPage


class TestGambling:
    home_page = HomePage()
    football_page = FootballPage()
    league_cup_page = LeaguesCupPage()
    premier_league_page = PremierLeaguePage()
    scores_and_fixtures_page = ScoresAndFixturesPage()

    def test_get_fixtures(self):
        tottenham = 'Tottenham Hotspur'
        self.home_page.click_on_football_link()
        self.football_page.click_on_leagues_and_cup_link()
        self.league_cup_page.click_on_premier_league_link()
        self.premier_league_page.click_on_view_all_premier_league_fixtures_link()
        fixture = self.scores_and_fixtures_page.get_fixtures()
        assert fixture is not None

    def test_get_list_of_easy_games(self):
        easy_games = self.scores_and_fixtures_page.get_easy_games()
        assert easy_games is not None
