# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:12:24 2020

@author: willf
"""

import praw

reddit = praw.Reddit(client_id = '_6THrUR76FgnHg',
                     client_secret = 'YdfybtUkBsOH-9tdY1io53PE7u9D-Q',
                     username = 'ResearchTeamChang',
                     password = 'cookies@cookies',
                     user_agent = 'Mozilla/5.0'
                     )
subreddit = reddit.subreddit('spinalcordinjuries')
hot_python = subreddit.hot(limit=3)#because first two are stickies!!!

for submission in hot_python:
    if not submission.stickied:
        print('*****Title: {}, ups: {}, downs {}, visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
        print(dir(submission))
       
        
"""
        comments = submission.comments.list()#convert comments to list
        submission.comments.replace_more(limit=0)
        for comment in submission.comments:
            print(dir(comment))
"""