import praw, datetime, random, os, time

# Create one bot with memeeconbot and then expand from there #
version = '1.0'

dude_username = 'dude0413'
dude_password = 'krul*aill6golt1MUNT'
dude_client_id = 'QgB5EYqXC1UaZQ'
dude_client_secret = 'XBNJ7ISvCANsOXCNjtCyvA1z_Fs'
bot = praw.Reddit(user_agent="Meme Economy Bot Trying to Win using Algorithms",
                  client_id=dude_client_id,
                  client_secret=dude_client_secret,
                  username=dude_username,
                  password=dude_password)

# Variables #
firstTimeNow = datetime.datetime.now()
log_file_name = str(firstTimeNow.strftime('%m.%d') + '..' + str(random.randint(1, 100)) + '.txt')

if os.path.isfile(log_file_name):
    print('Found the file')
else:
    invested_file = open(log_file_name, 'w+')
upvote_threshold = 650


# Functions #
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def log(stringInput, bot):
    timeNow = datetime.datetime.now()
    message = str(bot.user.me()) + ': ' + str(stringInput) + '\n' + str(timeNow.strftime('%m-%d %H:%M:%S'))
    print(message)
    with open(log_file_name, 'a') as l:
        l.write(message + '\n\n')

# Insert the submission post id, the contents and the bot that you would like to use #
def comment(interested_submission_post_id, contents, bot):
    submission = bot.submission(interested_submission_post_id)
    for comment in submission.comments():
        if comment.author == 'MemeInvestor_bot':
            try:
                comment.reply(contents)
            except praw.exceptions.APIException:
                print('Got the rate limit, exiting now...')
                exit()


subreddit = bot.subreddit('MemeEconomy')
global percentage_of_balance_invested
percentage_of_balance_invested = .75
# Search #
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
# Get balance from portfolio message #
inbox_comment_reply_list = []
for item in bot.inbox.comment_replies(limit=5):
    body = item.body
    # Find portfolio message
    if item.author == "MemeInvestor_bot" and body.split(' ', 1)[0] == 'Your':
        current_balance_message = body
        break
split_current_balance_message = current_balance_message.split()
global balance
balance = float(split_current_balance_message[17].replace('**', ''))
print('here is the balance: ' + str(balance))
global investment_boolean
investment_boolean = False
current_investment_boolean = False
print('Going to sleep for 10 minutes')
time.sleep(600)
# Invest #
def invest(post_id, shares, investing_bot):
    invest_message = "!buy " + str(shares)
    comment(post_id, invest_message, investing_bot)
    global investment_boolean
    investment_boolean = True

# Check the inputted post to see if it is good for investing #
global checking_boolean
checking_boolean = False
def check(post_id_checking):
    upvotes_on_checking_post = post_id_checking.score
    checking_flair = post_id_checking.link_flair_text
    checking_submission_created_formatted = post_id_checking.created_utc
    submission_time = datetime.datetime.utcfromtimestamp(checking_submission_created_formatted)
    checking_age = (datetime.datetime.now() - submission_time)
    time_boolean_sixty = checking_age < datetime.timedelta(minutes=60)
    if time_boolean_sixty and upvotes_on_checking_post > 650:
        # Extract the price of the post #
        if not hasNumbers(checking_flair):
            extractedFlair = checking_flair.replace("M¢", '')
            global price
            price = round(float(extractedFlair))
        checking_boolean = True
        return post_id_checking

# Search for a post to invest in and extract the submission_id #
def search():
    while not checking_boolean:
        for searching_submission in subreddit.hot(limit=15):
            check(searching_submission)


while not investment_boolean:
    # See if there are any posts in currently invested #
    # If not, search for a new one #
    # If there is, check if it is still good #
    # If it is bad, delete from currently invested #
    with open('currentlyinvestedin.txt') as r:
        already_invested_investments = r.read().splitlines()
    # If there isn't anything in currently invested, search for a post to invest in #
    if not already_invested_investments:
        extracted_investment = search()
        amount = (balance * percentage_of_balance_invested)/price
        invest(extracted_investment, bot, amount)
        print('invested in something lfmao')


