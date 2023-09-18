#!/usr/bin/env python3 
import pandas as pd

df = pd.read_csv('IRAhandle_tweets_1.csv')

# Look at the first 10,000 tweets in the file, keep only those in english and do not contain a question mark:
df = df[:10000]
df = df[df['language'] == 'English']
df = df[~df['content'].str.contains('\?')]

# Create a new tsv file containing these tweets:
df.to_csv('trumpMentions.tsv', sep='\t', index=False)

# Add a boolean trump_mention column to the dataframe:
df['trump_mention'] = df['content'].str.contains(r'\bTrump\b|[^a-zA-Z0-9]Trump[^a-zA-Z0-9]', regex=True)

# Update the tsv file with the new column:
df.to_csv('trumpMentions.tsv', sep='\t', index=False)

# Compute the % of tweets that mention Trump :
frac_trumpMentions = round(df['trump_mention'].sum() / len(df) * 100, 3)
print('Percentage of tweets that mention Trump: ' + str(frac_trumpMentions) + '%')

# Create a new tsv file from trumpMentions.tsv containing only the columns tweet_id, publish_date, content, and trump_mention:
dataset = df[['tweet_id', 'publish_date', 'content', 'trump_mention']]
dataset.to_csv('dataset.tsv', sep='\t', index=False)

# Create a tsv file, results.tsv, with headers "result" and "value", and the second line containing the result fro frac_trumpMentions:
with open('results.tsv', 'w') as f:
    f.write('result\tvalue\n')
    f.write('frac_trumpMentions\t' + str(frac_trumpMentions) + '\n')
