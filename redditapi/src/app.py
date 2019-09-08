#!/usr/bin/python 

import os, praw

reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                     client_secret=os.environ['CLIENT_SECRET'],
                     user_agent=os.environ['USER_AGENT'])

for comment in reddit.subreddit('all').stream.comments():
    print(comment.body)