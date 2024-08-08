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

def count_tweets(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Count tweets and determine the user who tweeted the most on the top 10 dates with the most tweets

    Parameters:
    file_path (str): The name of the file containing tweet data

    Returns:
    List[Tuple[datetime.date, str]]: A list of tuples containing the date and the username of the top tweeter on that date
    """
    # Initialize the counters and vars
    date_count = Counter()
    user_date_count = defaultdict(lambda: Counter())
    result = []

    # Start the generator for the json files
    lines = file_yielder(file_path=file_path)
    if lines:           
        for line in lines:
            # Parse the date and username from the JSON object
            date = datetime.fromisoformat(line['date']).date()
            username = line['user']['username']
            date_count[date] += 1
            user_date_count[date][username] += 1

        # Get the top 10 dates with the most tweets
        top_10_dates = date_count.most_common(10)

        # Find the user that tweeted the most on each of the top 10 dates
        for date, _ in top_10_dates:
            top_user = user_date_count[date].most_common(1)[0][0]
            result.append((date, top_user))
    return result