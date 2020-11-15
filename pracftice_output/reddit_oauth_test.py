# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:48:12 2020

@author: willf
"""

import praw

reddit = praw.Reddit(
     client_id="bkuh9DzVDurIaA",
     client_secret="F7h2OBJGVTG_ZzO7P-e9q2a6hz5yGQ",
     user_agent="my user agent"
 )
 
for submission in reddit.subreddit("spinalcordinjuries").hot(limit=10):
    print(submission.title)
    print(submission.comments)
    print("--------------------------")