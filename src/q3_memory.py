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

def count_mentions(file_name: str) -> List[Tuple[str, int]]:
    """
    Count the occurrences of each mentioned username in a file containing tweet data

    Parameters:
    file_name (str): The name of the file to read from

    Returns:
    List[Tuple[str, int]]: A list of tuples containing a username and its count for the top 10 most frequently mentioned usernames
    """
    counter = Counter()
    lines = file_yielder(file_name=file_name)
    if lines:
        for line in lines:
            # Extract the list of mentioned users
            mentioned_users = line['mentionedUsers']
            if mentioned_users:
                # Update the counter with the mentioned usernames
                counter.update(user['username'] for user in mentioned_users)
        # Get the top 10 most common mentions
        top_10_mentions = counter.most_common(10)
    else:
        top_10_mentions = []
    return top_10_mentions
    
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Provides the top 10 most frequently mentioned usernames

    Parameters:
    file_path (str): The path to the file containing tweet data

    Returns:
    List[Tuple[str, int]]: A list of tuples containing a username and its count for the top 10 most frequently mentioned usernames
    """
    # Get the answer by counting mentions from the file
    answer = count_mentions(file_name=file_path)
    return answer