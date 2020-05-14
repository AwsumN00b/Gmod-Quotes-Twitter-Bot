#!/usr/bin/env python3

import time, os, random
import tweepy
import API
import datetime

# magic gay

# Twitter API formalities
auth = tweepy.OAuthHandler(API.consumer_key, API.consumer_secret)

auth.set_access_token(API.access_token, API.access_secret)

api = tweepy.API(auth)

def read_quotes():
    # Import that juicy spreadsheet of gmod quotes

    quotes_dict = {}

    with open("quotes.txt") as fd:
        for line in fd.readlines():
            line = line.split(" - ", 1)

            try:
                if "youtu.be" not in line[1] and "[Original Video Removed]" not in line[1]:
                    line[1] += " [We currently don't have a link to the original video, but you can help us by providing one!]"
                    quotes_dict[line[0]] = line[1].strip()
            except:
                quotes_dict[line[0]] = None

    return quotes_dict

def generate_random_quote(dict):
    # picks a random quote to be tweeted
    return random.choice([key for key in dict])

def quotes_buffer(dict, size=7):
    # as requested by Kamiflage, this will pre-generate some quotes to
    # avoid repeats too close to eachother and see whats coming ahead of time

    print(chr(27) + "[2J") # clears the terminal window for neatness

    buffer = []
    while len(buffer) < size:
        quote = generate_random_quote(dict)
        if quote not in buffer:
            buffer.append(quote)

    return buffer

def send_quote(quote):
    api.update_status(quote)
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(quote)

def source_video(source):
    # Im not a fan of this use of a for loop, but tweepy seems kinda weird about finding the ID of other tweets so itll do
    for status in api.user_timeline():
        last_tweet_id = status.id
        break

    api.update_status(source, in_reply_to_status_id=last_tweet_id, auto_populate_reply_metadata=True)
    print(source)

def send_tweets(list, formatted_quotes):

    for quote in list:
        send_quote(quote)

        if formatted_quotes[quote] != None:
            source_video(formatted_quotes[quote])

        print("\n")

        wait_time = random.randint(21600, 43200)
        print("Next quote in {} hours, {:.0f} minutes".format((wait_time // 3600), (wait_time % 3600) / 60))
        time.sleep(wait_time)

def main():

    # send gmod quotes to twitter until the world explodes
    while True:
        formatted_quotes = read_quotes()

        list = quotes_buffer(formatted_quotes)
        print("Next 7 upcoming quotes are:")
        for item in list:
            print(item)
        print("\n")

        send_tweets(list, formatted_quotes)

if __name__ == "__main__":
    main()
