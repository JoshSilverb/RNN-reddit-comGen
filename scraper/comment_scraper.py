import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='BKGHyWtrrO_tnA', \
                     client_secret='vOEEpMXx1ybgOex1fjZZbcUR_r8', \
                     user_agent='UROP_data_scraper', \
                     username='JoshTheBosz', \
                     password='Joshjosh1212')


comments_dict = { "subreddit":[],\
                "commentBody":[],\
                "score":[],\
                "replyNum":[],\
                "username":[], \
                "karma":[], \
                "accAgeUTC":[], \
                "isUserMod":[], \
                "isUserGold":[]
}

subFreq = {}

# Top 30 Reddit users by comment karma - likely to have had a lot of comments 
# in the same subreddits, making the data a little better
userList = ["TooShiftyForYou", "Poem_for_your_sprog", "-eDgAR-", "poopellar", "dick-nipples", \
            "RamsesThePigeon", "Back2Bach", "PainMatrix", "BunyipPouch", "Rooonaldooo99", \
            "IranianGenius", "Portarossa", "straydog1980", "way_fairer", \
            "Donald_Keyman", "_vargas_", "SrGrafo", "SaintVanilla", "AWildSketchAppeared",\
            "mattreyu", "kingeryck", "StickleyMan", "J4CKR4BB1TSL1MS", "mrsuns10", \
            "Mutt1223", "VictorBlimpmuscle", "toeofcamell", "slakmehl"]

for name in userList:
    user = reddit.redditor(name)
    try:
        for comment in user.comments.new(limit=3):
            try:
                print("ayo this is", user.name)
                # username to ID comments
                comments_dict["username"].append(comment.author)

                # which subreddit
                comments_dict["subreddit"].append(comment.subreddit)

                # actual text
                comments_dict["commentBody"].append(comment.body)

                # other comment metadata
                comments_dict["score"].append(comment.score)
                comment.reply_sort = 'new'
                comment.refresh()
                replies = comment.replies
                comments_dict["replyNum"].append(len(replies))

                # user data to give context
                comments_dict["karma"].append(user.comment_karma)
                comments_dict["accAgeUTC"].append(user.created_utc)
                comments_dict["isUserMod"].append(user.is_mod)
                comments_dict["isUserGold"].append(user.is_gold)

                # update the subreddit frequency in subFreq
                if(str(comment.subreddit) in subFreq):
                    subFreq[str(comment.subreddit)] += 1
                else:
                    subFreq[str(comment.subreddit)] = 1
            except:
                print("Comment has been deleted")
    except:
        print(name, "has been deleted or doesn't exist")


'''
comments_dict_high = {  "subreddit":[],\
                        "commentBody":[],\
                        "score":[],\
                        "replyNum":[],\
                        "username":[], \
                        "karma":[], \
                        "accAgeUTC":[], \
                        "isUserMod":[], \
                        "isUserGold":[]
}
'''
iterFreq = subFreq

for sub in iterFreq:
    if(iterFreq[sub] <= 2):
        counter = 0
        for i in comments_dict["subreddit"]:
            if(i == sub):
                comments_dict["username"].pop(counter)
                comments_dict["subreddit"].pop(counter)
                comments_dict["commentBody"].pop(counter)
                comments_dict["score"].pop(counter)
                comments_dict["replyNum"].pop(counter)
                comments_dict["karma"].pop(counter)
                comments_dict["accAgeUTC"].pop(counter)
                comments_dict["isUserMod"].pop(counter)
                comments_dict["isUserGold"].pop(counter)
                counter+=1
        
y = [sub for sub in subFreq if subFreq[sub] > 2]
z = []
for sub in y:
    z.append(subFreq[sub])

print(y)
print(z)
#print(comments_dict)

#comment_data = pd.DataFrame(comments_dict)

#comment_data.to_csv('reddit_sample_data.csv', index=True) 