import requests
from bs4 import BeautifulSoup
from utils import setup_logging

class GoodreadsScraper:
    """
    A scraper for Goodreads Choice Awards pages.
    """
    BASE_URL = "https://www.goodreads.com/choiceawards/best-"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3"
    HEADERS = {"User-Agent": USER_AGENT}

    def __init__(self, years, categories):
        self.logger = setup_logging(__name__)
        self.years = years
        self.categories = categories
        self.books_data = []

    def fetch_page(self, url):
        """
        Fetches a page by URL and returns its BeautifulSoup object, or None if the fetch fails.
        """
        try:
            response = requests.get(url, headers=self.HEADERS)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            return BeautifulSoup(response.text, 'html.parser')
        except requests.HTTPError as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
        except requests.RequestException as req_err:
            self.logger.error(f"Request exception: {req_err}")
        except Exception as e:
            self.logger.critical(f"Unexpected error when fetching page {url}: {e}")
        return None

    def parse_book_details(self, book_page):
        """
        Parses book details from a book page BeautifulSoup object.
        """
        try:
            details = {
                'title': book_page.find('h1', class_='Text Text__title1').get_text(strip=True),
                'author': book_page.find('a', class_='ContributorLink').get_text(strip=True),
                'average_rate': book_page.find('div', class_='RatingStatistics__rating').get_text(strip=True),
                'genre': book_page.find('span', class_='BookPageMetadataSection__genreButton').get_text(strip=True),
                'summary': book_page.find('span', class_='Formatted').get_text(strip=True),
                'link': book_page.find('a')['href']
            }
            return details
        except AttributeError as attr_err:
            self.logger.warning(f"Missing expected book detail: {attr_err}")
        except Exception as e:
            self.logger.critical(f"Unexpected error when parsing book details: {e}")
        return {}

    def scrape_category(self, category, year):
        """
        Scrapes a specific category for a given year.
        """
        url = f"{self.BASE_URL}{category}-books-20{year}"
        category_page = self.fetch_page(url)
        if category_page is None:
            self.logger.info(f"Category {category} for year 20{year} is not available. Skipping...")
            return

        books = category_page.find_all('div', class_='inlineblock pollAnswer resultShown')
        for book in books:
            book_link = 'https://www.goodreads.com' + book.find('a')['href']
            book_page = self.fetch_page(book_link)
            if book_page:  # Ensure the book page was successfully fetched
                book_details = self.parse_book_details(book_page)
                if book_details:  # Check if book details were successfully parsed
                    book_details['year'] = '20' + year
                    book_details['category'] = category
                    self.books_data.append(book_details)
                else:
                    self.logger.info(f"Failed to parse details for book at {book_link}")

    def scrape(self):
        """
        Scrapes all specified categories for all specified years.
        """
        for year in self.years:
            for category in self.categories:
                self.scrape_category(category, year)
