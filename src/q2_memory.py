from typing import List, Tuple, Iterator
import json
import regex as re
import emoji
from collections import Counter

def extract_emojis_from_tweet(tweet_content: str) -> Iterator[str]:
    """
    Extract emojis from the tweet content

    Parameters:
    tweet_content (str): The content of the tweet

    Yields:
    Iterator[str]: An iterator of emojis found in the tweet content
    """
    # Extract grafemas (the minimum units of a language) from the tweet content
    grafemas = re.findall(r'\X', tweet_content)
    for grafema in grafemas:
        # Check if the data contains any emoji and yield it
        if any(char in emoji.EMOJI_DATA for char in grafema):
            yield grafema

def count_emojis_in_file(file_path: str) -> Counter | None:
    """
    Count the occurrences of each emoji in a file containing tweet data

    Parameters:
    file_path (str): The name of the file to read from

    Returns:
    Counter: A Counter object with the count of each emoji found in the file
             Returns None if the file is not found or JSON decoding fails

    Exceptions:
    FileNotFoundError: If the file is not found
    json.JSONDecodeError: If there is an error decoding a JSON line
    """
    emoji_counter = Counter()
    try:
        with open(file_path, encoding='latin-1') as file:
            for line in file:
                obj = json.loads(line)
                tweet_content = obj['content']
                # Extract emojis from the tweet content and update the counter
                for emoji_char in extract_emojis_from_tweet(tweet_content):
                    emoji_counter[emoji_char] += 1
        return emoji_counter
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    pass