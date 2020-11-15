# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:37:16 2020

@author: willf
"""

import praw
import csv

reddit = praw.Reddit(client_id = '_6THrUR76FgnHg',
                     client_secret = 'YdfybtUkBsOH-9tdY1io53PE7u9D-Q',
                     username = 'ResearchTeamChang',
                     password = 'cookies@cookies',
                     user_agent = 'Mozilla/5.0'
                     )

#rebuild comment tree parent id, comment, all replies

#subreddit = reddit.subreddit("news")

#console
subreddit = reddit.subreddit('spinalcordinjuries')
hot_python = subreddit.hot(limit=None)#because first two are stickies!!!
try:
    for submission in hot_python:
        if not submission.stickied:
            with open('wordcloud.txt', 'a', errors='Ignore',encoding='utf-8') as txt:
                txt.write(str(submission.title))
                comments = submission.comments.list()#convert comments to list
                submission.comments.replace_more(limit=0)
                #for title in submission: 
                #    txt.write(str(submission.title))
                for comment in submission.comments:
                    #txt.write(str(submission.title))
                    txt.write(str(comment.body) + '\n')
                for comment_replies in submission.comments:
                    if len(comment_replies.replies) > 0:
                        for reply in comment_replies.replies:
                            txt.write( str(reply.body))
                    #else:
                    #    txt.write(str(submission.title) + ',' + str(comment.body) + ',' + '*no reply*' + ',' + str(submission.id) + ',' + str(comment.id) + ',' + '*no repy id*' )
                    #    txt.write('\n')
              
except praw.exceptions.PRAWException as e:
    print(str(e))
except AssertionError as e:
    print(str(e))
       


"""
                    #print(20 * '-')
                    #txt.write(20 * '-' + "\n")
                    #print('Parent ID:' , comment.parent())
                    #txt.write('Parent ID:'+ str(comment.parent()) + '\n',
                    #          'Comment ID:' + str(comment.id) + '\n',
                    #          'Comment Body:' + str(comment.body) + '\n'
                    #          )
                    #print(str(comment.parent()) + '\n', file=txt)
                    #print('Comment ID:', comment.id)
                    #txt.write('Comment ID:' + str(comment.id) + '\n')
                    #print(str(comment.id) + '\n', file=txt)
                    #print('Comment Body:', comment.body)
                    #txt.write('Comment Body:' + str(comment.body) + '\n')
                    #print(comment.body, file=txt)
                    
                    if len(comment.replies) > 0:
                            for reply in comment.replies:
                                #print(20 * '*')
                                txt.write(20 * '*' + '\n')
                                #print('Reply: ', reply.body)
                                txt.write('Reply: ' + str(reply.body) + '\n')
""" 
