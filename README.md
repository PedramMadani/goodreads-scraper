# Goodreads Scraper

## Introduction
The Goodreads Scraper is a Python tool designed for extracting book information from Goodreads, focusing on the Choice Awards sections. It aims to facilitate data analysis on book trends across various genres and years.

## Features
- Extracts book details: title, author, average rating, genre, and summary.
- Customizable for different years and categories.
- Outputs data in CSV format for easy analysis.

## Installation
```bash
# Clone the repository
git clone https://github.com/PedramMadani/goodreads-scraper.git

# Navigate to the project directory
cd goodreads-scraper

# Create and activate a virtual environment
## Windows
python -m venv goodreads-env
.\goodreads-env\Scripts\activate
## macOS/Linux
python3 -m venv goodreads-env
source goodreads-env/bin/activate
```
# Install dependencies
pip install -r requirements.txt
Usage
Run the scraper with the following command:

Copy code
```python
python src/main.py
```
This initiates the scraper, saving the data to goodreads_books.csv.

# Contributing
Contributions are welcome! Here's how you can contribute:

1- Fork the Project 

2- Create your Feature Branch (git checkout -b feature/AmazingFeature)

3- Commit your Changes (git commit -m 'Add some AmazingFeature')

4- Push to the Branch (git push origin feature/AmazingFeature)

5- Open a Pull Request

# License
This project is licensed under the MIT License. See the LICENSE file in the project repository for more information.

# Acknowledgments
Thanks to BeautifulSoup and Requests for HTML parsing and HTTP requests.

Pandas for data manipulation and analysis capabilities.
This project is not affiliated with Goodreads.
