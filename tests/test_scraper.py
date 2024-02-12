import pytest
import requests_mock
from src.scraper import GoodreadsScraper

@pytest.fixture
def goodreads_scraper():
    years = ['21']  # Example year for the test, not relevant for fetch_page
    categories = ['fiction']  # Example category for the test, not relevant for fetch_page
    return GoodreadsScraper(years, categories)

def test_fetch_page_success(goodreads_scraper):
    mock_url = "https://mockedgoodreads.com/success"
    with requests_mock.Mocker() as m:
        m.get(mock_url, text='Mocked page content for success scenario')
        soup = goodreads_scraper.fetch_page(mock_url)
        assert soup is not None
        assert "Mocked page content for success scenario" in str(soup)

def test_fetch_page_failure(goodreads_scraper):
    mock_url = "https://mockedgoodreads.com/notfound"
    with requests_mock.Mocker() as m:
        m.get(mock_url, status_code=404)
        soup = goodreads_scraper.fetch_page(mock_url)
        assert soup is None
