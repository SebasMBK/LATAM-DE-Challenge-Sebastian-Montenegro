from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd

def read_and_load_data(file_path: str) -> List[List[str]] | None:
    """
    Read JSON objects from a file and load specific fields into a list of lists

    Parameters:
    file_path (str): The path to the file to read from

    Returns:
    List[List[str]] | None: A list of lists where each list contains the date and username from a tweet
                            Returns None if the file is not found or JSON decoding fails

    Exceptions:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If there is an error decoding a JSON line
    """
    data = []
    try:
        with open(file_path, encoding='latin-1') as file:
            for line in file:
                obj = json.loads(line)
                # Extract the date and username and append to the data list
                lst_data = [obj['date'], obj['user']['username']]
                data.append(lst_data)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    pass