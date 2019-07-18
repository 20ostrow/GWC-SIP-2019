'''
In this program, we print out all the text data from our twitter JSON file.

Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)

#print(tweetData[0])
#print(list(tweetData[0].keys()))

# tweetsWithRetweets = []
# total = 0
# for i in range(len(tweetData)):
#     if "retweet_count" in list(tweetData[i].keys()):
#         total += tweetData[i]["retweet_count"]
#         tweetsWithRetweets.append(tweetData[i]["retweet_count"])
#     else:
#         total += 0
# avg = total/len(tweetsWithRetweets)
# print(f"The average number of retweets is {avg}")
#
# ##################################
#
# tweetsWithFavorites = []
#
# sum = 0
# for i in range(len(tweetData)):
#     if "favorite_count" in list(tweetData[i].keys()):
#         sum += tweetData[i]["favorite_count"]
#         tweetsWithFavorites.append(tweetData[i]["favorite_count"])
#     elif "favourites_count" in list(tweetData[i].keys()):
#         sum += tweetData[i]["favourites_count"]
#         tweetsWithFavorites.append(tweetData[i]["favourites_count"])
#     else:
#         sum += 0
# average = sum/len(tweetsWithFavorites)
# print(f"The average number of favorites is {average}")
#
# # print(tweetData[0]["text"])
#
# ###################################
allTweets = []

for i in range(len(tweetData)):
    tempTweet = tweetData[i]["text"]
    allTweets.append(tempTweet)
# print(allTweets)
# print(allTweets[0])

###################################
polarityList = []
for item in allTweets:
    blob1 = TextBlob(item)
    polar1 = blob1.polarity
    polarityList.append(polar1)
#print(polarityList)

###################################
fullTweetList = []
for x in range(len(tweetData)):
    tempDictionary = {}
    tempDictionary["ID"] = tweetData[x]["id"]
    tempDictionary["tweet"] = allTweets[x]
    tempDictionary["polarity"] = polarityList[x]
    fullTweetList.append(tempDictionary)

#####################################
tweetString = ""
for tweet in allTweets:
    tweet += " "
    tweetString += tweet
#print(tweetString)

#####################################
wordcloud = WordCloud().generate(tweetString)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig("tweetchart.png")

# numA = 0
#
# for i in range(len(allTweets)):
#     characters = allTweets[i].list()
#     if "a" in characters:
#         numA += 1
#     elif "A" in characters:
#         numA += 1
#     else:
#         numA += 0
# print(f"The number of a's in all the tweets is {numA}")

#
# # We can close the file now that we have locally stored the data.
# tweetFile.close()
#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
