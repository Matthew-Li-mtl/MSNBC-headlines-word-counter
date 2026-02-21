# run this to save a copy of the aggregates

import time

aggregate_word_count_data_file_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\word_count_data_aggregate.txt"
aggregate_raw_word_repeats_file_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\raw_word_repeats_aggregate.txt"

time_stamp = time.strftime("%Y %b %d %H %M %S")
file_name_extension = time_stamp + ".txt"

aggregate_word_count_data_file_copy_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\saves\\word_count_data_aggregate_saves\\word_count_data_aggregate" + file_name_extension
aggregate_raw_word_repeats_file_copy_path = "msnbc\\msnbc\\word_data\\output\\aggregates\\saves\\raw_word_repeats_aggregate_saves\\raw_word_repeats_aggregate" + file_name_extension

aggregate_word_count_data_file = open(aggregate_word_count_data_file_path, "r")
aggregate_word_count_data = aggregate_word_count_data_file.read()
aggregate_word_count_data_file.close()

aggregate_word_count_data_file_copy = open(aggregate_word_count_data_file_copy_path, "w")
aggregate_word_count_data_file_copy.write(aggregate_word_count_data)
aggregate_word_count_data_file_copy.close()

aggregate_raw_word_repeats_file = open(aggregate_raw_word_repeats_file_path, "r")
aggregate_raw_word_repeats = aggregate_raw_word_repeats_file.read()
aggregate_raw_word_repeats_file.close()

aggregate_raw_word_repeats_file_copy = open(aggregate_raw_word_repeats_file_copy_path, "w")
aggregate_raw_word_repeats_file_copy.write(aggregate_raw_word_repeats)
aggregate_raw_word_repeats_file_copy.close()

log_path = "msnbc\\msnbc\\word_data\\output\\log.txt"
log_file = open(log_path, "a")

log = "\n\nsave_aggregates.py ran at " + time_stamp

log_file.write(log)
log_file.close()

