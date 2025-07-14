import sys

import numpy as np
import pandas as pd

from praw import Reddit
import praw

from utils.constants import POST_FIELDS




def connect_reddit(client_id,client_secret,user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent
                             )
        print("Connected to Reddit")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_posts(reddit_instance:Reddit, subreddit:str, time_filter:str, limit:None):
    #Function to extract posts...
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit) #here variable and param is of same name in posts we used the variable one
    
    post_lists = []
    
    # print(posts)
    
    for post in posts:
        post_dict = vars(post)
        # print(post_dict)
        # continue with post fields
        post = {key : post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)
    # print(post_lists)
    return post_lists

def transform_data(post_df : pd.DataFrame) :
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    # Example: A value like 1625097600 (Unix timestamp) becomes 2021-06-30 12:00:00.
    
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    # Example: Any value that isn't explicitly True is set to False, ensuring consistency.
    
    post_df['author'] = post_df['author'].astype(str)
    # Example: A value like None becomes the string "None".
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    # edited column indicates whether a post has been edited. This transformation replaces any non-boolean values (e.g., timestamps or NaN) with the mode (most frequent value) of the column and ensures the column is boolean.
    
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)
    # post_df['selftext'] = post_df['selftext'].astype(str)
    
    

    return post_df

def load_data_to_csv(data : pd.DataFrame, path: str):
    data.to_csv(path,index=False)
 
        