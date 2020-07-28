import praw, time, os, csv
dude_username = 'dude0413'
dude_password = 'krul*aill6golt1MUNT'
dude_client_id = 'QgB5EYqXC1UaZQ'
dude_client_secret = 'XBNJ7ISvCANsOXCNjtCyvA1z_Fs'
bot = praw.Reddit(user_agent="Meme Economy Bot Trying to Win using Algorithms",
                  client_id=dude_client_id,
                  client_secret=dude_client_secret,
                  username=dude_username,
                  password=dude_password)

invested_file_name = 'currentlyinvestedin.txt'
if os.path.isfile(invested_file_name):
    print('Found the file')
else:
    invested_file = open(invested_file_name, 'w+')

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

while True:
    global both_data
    # Open the current investments and put investments into a list #
    with open(invested_file_name) as r:
        already_invested_investments = r.read().splitlines()
    if len(already_invested_investments) != 0:
        print('I got to the investment part')
        for investment in already_invested_investments:
            submission = bot.submission(investment)
            flair = str(submission.link_flair_text)
            if hasNumbers(flair):
                extractedFlair = flair.replace("M¢", '')
                price = round(float(extractedFlair))
                upvotes = int(submission.score)
                both_data = str(price) + ',' + str(upvotes)
            # Look for price and log into txt file for submission #
            submission_text_file_name = str(investment) + "data.txt"
            if os.path.isfile(submission_text_file_name):
                print('Found ' + str(submission_text_file_name))
            else:
                submission_text_file = open(submission_text_file_name, 'w+')
                print('Creating a new file for ' + str(submission_text_file_name))
            with open(submission_text_file_name, 'a') as I:
                I.write(both_data + '\n')
        # Wait 15 minutes and go agane #
        print('Completed a cycle. Sleeping for 15 minutes')
        time.sleep(900)

    else:
        # Wait 5 minutes and then check to see if the list has any contents #
        print("Didn't find anything in the file, waiting for 5 minutes.")
        time.sleep(300)


