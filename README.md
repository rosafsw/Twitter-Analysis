# Twitter-Analysis
Here do some basic sentiment analysis based on real time twitter data.

Get Twitter Data
edit the keys and tockens based on twitter application in twitterstream.py
run " python twitterstream.py > output.txt " and wait at least 3 minutes to generate analysis data

Derive the sentiment of each tweet
run "python tweet_sentiment.py AFINN-111.txt output.txt"

Derive the sentiment of new terms
run "python term_sentiment.py AFINN-111.txt output.txt"

Compute Term Frequency
run "python frequency.py output.txt"

Which State is happiest?
run "python happiest_state.py AFINN-111.txt output.txt"

Top ten hash tags
run "python top_ten.py output.txt"

