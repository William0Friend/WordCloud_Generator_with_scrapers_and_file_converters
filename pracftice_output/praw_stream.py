# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:21:48 2020

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

#for comment in subreddit.stream.comments():
for comment in subreddit.comments():
    try:        
        print('parent_id:', comment.parent_id)
        print('body: ', comment.body)
        # parent_id = str(comment.parent())
    
        # original = reddit.comment(parent_id)#search for comment by id
        # print('Parent:' )
        # print(original.body)
        # print('Reply:')
        # print(comment.body)
    except praw.exceptions.PRAWException as e:
        print(str(e))
        #pass