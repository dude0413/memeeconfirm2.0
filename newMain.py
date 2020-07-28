import praw, datetime, random, os, time
from package.team1config import *
from package.team2config import *

# Create one bot with memeeconbot and then expand from there #
version = '1.0'
bot = dude
# Insert the submission post id, the contents and the bot that you would like to use #
def comment(interested_submission_post_id, contents, bot):
    submission = bot.submission(interested_submission_post_id)
    for investment_comment in submission.comments:
        if investment_comment.author == 'MemeInvestor_bot':
            try:
                investment_comment.reply(contents)
            except praw.exceptions.APIException:
                print('Got the rate limit, exiting now...')
                exit()

subreddit = bot.subreddit('MemeEconomy')
percentage_of_balance_invested = .75

# Portfolio message #
for submission in subreddit.hot(limit=2):
    # Don't use the first post because the MemeInvestor_bot doesn't look for comments in it #
    if not submission.link_flair_text == "Welcome new users":
        for comment in submission.comments:
            if comment.author == "MemeInvestor_bot":
                try:
                    comment.reply("!portfolio")
                except praw.exceptions.APIException:
                    print('Got the rate limit, exiting now...')
                    exit()
print('i got this far hehe')

# Get balance from portfolio #
for item in bot.inbox.comment_replies(limit=5):
    body = item.body
    # Find portfolio message
    if item.author == "MemeInvestor_bot" and body.split(' ', 1)[0] == 'Your':
        current_balance_message = body
        break
print('sleeping 10 minutes')

split_current_balance_message = current_balance_message.split()
balance = float(split_current_balance_message[17].replace('**', ''))
print('balance = ' + str(balance))
investment_boolean = False
while not investment_boolean:
    print('hahahaa')
    for searching_submission in subreddit.hot(limit=15):
        upvotes_on_checking_post = searching_submission.score
        checking_submission_created_formatted = searching_submission.created_utc
        now = time.time()
        time_boolean_sixty = (now - searching_submission.created_utc) <= 3600
        print('iteration')
        if time_boolean_sixty and upvotes_on_checking_post > 650:
            # Extract the price of the post #
            print('something got passed this with ' + str(upvotes_on_checking_post) + ' upvotes and an age of '
                  + str(checking_age))
            print('this is the state of time_boolean' + str(time_boolean_sixty))
            checking_flair = searching_submission.link_flair_text
            extractedFlair = checking_flair.replace("M¢", '')
            price = round(float(extractedFlair))
            amount = round(int(balance * percentage_of_balance_invested) / price)
            invest_message = "!buy " + str(amount)
            comment(searching_submission, invest_message, bot)
            print('Successfully invested in something')
            investment_boolean = True
            break

    time.sleep(600)
    print('sleeping for a lil bit')
print('All done, exiting the program now')
