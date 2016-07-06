
# coding: utf-8

# ## MISSION PART ONE: GETTING DATA
# * You are going to scrape the front page of reddit every 4 hours, saving a CSV file that includes:
# 1. The title of the post
# 2. The number of votes it has (the number between the up and down arrows)
# 3. The number of comments it has
# 4. What subreddit it is from (e.g. /r/AskReddit, /r/todayilearned)
# 5. When it was posted (get a TIMESTAMP, e.g. 2016-06-22T12:33:58+00:00, not "4 hours ago")
# 6. The URL to the post itself
# 7. The URL of the thumbnail image associated with the post

# For the purposes of this exercise I shall be scraping https://www.reddit.com/r/funny/ because who doesn't want funny e-mails coming in at 8am every morning? I am going to regret this aren't I.

# In[11]:

import requests
from bs4 import BeautifulSoup


# In[12]:

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# In[13]:

#Grab the reddit site
response = requests.get("https://www.reddit.com/r/funny/", headers=headers)


# In[14]:

doc = BeautifulSoup(response.text, 'html.parser')


# In[78]:

#doc


# In[21]:

#Grab the posts

posts = doc.find_all('div', {'class': 'thing'})
#len(posts)


# In[83]:

#posts


# In[107]:

all_posts = []

#Let's grab the title of the posts
for post in posts:
    #Titles are <a> and title
    title = post.find('a', {'class': 'title'})
    title_text = title.text.strip()
    #Votes are <div> <score>
    vote = post.find('div', {'class': 'score'})
    vote_text = vote.text.strip()
    #Comments are <a> and bylink
    comment = post.find('a', {'class': 'bylink'})
    comment_text = comment.text.strip()
    #When it was posted <time> datetime
    time = post.find('time', {'class': 'live-timestamp'})['datetime']
    #URL
    link = post.find('a', {'class': 'title'})['href']
    #URL link
    thumbnail = post.find('img')
    if thumbnail:
        thumbnail = "http:" + (thumbnail['src'])
    funny_posts = {'title': title_text, 'votes': vote_text, 'comments': comment_text, 'timestamp': time, 'link': link, 'thumbnail': thumbnail}
    all_posts.append(funny_posts)
all_posts
    
#QUESTION: How to replace /r/ with link? Do we use regular expressions?


# In[108]:

#len(all_posts)


# In[109]:

import pandas as pd


# In[111]:

posts_df = pd.DataFrame(all_posts)
posts_df.head()


# In[112]:

import time


# In[113]:

datestring = time.strftime("%Y-%m-%d-%H-%M")
datestring


# In[115]:

filename = "reddit-data" + datestring + ".csv"
posts_df.to_csv(filename, index=False)


# In[ ]:



