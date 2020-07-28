import praw
# Team 2 #
# dude0413 is CEO, John is exe, rest are floor traders #
# There are 6 members in this firm #

JDR_username = 'JohnDRockefellerbot'
JDR_password = '$KiNny B0i0413^^'
JDR_client_id = 'H_SkoYJpdXQhDQ'
JDR_client_secret = 'CyuWf4YhA5c2dkxc5EfPP4nDFJ0'

JDR = praw.Reddit(user_agent='testing',
                      client_id=JDR_client_id,
                      client_secret=JDR_client_secret,
                      username=JDR_username,
                      password=JDR_password)


SoT_username = 'SoTInfoBot'
SoT_password = 'MitcheLL02$'
SoT_client_id = 'ER8pNT2MtJ_jmw'
SoT_client_secret = '5qqZkF-4OaKX5-Qnowy41rdKvCI'

SoT = praw.Reddit(user_agent="Apart of the Robotic Overloads Econ",
                 client_id=SoT_client_id,
                 client_secret=SoT_client_secret,
                 username=SoT_username,
                 password=SoT_password)


MEB_username = 'memeeconbot'
MEB_password = 'SPIB5poch!fich2noff'
MEB_client_id = '3CMfiAi1cCxq5A'
MEB_client_secret = '1jK_eTdcBKYNohHdXvnvcke7U28'

MEB = praw.Reddit(user_agent="Meme Economy Bot Trying to Win using Algorithms",
                 client_id=MEB_client_id,
                 client_secret=MEB_client_secret,
                 username=MEB_username,
                 password=MEB_password)


WB_username = 'WarrenBuffettbot'
WB_password = 'Xk9]4}8=621193l'
WB_client_id = 'XxeFevB3h0KK8g'
WB_client_secret = 'NL8by0U2trb9O5IUMIrD4MMlUY4'

WB = praw.Reddit(user_agent='WarrenBuffetBot',
                     client_id=WB_client_id,
                     client_secret=WB_client_secret,
                     username=WB_username,
                     password=WB_password)

my_username = 'dude0413'
my_password = 'krul*aill6golt1MUNT'
my_client_id = 'QgB5EYqXC1UaZQ'
my_client_secret = 'XBNJ7ISvCANsOXCNjtCyvA1z_Fs'

dude = praw.Reddit(user_agent='Mitchell Durbin bot',
                  username=my_username,
                  password=my_password,
                  client_id=my_client_id,
                  client_secret=my_client_secret)

LD_username = "LucidDreaming_bot"
LD_password = "MitcheLL02$"
LD_client_id = "QgB5EYqXC1UaZQ"
LD_client_secret = "XBNJ7ISvCANsOXCNjtCyvA1z_Fs"

LD = praw.Reddit(user_agent='Lucid Dreaming Bot',
                  username=LD_username,
                  password=LD_password,
                  client_id=LD_client_id,
                  client_secret=LD_client_secret)

team_2_bot_list = [dude, WB, JDR, LD, SoT, WB, MEB]