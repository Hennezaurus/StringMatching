# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:52:08 2017

@author: Matthew
"""

import numpy as np
import random, string, csv
from StringMatching import BruteForceStringMatch, HorspoolMatching


def random_word(text_length, pattern_length, seed=None, num_letters=26):
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Set list of random letters to use
    letters = string.ascii_lowercase
    sub_letters = []
    for i in range(len(letters)):
        if i < num_letters:
            sub_letters.append(letters[i])
    
    # Create and random word of given length using letters
    return(''.join(random.choice(sub_letters) for i in range(text_length)), 
           ''.join(random.choice(sub_letters) for i in range(pattern_length)))
    
    
    
def dump_data_to_csv(path, data):
    '''
    Save recorded data from string_match_data to a given file
    
    @params
        data: List of data to log to csv
        path: File name or file path to save data at
        
    @post
        All data saved in csv format at [path]
    '''
    # Open connection to the file
    with open(path, 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        
        # Column Titles
        w.writerow(['Text Length', 'Pattern Length', 'Letter Limit', 'Search Method',
                    'Seed', 'Time Taken', 'Basic Operation Count', 'Index Found'])

        # Write data file row by row to csv
        for row in data:
            w.writerow(row)


def string_match_data(n, m, letter_limit, iterations, path=None):
    '''
    Generate array holding the csv data for a test
    Inputs:
        @n: Length of text to search in
        @m: Length of pattern to search for
        @iterations: Number of times to re-run the search per method for consistency
    Output:
        @return: A list of search results in the following format:
            
 Text Length  |  Pat Length  | Letter limit |  Method  |   Seed  |  Time  |  Basic Operations  | Found Index
--------------|--------------|--------------|----------|---------|--------|--------------------|--------------
   10 000     |      8       |      7       | Horspool |   72    |  0.002 |         54         |     430
   10 000     |      8       |      7       |  Brute   |   34    |  0.003 |         75         |     -1
    '''
    
    # Create list to populate with data (No array because mixed data types)
    search_results = [None] * (iterations * 2)
    
    # Run Brute Force search [iteration] times using the counter as the random seed
    for i in range(iterations):
        print("Testing seed: " + str(i))
        
        # Generate pseudo random text and pattern
        text, pattern = random_word(n, m, seed = i, num_letters = letter_limit)
        
        # Run search and store results
        index, time, bo_count = BruteForceStringMatch(text, pattern)
        
        # Log full brute force data row
        search_results[2*i] = n, m, letter_limit, 'Brute', i, time, bo_count, index
        
        # Run search using Horspool
        index, time, bo_count = HorspoolMatching(pattern, text)
        
        # Log full horspool data row
        search_results[2*i + 1] = n, m, letter_limit, 'Horspool', i, time, bo_count, index
    
        
    if path is not None:
        # Save data to specified csv
        dump_data_to_csv(path, search_results)
    else:
        # Return array of results
        return(search_results)


#------------------------------------------------------------------------------
#                               Run Tests
#------------------------------------------------------------------------------


if __name__ == '__main__':
    
    iter_count = 10
    string_match_data(n = 1000000, m = 7, letter_limit = 7,
                      iterations = iter_count, path = 'data.csv')
    
    '''
    found = 0
    for w in x:
        if w[6] > -1:
            found += 1
    
    [print(w) for w in x] 
    print("Found pattern in " + str((found/(iter_count*2)) * 100) + "%")
    '''