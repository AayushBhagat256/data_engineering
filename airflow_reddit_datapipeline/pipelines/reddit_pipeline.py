from utils.constants import CLIENT_ID, OUTPUT_PATH
from utils.constants import SECRET

from etls.reddit_etl import connect_reddit, load_data_to_csv
from etls.reddit_etl import extract_posts
from etls.reddit_etl import transform_data

import pandas as pd

def reddit_pipeline(filename:str,subreddit:str,time_filter='day',limit=None):
    # returning a particular instance of reddit here
    #1. connecting to reddit instance
    
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    # the function connect_reddit is called from etls and clientid and secret are called from utils/constants directory
    
    #2. extraction
    posts = extract_posts(instance,subreddit,time_filter,limit)
    post_df = pd.DataFrame(posts)
    
    #3. transformation
    post_df = transform_data(post_df)
    #4. loading to csv
    file_path = f'{OUTPUT_PATH}/{filename}.csv'
    load_data_to_csv(post_df,file_path)
    
    return file_path