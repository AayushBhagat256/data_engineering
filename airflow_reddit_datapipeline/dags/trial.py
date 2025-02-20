import os
import sys

# e = os.path.abspath(__file__)
# print(f'The path is {e}')

print("Before:", sys.path)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("After:", sys.path)

"""
Before: ['C:\\Users\\Aayush Bhagat\\Desktop\\data_engineering\\airflow_reddit_datapipeline\\dags',..,..]
After:  ['C:\\Users\\Aayush Bhagat\\Desktop\\data_engineering\\airflow_reddit_datapipeline',..,..]
"""

"""
resume at 19:10
"""