from typing import List, Tuple
import json
import regex as re
import emoji
import pandas as pd

def read_and_load_data(file_path: str) -> List[str] | None:
    """
    Read JSON objects from a file and extract emojis from the content

    Parameters:
    file_path (str): The path to the file to read from

    Returns:
    List[str] | None: A list of emojis found in the content
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
                tweet_content = obj['content']
                # Extract grafemas (the minimum units of a language) from the content
                grafemas = re.findall(r'\X', tweet_content)
                for grafema in grafemas:
                    # Check if there are any emojis and append to the data list
                    if any(char in emoji.EMOJI_DATA for char in grafema):
                        data.append(grafema)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

def count_emojis(data: List[str]) -> List[Tuple[str, int]]:
    """
    Count the occurrences of each emoji and return the top 10 most frequent ones

    Parameters:
    data (List[str]): A list of emojis extracted from the tweet content

    Returns:
    List[Tuple[str, int]]: A list of tuples containing an emoji and its count for the top 10 most frequent emojis
    """
    # Count the occurrences of each emoji
    emojis_count = pd.Series(data).value_counts().nlargest(n=10)
    # Convert the counts to a list of tuples
    result = list(zip(emojis_count.index, emojis_count))
    return result

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    pass