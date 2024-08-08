from typing import List, Tuple, Iterator
import json
from collections import Counter

def file_yielder(file_name: str) -> Iterator[dict] | None:
    """
    Yield JSON objects from a file one line at a time

    Parameters:
    file_name (str): The name of the file to read from

    Yields:
    Iterator[dict]: An iterator of dictionaries parsed from JSON lines in the file
    
    Exceptions:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If there is an error decoding a JSON line
    """
    try:
        with open(file_name, encoding='latin-1') as file:
            for line in file:
                # Yield each line
                yield json.loads(line)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_name}.")
        return None
    
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    pass