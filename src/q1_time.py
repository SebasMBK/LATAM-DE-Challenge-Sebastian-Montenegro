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

def find_answer(data: List[List[str]], cols: List[str]) -> List[Tuple[datetime.date, str]]:
    """
    Find the top 10 dates with the most tweets and the user who tweeted the most on each of those dates

    Parameters:
    data (List[List[str]]): A list of lists containing tweet data where each list contains the date and username
    cols (List[str]): Column names for the DataFrame

    Returns:
    List[Tuple[datetime.date, str]]: A list of tuples containing a date and the username of the top tweeter on that date
    """
    df = pd.DataFrame(data=data, columns=cols)
    # Convert the 'date' column to datetime.date objects
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Get the top 10 dates with the most tweets
    df_top_10_dates_tweets = df['date'].value_counts().sort_values(ascending=False).head(10)
    
    # Count the number of tweets per user per date
    df_users_tweets_per_date = df.groupby(['date', 'username']).size().reset_index(name='tweet_count')
    
    # Find the user with the most tweets on each date
    df_top_user_per_date = df_users_tweets_per_date.loc[df_users_tweets_per_date.groupby('date')['tweet_count'].idxmax()]
    
    # Join the top 10 dates with the corresponding top user
    df_top_10_date_wth_user = pd.merge(df_top_10_dates_tweets, df_top_user_per_date, on='date', how='left')[['date', 'username']]
    
    result = list(df_top_10_date_wth_user.itertuples(index=False, name=None))
    return result

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    pass