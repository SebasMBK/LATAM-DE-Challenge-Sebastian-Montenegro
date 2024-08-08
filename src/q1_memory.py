from typing import List, Tuple, Iterator
from datetime import datetime
import json
from collections import defaultdict, Counter

def file_yielder(file_path: str) -> Iterator[dict] | None:
    """
    Yield one line at the time from the JSON file

    Parameters:
    file_path (str): The path of the file to read from

    Yields:
    Iterator[dict]: An iterator of dictionaries parsed from JSON lines in the file
    
    Exceptions:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If there is an error decoding a JSON line
    """
    try:
        with open(file_path, encoding='latin-1') as file:
            for line in file:
                yield json.loads(line)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None