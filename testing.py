import praw, datetime, random, os, time

# Create one bot with memeeconbot and then expand from there #
version = '1.0'

FT1_username = 'memeslavebot1'
FT1_password = "c495Ju+X/c`J&ec'"
FT1_client_id = 'nN7Nj_g_BfETQg'
FT1_client_secret = 'NO9iW94p8FZY8mu4HsKAjT1sRnI'
bot = praw.Reddit(user_agent="Meme Economy Bot Trying to Win using Algorithms",
                  client_id=FT1_client_id,
                  client_secret=FT1_client_secret,
                  username=FT1_username,
                  password=FT1_password)
submission = bot.submission('hzg28t')
upvotes_on_checking_post = submission.score
checking_submission_created_formatted = submission.created_utc
submission_time = datetime.datetime.utcfromtimestamp(checking_submission_created_formatted)
now = datetime.datetime.now(datetime.timezone.utc)

now = time.time()
age = now - submission.created_utc  # in seconds
if age >= 3600:
    print("post is at least an hour old")