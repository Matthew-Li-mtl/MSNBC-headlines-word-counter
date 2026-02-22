# Run this file to get your raw_word_repeats, word_count_data, and their aggregates. 
# Use RESET_AGGREGATES to reset the aggregate data to only the most recent scrape. REMEMBER TO UNTOGGLE THIS AFTERWADS!
# Change the scrape_json_path to read a different scrape obviously.
# Change WORDS_NOT_ALLOWED to filter out the words you don't want. You can remove all the meaningless words like "the", but I like to keep them there just for fun.

RESET_AGGREGATES = True
WRITE_TO_AGGREGATES = True
WORDS_NOT_ALLOWED = ["", " "]


import os
import sys

import json
import time

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

scrape_json_path = "msnbc\\msnbc\\msnbc.json"

file = open(scrape_json_path, encoding="utf-8")
#file_content = file.read()

titles_json = json.load(file)
file.close()

print(f"{os.getcwd()}")

word_count_dict = {}
raw_word_repeats_dict = {}

aggregate_word_count_data_file_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\word_count_data_aggregate.txt"
aggregate_raw_word_repeats_file_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\raw_word_repeats_aggregate.txt"

def remove_punctuation(text):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    safe_characters = [" ", "-"]
    
    direct_removal = ["\n", "  ", "   ", "    "] # well well well
        
    for char in direct_removal:
        text.replace(char, "")
    
    newtext = ""
    
    for char in text:
        if char.lower() in alphabet or char in safe_characters:
            newtext += char
    
    return newtext

all_words = []


for title_json in titles_json:
    title = title_json["title"]
    formatted_line = remove_punctuation(title)
    line_words = formatted_line.split(" ")
    for word in line_words:
        if word not in WORDS_NOT_ALLOWED:
            all_words.append(word.lower())


word_count = {}

for word in all_words: # counts the word from the most recent scrape
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

words_to_sort = []
count_to_sort = []

words_to_sort_aggregate = []
count_to_sort_aggregate = []


aggregate_word_count_data = {}

try: # grab the aggregate of all the saved scrapes since the last reset
    aggregate_word_count_data_file = open(aggregate_word_count_data_file_path, "r")
    aggregate_word_count_data = json.loads(aggregate_word_count_data_file.read())
    aggregate_word_count_data_file.close()
except:
    pass

for word in word_count: # add the words from the most recent scrape to the non-aggregate and aggregate datasets
    words_to_sort.append(word)
    count_to_sort.append(word_count[word])
    if WRITE_TO_AGGREGATES:
        if word in aggregate_word_count_data:
            aggregate_word_count_data[word] += word_count[word]
        else:
            aggregate_word_count_data[word] = word_count[word]

for word in aggregate_word_count_data: # once the most recent scrape and the previous aggregate scrapes are combined, we can add them to the lists to be sorted ALL AT ONCE.
    words_to_sort_aggregate.append(word)
    count_to_sort_aggregate.append(aggregate_word_count_data[word])

#bubble sort the lists so that the most frequest words come out on top yay
words_sorted_by_count = False
while not words_sorted_by_count:
    words_sorted_by_count = True
    for i in range(len(count_to_sort) - 1):
        if count_to_sort[i] < count_to_sort[i+1]: #left heavy
            words_sorted_by_count = False
            
            temp_count = count_to_sort[i]
            count_to_sort[i] = count_to_sort[i+1]
            count_to_sort[i+1] = temp_count
            
            temp_word = words_to_sort[i]
            words_to_sort[i] = words_to_sort[i+1]
            words_to_sort[i+1] = temp_word
            
aggregate_words_sorted_by_count = False
while not aggregate_words_sorted_by_count:
    aggregate_words_sorted_by_count = True
    for i in range(len(count_to_sort_aggregate) - 1):
        if count_to_sort_aggregate[i] < count_to_sort_aggregate[i+1]: #left heavy
            aggregate_words_sorted_by_count = False
            
            temp_count = count_to_sort_aggregate[i]
            count_to_sort_aggregate[i] = count_to_sort_aggregate[i+1]
            count_to_sort_aggregate[i+1] = temp_count
            
            temp_word = words_to_sort_aggregate[i]
            words_to_sort_aggregate[i] = words_to_sort_aggregate[i+1]
            words_to_sort_aggregate[i+1] = temp_word
    

