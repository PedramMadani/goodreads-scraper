import pytest
import csv
import os
from src.data_processing import to_csv

def test_to_csv(tmpdir):
    """
    Test the to_csv function to ensure it correctly writes data to a CSV file.
    """
    # Sample data to be written
    sample_data = [
        {'title': 'Book 1', 'author': 'Author 1', 'genre': 'Genre 1'},
        {'title': 'Book 2', 'author': 'Author 2', 'genre': 'Genre 2'}
    ]
    # Temporary file path
    file_path = tmpdir.join("test_books.csv")
    
    # Call the to_csv function
    to_csv(sample_data, str(file_path))
    
    # Verify the file exists
    assert os.path.exists(file_path)
    
    # Read the file back and verify content
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            assert row['title'] == sample_data[i]['title']
            assert row['author'] == sample_data[i]['author']
            assert row['genre'] == sample_data[i]['genre']

def test_to_csv_empty_data(tmpdir):
    """
    Test the to_csv function with an empty data list to ensure it handles empty data gracefully.
    """
    # Empty data list
    empty_data = []
    # Temporary file path for the empty data test
    file_path = tmpdir.join("empty_test_books.csv")
    
    # Call the to_csv function with empty data
    to_csv(empty_data, str(file_path))
    
    # Verify the file exists
    assert os.path.exists(file_path)
    
    # Verify the file is empty
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        assert len(csvfile.readlines()) == 1  # Expecting only the header line
