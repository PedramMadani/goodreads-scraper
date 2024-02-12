from scraper import GoodreadsScraper
from data_processing import to_csv

if __name__ == "__main__":
    """
    Main entry point for the script. Initializes the scraper, performs scraping,
    and saves the data to a CSV file.
    """
    # Generate a list of years from 2011 to 2023 as strings
    years = [str(year) for year in range(2011, 2024)]
    # Adjust the list to match the original format ('11', '12', ..., '23')
    years = [year[2:] for year in years]

    categories = [
        'fiction', 'historical-fiction', 'mystery-thriller', 'romance', 'romantasy',
        'fantasy', 'science-fiction', 'horror', 'young-adult-fantasy', 'young-adult-fiction',
        'debut-novel', 'nonfiction', 'memoir-autobiography', 'history-biography', 'humor'
    ]

    scraper = GoodreadsScraper(years, categories)
    scraper.scrape()
    to_csv(scraper.books_data, 'goodreads_books.csv')
