import praw
import pandas as pd

posts = []

reddit = praw.Reddit(
    client_id='hd3RcQEYVyqZpw', 
    client_secret='KCMqXYVm9NH8tmmYQxaegXxhLPa3EQ', 
    user_agent='Momentum Trading Bot')

rs = reddit.subreddit('stocks')
wsb = reddit.subreddit('wallstreetbets')
ps = reddit.subreddit('pennystocks')

for post in rs.new(limit=1000):
    if post.link_flair_text == 'Ticker News':
        posts.append([post.title, post.score, post.subreddit, post.url, 
                      post.num_comments, post.selftext, post.created_utc])
        
for post in wsb.new(limit=1000):
    if post.link_flair_text == 'DD':
        posts.append([post.title, post.score, post.subreddit, post.url, 
                      post.num_comments, post.selftext, post.created_utc])
        
for post in ps.new(limit=1000):
    if post.link_flair_text == 'DD':
        posts.append([post.title, post.score, post.subreddit, post.url, 
                  post.num_comments, post.selftext, post.created_utc])
        
posts = pd.DataFrame(posts, columns = ['Title', 'Score', 'Subreddit', 'URL', 'Number of Comments', 'Post Content', 'Created'])

posts.to_csv("C:/Users/manuh/Documents/GitHub/Momentum Trading Bot/test.csv")

