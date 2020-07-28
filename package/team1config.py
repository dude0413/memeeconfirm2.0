import praw
# Team 1 #
# SMEB is CEO, memeslavebot1 is exe, and rest are floor traders #
# There are 8 members in this firm #

FT1_username = 'memeslavebot1'
FT1_password = "c495Ju+X/c`J&ec'"
FT1_client_id = 'nN7Nj_g_BfETQg'
FT1_client_secret = 'NO9iW94p8FZY8mu4HsKAjT1sRnI'

FT2_username = 'memeslavebot2'
FT2_password = '8,YQ"wk=NrE;3m$g'
FT2_client_id = '-DIZzDTzT9Sd4g'
FT2_client_secret = 'n8bUZCazGp4wGSFuyEgMtcfPLO8'

FT3_username = 'memeslavebot3'
FT3_password = '([RS4kP&z)qEbdp&'
FT3_client_id = '6sLVA6CKfW87VA'
FT3_client_secret = 'y9VPqi63gIkwU3kusYoZVAPnOAo'

FT4_username = 'memeslavebot4'
FT4_password = 's3WaF=dg(_)fr.Ev'
FT4_client_id = 'jjkoDkh1wRQnnw'
FT4_client_secret = 'qORfWohGFTLfj7AZNKlivvC0E30'

FT5_username = 'memeslavebot5'
FT5_password = "D-Kt)t9D}q'haLrx"
FT5_client_id = '_rdRFO3yYV1MAA'
FT5_client_secret = 'IJLcjDHJ8-ddI9T8P9EquISRexw'

FT6_username = 'memeslavebot6'
FT6_password = 'GB855dKbv:7n"`x'
FT6_client_id = 'USYb29LGOPIC8g'
FT6_client_secret = 'jpKb_rUxcPZ2VPvUrd8hlYU6kCs'

FT10_username = 'memeslavebot7'
FT10_password = 'P9aaSAuJ02hD+Ra'
FT10_client_id = '4xZ4SYtddAj5vg'
FT10_client_secret = 'zD6C7p41IZlI_UaI1fm42aHEs0M'

SMEB_username = 'SkynetMemeEconBot2'
SMEB_password = 'huft9hach*SHUR.chum'
SMEB_client_id = 'AinhuT7sX1OoXw'
SMEB_client_secret = '4m_6E_LuWi9hPgXkiTSDF9DfAV0'


FT1 = praw.Reddit(user_agent="Memeslave1",
                      client_id=FT1_client_id,
                      client_secret=FT1_client_secret,
                      username=FT1_username,
                      password=FT1_password)

FT2= praw.Reddit(user_agent="Memeslave2",
                 client_id=FT2_client_id,
                 client_secret=FT2_client_secret,
                 username=FT2_username,
                 password=FT2_password)

FT3= praw.Reddit(user_agent="Memeslave3",
                 client_id=FT3_client_id,
                 client_secret=FT3_client_secret,
                 username=FT3_username,
                 password=FT3_password)

FT4= praw.Reddit(user_agent="Memeslave4",
                 client_id=FT4_client_id,
                 client_secret=FT4_client_secret,
                 username=FT4_username,
                 password=FT4_password)

FT5= praw.Reddit(user_agent="Memeslave5",
                 client_id=FT5_client_id,
                 client_secret=FT5_client_secret,
                 username=FT5_username,
                 password=FT5_password)

FT6= praw.Reddit(user_agent="Memeslave9",
                 client_id=FT6_client_id,
                 client_secret=FT6_client_secret,
                 username=FT6_username,
                 password=FT6_password)

FT7= praw.Reddit(user_agent="Memeslave10",
                  client_id=FT10_client_id,
                  client_secret=FT10_client_secret,
                  username=FT10_username,
                  password=FT10_password)

SMEB= praw.Reddit(user_agent="Apart of the Robotic Overlords Econ",
                 client_id=SMEB_client_id,
                 client_secret=SMEB_client_secret,
                 username=SMEB_username,
                 password=SMEB_password)

team_1_bot_list = [FT1, FT2, FT4, FT5, FT6, SMEB, FT3, FT7]