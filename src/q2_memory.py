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

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    pass