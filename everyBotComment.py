from package.team1config import *
from package.team2config import *
import time
version = '0.1'
message = ""
full_bot_list = team_1_bot_list + team_2_bot_list

for bot in full_bot_list:
    subreddit = bot.subreddit('MemeEconomy')
    for submission in subreddit.hot(limit=2):
        if not submission.link_flair_text == "Welcome new users":
            for comment in submission.comments():
                if comment.author == "MemeInvestor_bot":
                    try:
                        comment.reply(message)
                    except praw.exceptions.APIException:
                        print('Got the rate limit, exiting now...')
                        exit()
    # Wait 10 minutes so you can try to not get the error
    time.sleep(600)
