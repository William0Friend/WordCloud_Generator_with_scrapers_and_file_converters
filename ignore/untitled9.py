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
hot_python = subreddit.hot(limit=1)#because first two are stickies!!!

for submission in hot_python:
    if not submission.stickied:
        with open('console.txt', 'a', encoding='utf-8') as txt:
            #print('\n*****Title: {}, ups: {}, downs {}, visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
            #txt.write('\nTitle: {}, ups: {}, downs {}, visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
            #txt.write('\n')
            comments = submission.comments.list()#convert comments to list
            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                txt.write('Parent ID:'+ str(comment.parent()) + '\n' + 'Comment ID:' + str(comment.id) + '\n' + 'Comment Body:' + str(comment.body) + '\n')
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
                """
                if len(comment.replies) > 0:
                        for reply in comment.replies:
                            #print(20 * '*')
                            txt.write(20 * '*' + '\n')
                            #print('Reply: ', reply.body)
                            txt.write('Reply: ' + str(reply.body) + '\n')
                """