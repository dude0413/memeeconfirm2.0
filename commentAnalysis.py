from package.team1config import *
from package.team2config import *

all_bots = team_1_bot_list + team_2_bot_list

for bot in all_bots:
    for item in bot.inbox.comment_replies(limit=5):
        if item.author == "MemeInvestor_bot":
            body = item.body
            print(body)