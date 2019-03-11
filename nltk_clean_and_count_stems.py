#!/usr/bin/python3
#
# nltk_clean_and_count_stems.py - Counting and stemming words ina file
# Author: <Ines Simbi>(inessimbi@bennington.edu)
# Date: <03.03.2019>
#

import re
from nltk.stem import PorterStemmer

file_name = "Wikipedia-LexicalAnalysis.xml"
out_file_name = "lexical_analysis_nltk_stemmed_out.txt"

counting_dict = {} # dictionary to save words
with open(file_name, 'r') as file: # open file
   with open(out_file_name, 'w') as file_output: # writes to file
        text = file.readlines()# read what's in file
        the_stem = PorterStemmer()
        the_list = []
        for line in text:
            line = line.lower()
            line = re.sub("[^a-zA-Z']+", " ", line)
            the_list = the_list + line.split()
        print(the_list)
        for word in the_list:
            stem = the_stem.stem(word) # stem word before counting and putting it in a dictionary
            if stem in counting_dict:
                counting_dict[stem] = counting_dict[stem] + 1
            else:
                counting_dict[stem] = 1
        print(counting_dict)
        the_keys = sorted(counting_dict.keys())
        for key in the_keys:
            the_keys= sorted(counting_dict.keys())
            the_value= counting_dict[key]
            the_string = key + ":" + str(the_value) + "\n"
            file_output.write(the_string) 