#!/usr/bin/python3
#
# clean_and_count_tokens.py - Counting words in a file
# Author: <Ines Simbi>(inessimbi@bennington.edu)
# Date: <03.03.2019>
#

import re


file_name = "Wikipedia-LexicalAnalysis.xml"
out_file_name = "lexical_analysis_out.txt"

# use potter stemmer in each word before count
counting_dict = {}
with open(file_name, 'r') as file: # open file
   with open(out_file_name, 'w') as file_output: # writes to file
        text = file.readlines()# read what's in file
        #print(text)
       # dictionary to save out words
        # #loop to get lines in text
        the_list= []
        for line in text:
            line = line.lower() # Sadip suggested I make everything lowercase to be able to count words
            #print(line)
           # line = re.sub(r'()|()')
            """
            line = re.sub(r'<\w+>', " ", line)
            line = re.sub(r'[<][/]\w+[>]', " ", line)
            line = re.sub(r'[!^_]', " ", line)
            """
            line = re.sub("[^a-zA-Z']+", " ", line)
            #line = re.findall("\w+", line)
            #line = re.sub("'(.+)", " ", line)
            #line = re.sub(" (')+", " ", line)
            the_list = the_list + line.split() #adds lines in a list
        print(the_list)
        for word in the_list:
            if word in counting_dict:
                counting_dict[word] = counting_dict[word] + 1
            else:
                counting_dict[word] = 1
        print(counting_dict)
        the_keys = sorted(counting_dict.keys()) #sorts keys in the dictionary
        for key in the_keys:
            the_value= counting_dict[key]
            the_string = key + ":" + str(the_value) + "\n" #adds key and it's value in string
            #print(the_string)
            file_output.write(the_string) #outputs the string in a file