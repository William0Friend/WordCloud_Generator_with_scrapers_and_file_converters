# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:44:04 2020

@author: willf
"""

import praw

reddit = praw.Reddit(
    client_id="EciGYb3VVf8V6g",
    client_secret="qlX04tWp3yPmWT0U_4ZgXx5dhtwDow",
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    username="William0Friend",
    password="Yoshi69@Yoshi69"
)

#reddit.read_only = True
print(reddit.read_only)  # Output: False


# assume you have a reddit instance bound to variable `reddit`
subreddit = reddit.subreddit("spinalcordinjuries")

print(subreddit.display_name)  # output: redditdev
print(subreddit.title)         # output: reddit development
print(subreddit.description)   # output: a subreddit for discussion of ...