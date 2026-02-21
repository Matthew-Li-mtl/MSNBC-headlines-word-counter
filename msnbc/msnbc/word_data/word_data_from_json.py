import os
import sys

import json
import time

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

full_path = "C:\\Users\\ml113\\Matthew\\Scripts\\Web_scraping\\Scrapy\\Scrapy_playwright\\MSNBC\\msnbc\\msnbc\\msnbc.json"

file = open(full_path, encoding="utf-8")
#file_content = file.read()

titles_json = json.load(file)
file.close()

print(f"{os.getcwd()}")

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
        all_words.append(word.lower())

word_count = {}

for word in all_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

words_to_sort = []
count_to_sort = []

for word in word_count:
    words_to_sort.append(word)
    count_to_sort.append(word_count[word])


#bubble sort yay
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



word_count_data = ""

for i in range(len(words_to_sort)):
    word_count_data += words_to_sort[i] + " " + str(count_to_sort[i]) + "\n"



raw_word_repeats = ""
for i in range(len(words_to_sort)):
    for j in range(count_to_sort[i]):
        raw_word_repeats += words_to_sort[i] + " "
    raw_word_repeats += "\n"

# C:\Users\ml113\Matthew\Scripts\Web_scraping\Scrapy\Scrapy_playwright\MSNBC\msnbc\msnbc\additional_scripts

file_name_extension = time.strftime("%H %M %S %b %d %Y") + ".txt"

word_count_data_file_path = "msnbc\\msnbc\\word_data\\output\\word_count\\word_count_data " + file_name_extension
raw_word_repeats_file_path = "msnbc\\msnbc\\word_data\\output\\raw_word_repeats\\raw_word_repeats " + file_name_extension

word_count_data_output_file = open(word_count_data_file_path, "w")
word_count_data_output_file.write(word_count_data)
word_count_data_output_file.close()

raw_word_repeats_output_file = open(raw_word_repeats_file_path, "w")
raw_word_repeats_output_file.write(raw_word_repeats)
raw_word_repeats_output_file.close()

