import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))
# the above basically gets the location of the config directory where we will have the keys and confidential material

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

# AWS
AWS_ACCESS_KEY_ID = parser.get('aws','aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws','aws_secret_access_key')
AWS_REGION = parser.get('aws','aws_region')
AWS_BUCKET_NAME = parser.get('aws','aws_bucket_name')



INPUT_PATH = parser.get('file_paths','input_path')
OUTPUT_PATH = parser.get('file_paths','output_path')

POST_FIELDS = (
    'id',
    'title',
    # 'selftext',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    # 'upvote_ratio',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)