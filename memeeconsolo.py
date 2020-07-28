import praw, datetime, random, os, time
# Create one bot with memeeconbot and then expand from there #
# version = '1.0' #
"""
MEB_username = 'memeeconbot'
MEB_password = 'SPIB5poch!fich2noff'
MEB_client_id = '3CMfiAi1cCxq5A'
MEB_client_secret = '1jK_eTdcBKYNohHdXvnvcke7U28'
"""

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
log_file_name = str(firstTimeNow.strftime('%m.%d') + '..' + str(random.randint(1,100)) + '.txt')

if os.path.isfile(log_file_name):
    print('Found the file')
else:
    invested_file = open(log_file_name, 'w+')
upvote_threshold = 650

# Functions #
def log(stringInput):
    timeNow = datetime.datetime.now()
    message = str(bot.user.me()) + ': ' + str(stringInput) + '\n' + str(timeNow.strftime('%m-%d %H:%M:%S'))
    print(message)
    with open(log_file_name, 'a') as l:
        l.write(message + '\n\n')

# TODO refine the comment function and get it where you can both comment for portfolio and buy with less code #
def comment(interested_submission_post_id, contents):
    commenting_submission = bot.submission(interested_submission_post_id)
    for wanted_comment in commenting_submission.comments():
        if wanted_comment.author == 'MemeInvestor_bot':
            try:
                wanted_comment.reply(contents)
            except praw.exceptions.APIException:
                print('Got the rate limit, exiting now...')
                exit()
    
subreddit = bot.subreddit('MemeEconomy')
percentage_of_balance_invested = .75
# Search #
# Portfolio message #
for submission in subreddit.hot(limit=2):
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
balance = float(split_current_balance_message[12].replace('**', ''))

# Search #
investment_boolean = False
while not investment_boolean:
    log('Searching...')
    for searching_submission in subreddit.hot(limit=15):
        # Variables #
        upvotes_on_post = searching_submission.score
        flair = searching_submission.link_flair_text

        submission_created_formatted = searching_submission.created_utc
        submission_time = datetime.datetime.utcfromtimestamp(submission_created_formatted)
        age = (datetime.datetime.now() - submission_time)
        time_boolean_sixty = age < datetime.timedelta(minutes=60)
        # If the post is less than an hour old and has x number of upvotes, THEN extract the price #
        if time_boolean_sixty and upvotes_on_post > 500:
            # Extract the price of the post #
            if any(char.isdigit() for char in flair):
                log('Bot has found a post!')
                interested_submission = searching_submission
                extractedFlair = flair.replace("M¢", '')
                global price
                price = round(float(extractedFlair))
                log('It had ' + str(upvotes_on_post) + ' upvotes on the post and the price was ' + str(price) +
                    ' memecoins.')
                # Calculate the number of shares that we want #
                amount = (balance / price) * .25
                invest_message = "!buy " + str(amount)
                # Invest #
                comment(interested_submission, invest_message)
                investment_boolean = True
            else:
                continue
    log('Sleeping for 5 minutes and going again')
    time.sleep(300)


