import praw, time, os, datetime

MEB_username = 'memeeconbot'
MEB_password = 'SPIB5poch!fich2noff'
MEB_client_id = '3CMfiAi1cCxq5A'
MEB_client_secret = '1jK_eTdcBKYNohHdXvnvcke7U28'

bot = praw.Reddit(user_agent="Meme Economy Bot Trying to Win using Algorithms",
                  client_id=MEB_client_id,
                  client_secret=MEB_client_secret,
                  username=MEB_username,
                  password=MEB_password)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


subreddit = bot.subreddit("MemeEconomy")
watch_list = []
while True:
    # Search mode #
    # Find posts that we would be interested in investing in and create a file for them #
    for submission in subreddit.hot(limit=15):
        # Variables #
        upvotes_on_post = submission.score
        flair = submission.link_flair_text
        submission_id = submission.id
        submission_created_formatted = submission.created_utc
        submission_time = datetime.datetime.utcfromtimestamp(submission_created_formatted)
        age = (datetime.datetime.now() - submission_time)
        time_boolean_sixty = age < datetime.timedelta(minutes=60)
        time_boolean_fifteen = age < datetime.timedelta(minutes=15)
        # If its less than an hour old / has more than 400 upvotes; If its less than 15 minutes old and has >75 upvotes
        # poggers #
        if (time_boolean_sixty and upvotes_on_post > 600) or (time_boolean_fifteen and upvotes_on_post > 90):
            print("Found a post that fit the requirements")
            # if we haven't seen this submission before, create a file for it #
            if submission_id not in watch_list:
                watch_list.append(submission_id)
                new_file_name = str(submission_id + 'data.txt')
                f = open(new_file_name, 'a')
            # If we have seen this submission before, continue on to writing the data #
    # Diagnostics Mode #
    # Just writing down the data from the relevant posts that we have found that (kinda) would've invested in
    # initially #
    for post in watch_list:
        per_cycle_file_name = str(post + 'data.txt')
        per_cycle_submission = bot.submission(post)
        per_cycle_upvotes = per_cycle_submission.score
        per_cycle_flair = str(per_cycle_submission.link_flair_text)

        if hasNumbers(per_cycle_flair):
            extractedFlair = per_cycle_flair.replace("M¢", '')
            price = round(float(extractedFlair))
            upvotes = int(per_cycle_submission.score)
            both_data = str(price) + ',' + str(upvotes)
        with open(per_cycle_file_name, "a") as c:
            c.write(both_data + '\n')

    # Wait 15 minutes and go agane #
    print('Completed a cycle. Sleeping for 15 minutes')
    time.sleep(900)
