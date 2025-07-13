from utils.constants import CLIENT_ID
from utils.constants import SECRET

from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts

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
    #4. loading to csv