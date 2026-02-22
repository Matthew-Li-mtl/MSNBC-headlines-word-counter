# MSNBC-headlines-word-counter
Scrapes ms.now and counts the repeats of words in across all headlines on the front page in a useable format for word clouds. Can be run multiple times and stores the aggregate word data across all scrapes, with some customization. 

# Usage
Getting the word data happens in two steps:
1) Scraping ms.now
2) Running word_data.py to process the scraped data

To scrape, set up a virtual environment then use this in the terminal:
```
scrapy crawl msnbc -O msnbc.json
```

Then run word_data.py as a standalone Python file.

# Output
word_data.py will create two types of files:
 - Word count json
 - Raw word repeat txt

Word count files store each unique word and their repetitions.
Raw word repeat files simply sort the words by their frequency. These can be pasted into word cloud generators as raw data.

The data from the most recent scrape will be stored as these two files in msnbc/msnbc/word_data/output

The data will also be appended to the aggregate files in /msnbc/msnbc/word_data/output, and maintain their formatting.

## Aggregates

Aggregate output files store data from multiple scrapes. Simply repeat the two step process at the top with RESET_AGGREGATES=False in word_data.py.

To reset the aggregates (such that they only contain the most recent scrape of data), set RESET_AGGREGATES=True in word_data.py then run word_data.py.

Run save_aggregates.py to a copy of the aggregate files with a timestamp.

You may also toggle WRITE_TO_AGGREGATES in word_data.py to store the data from the most recent scrape without appending it to the aggregate data.

## Word clouds

Again, any aggregate or non-aggregate "raw_word_repeat" text file is formatted for use with word clouds. Cheers.

