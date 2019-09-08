#!/usr/bin/python 

import os, praw, pymysql

reddit = praw.Reddit (
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent=os.environ['USER_AGENT']
)

db = pymysql.connect (
    host=os.environ['MYSQL_HOSTNAME'],
    user='redditapi',
    passwd='pass',
    db='redditeye',
    charset='utf8',
    autocommit=True
)
cursor = db.cursor(pymysql.cursors.DictCursor)
    
for comment in reddit.subreddit('all').stream.comments():
    print(comment.body)
    reddit_id = str(comment.id)
    body = str(comment.body)
    author = str(comment.author)
    subreddit = str(comment.subreddit)
    cursor.execute("INSERT INTO `comments` (`reddit_id`, `body`, `author`, `subreddit`) VALUES ('"+reddit_id+"', %s, '"+author+"', '"+subreddit+"')", body)