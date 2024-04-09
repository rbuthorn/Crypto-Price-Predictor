import argparse
import praw
from datetime import datetime

class RedditDataCollector:
    #this class can handle returning historical data about a specific coin from "start" to "end" dates, 
    def __init__(self, coin_name, historical, subreddit_name, start, end):
        self.coin_name, self.historical, self.subreddit_name, self.start, self.end = coin_name, historical, subreddit_name, start, end
        self.reddit_api_secret, self.reddit_password = self.get_secrets()
        self.reddit = self.init_reddit()
        self.CryptoCurrency_sub, self.CryptoMarkets_sub, self.CryptoMoonShots_sub = self.init_general_subreddits()
        self.subreddit = self.init_specific_subreddit()

    def get_secrets(self):
        with open("../secrets/reddit_api_secret.txt", 'r') as ras, open("../secrets/reddit_password.txt", 'r') as rp:
            return ras.read(), rp.read()

    def init_reddit(self):
        reddit = praw.Reddit(
          check_for_async = False,
          client_id = 'Gh-hxk1LwuTnCS0nDyGtQA',
          client_secret = self.reddit_api_secret,
          user_agent = 'MyBot/0.0.1',
          username = 'Weird-History8104',
          password = self.reddit_password
        )
        return reddit

    def init_general_subreddits(self):
        CryptoCurrency_sub = self.reddit.subreddit("CryptoCurrency")
        CryptoMarkets_sub = self.reddit.subreddit("CryptoMarkets")
        CryptoMoonShots_sub = self.reddit.subreddit("CryptoMoonShots")
        return CryptoCurrency_sub, CryptoMarkets_sub, CryptoMoonShots_sub

    def init_specific_subreddit(self):
        return self.reddit.subreddit(f"{self.subreddit_name}")

    def test_subreddit_query(self):
        for submission in self.CryptoCurrency_sub.hot(limit=3):
            print(submission.title)


def main(args):
    check_args(args)
    coin_name = args.arg1
    historical = args.arg2
    subreddit_name = args.arg3
    start = args.arg4
    end = args.arg5
    DataCollector = RedditDataCollector(coin_name, historical, subreddit_name, start, end)
    DataCollector.test_subreddit_query()

def check_args(args):
    #exits and provides explanation if incorrect arg(s)
    return

if __name__ == "__main__":

    #can be called from another file inside a for loop to provide/store data for multiple different cryptocurrencies
    parser = argparse.ArgumentParser(description='data collection from reddit')
    parser.add_argument('-c', '--arg1', type=str, help='name of cryptocurrency')
    parser.add_argument('-HL', '--arg2', type=str, help='query historical data(H) or live data(L)?')
    parser.add_argument('-sr', '--arg3', type=str, help='name of subreddit("none" if none exists)')
    parser.add_argument('-s', '--arg4', type=str, help='collect data from start datetime(YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('-e', '--arg5', type=str, help='collect data from end datetime(YYYY-MM-DD HH:MM:SS)')

    # parse arguments and add them to args variable
    args = parser.parse_args()
    main(args)