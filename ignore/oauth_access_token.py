# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:22:13 2020

@author: willf

reddit@reddit-VirtualBox:~$ curl -X POST -d 'grant_type=password&username=reddit_bot&password=snoo' --user 'p-jcoLKBynTLew:gko_LXELoV07ZBNUXrvWZfzE3aI' https://www.reddit.com/api/v1/access_token
{
    "access_token": "J1qK1c18UUGJFAzz9xnH56584l4", 
    "expires_in": 3600, 
    "scope": "*", 
    "token_type": "bearer"
}

reddit@reddit-VirtualBox:~$ curl -H "Authorization: bearer J1qK1c18UUGJFAzz9xnH56584l4" -A "ChangeMeClient/0.1 by YourUsername" https://oauth.reddit.com/api/v1/me
{
    "comment_karma": 0, 
    "created": 1389649907.0, 
    "created_utc": 1389649907.0, 
    "has_mail": false, 
    "has_mod_mail": false, 
    "has_verified_email": null, 
    "id": "1", 
    "is_gold": false, 
    "is_mod": true, 
    "link_karma": 1, 
    "name": "reddit_bot", 
    "over_18": true
}


"""
import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('EciGYb3VVf8V6g', 'qlX04tWp3yPmWT0U_4ZgXx5dhtwDow')
post_data = {"grant_type": "password", "username": "William0Friend", "password": "Yoshi69@Yoshi69"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())