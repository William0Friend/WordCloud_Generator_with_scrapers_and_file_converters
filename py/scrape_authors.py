# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:37:16 2020

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
hot_python = subreddit.hot(limit=None)#because first two are stickies!!!
try:
    for submission in hot_python:
        if not submission.stickied:
            with open('authors.txt', 'a', errors='Ignore',encoding='utf-8') as txt:
                txt.write(str(submission.author) + '\n')
                comments = submission.comments.list()#convert comments to list
                submission.comments.replace_more(limit=0)
                for comment in submission.comments:
                    txt.write(str(comment.author) + '\n')
                for comment_replies in submission.comments:
                    if len(comment_replies.replies) > 0:
                        for reply in comment_replies.replies:
                            txt.write( str(reply.author) + '\n')
                    
except praw.exceptions.PRAWException as e:
    print(str(e))
except AssertionError as e:
    print(str(e))
 