aggregate_word_count_data_output = {} # dictionaries preserve insertion order. These dictionaries will be 'sorted' by referring to the sorted lists from above.
word_count_data = {}

for i in range(len(words_to_sort)):
    word_count_data[words_to_sort[i]] = count_to_sort[i]
for i in range(len(words_to_sort_aggregate)):
    aggregate_word_count_data_output[words_to_sort_aggregate[i]] = count_to_sort_aggregate[i]


raw_word_repeats = ""
for i in range(len(words_to_sort)):
    for j in range(count_to_sort[i]):
        raw_word_repeats += words_to_sort[i] + " "
    raw_word_repeats += "\n"
    
raw_word_repeats_aggregate = ""
for i in range(len(words_to_sort_aggregate)):
    for j in range(count_to_sort_aggregate[i]):
        raw_word_repeats_aggregate += words_to_sort_aggregate[i] + " "
    raw_word_repeats_aggregate += "\n"

time_stamp = time.strftime("%Y %b %d %H %M %S")
file_name_extension = time_stamp + ".txt"

word_count_data_file_path = "msnbc\\msnbc\\word_data\\output\\word_count\\word_count_data " + file_name_extension
raw_word_repeats_file_path = "msnbc\\msnbc\\word_data\\output\\raw_word_repeats\\raw_word_repeats " + file_name_extension

#aggregates go first so that in the case of a reset, they get overriden by the data from only the most recent scrape. cheers.



if RESET_AGGREGATES:
    word_count_data_output_file = open(aggregate_word_count_data_file_path, "w")
    word_count_data_output_json = json.dumps(word_count_data)
    word_count_data_output_file.write(word_count_data_output_json)
    word_count_data_output_file.close()

    raw_word_repeats_output_file = open(aggregate_raw_word_repeats_file_path, "w")
    raw_word_repeats_output_file.write(raw_word_repeats)
    raw_word_repeats_output_file.close()
    
elif WRITE_TO_AGGREGATES:
    aggregate_word_count_data_file = open(aggregate_word_count_data_file_path, "w")
    aggregate_word_count_data_output_json = json.dumps(aggregate_word_count_data_output)
    aggregate_word_count_data_file.write(aggregate_word_count_data_output_json)
    aggregate_word_count_data_file.close()

    aggregate_raw_word_repeats_file = open(aggregate_raw_word_repeats_file_path, "w")
    aggregate_raw_word_repeats_file.write(raw_word_repeats_aggregate)
    aggregate_raw_word_repeats_file.close()

word_count_data_output_file = open(word_count_data_file_path, "w")
word_count_data_output_json = json.dumps(word_count_data)
word_count_data_output_file.write(word_count_data_output_json)
word_count_data_output_file.close()

raw_word_repeats_output_file = open(raw_word_repeats_file_path, "w")
raw_word_repeats_output_file.write(raw_word_repeats)
raw_word_repeats_output_file.close()

log_path = "msnbc\\msnbc\\word_data\\output\\log.txt"
log_file = open(log_path, "a")

log = "\n\nword_data.py ran at " + time_stamp
log += "\nRESET_AGGREGATES = " + str(RESET_AGGREGATES)
log += "\nWRTIE_TO_AGGREGATES = " + str(WRITE_TO_AGGREGATES)
log += "\nAppended data for " + str(len(words_to_sort)) + " unique words from most recent scrape."
log += "\nThere are data for " + str(len(words_to_sort_aggregate)) + " unique words in the aggregate."
log += f"\nMost common word from most recent scrape: {words_to_sort[0]} ({count_to_sort[0]})"
log += f"\nMost common word in aggregate: {words_to_sort_aggregate[0]} ({count_to_sort_aggregate[0]})"

log_file.write(log)
log_file.close()

