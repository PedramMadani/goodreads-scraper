import pandas as pd

def to_csv(data, filename):
    """
    Saves the given data to a CSV file.

    Args:
        data (list of dict): The data to save.
        filename (str): The filename for the CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
