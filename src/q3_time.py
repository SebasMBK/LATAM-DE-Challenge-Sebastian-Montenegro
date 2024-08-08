from typing import List, Tuple
import json
import pandas as pd

def read_and_load_data(file_path: str) -> List[str] | None:
    """
    Read JSON objects from a file and extract mentioned usernames

    Parameters:
    file_path (str): The path to the file to read from

    Returns:
    List[str] | None: A list of mentioned usernames
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
                # Extract the list of mentioned users
                lst_data = obj['mentionedUsers']
                if lst_data:
                    # Extract usernames from the mentioned users
                    lst_data = [user['username'] for user in lst_data]
                    # Extend/flatten the data list with the extracted usernames
                    data.extend(lst_data)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    pass