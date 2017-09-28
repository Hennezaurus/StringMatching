# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:52:08 2017

@author: Matthew
"""

import numpy as np
import random, string
from StringMatching import BruteForceStringMatch, HorspoolMatching


def random_word(text_length, pattern_length, seed=None):
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Set list of random letters to use
    letters = string.ascii_lowercase
    
    # Create and random word of given length using letters
    return(''.join(random.choice(letters) for i in range(text_length)), 
           ''.join(random.choice(letters) for i in range(pattern_length)))


def string_match_data(n, m, iterations):
    '''
    Generate array holding the csv data for a test
    Inputs:
        @n: Length of text to search in
        @m: Length of pattern to search for
        @iterations: Number of times to re-run the search per method for consistency
    Output:
        @return: A list of search results in the following format:
            
 Text Length  |  Pat Length  |  Method  |   Seed  |  Time  |  Basic Operations  | Found Index
--------------|--------------|----------|---------|--------|--------------------|--------------
   10 000     |      8       | Horspool |   72    |  0.002 |         54         |     430
   10 000     |      8       |   Brute  |   34    |  0.003 |         75         |     -1
    '''
    
    # Create list to populate with data (No array because mixed data types)
    search_results = [None] * (iterations * 2)
    print("Testing Brute Force...")
    
    # Run Brute Force search [iteration] times using the counter as the random seed
    for i in range(iterations):
        
        # Generate pseudo random text and pattern
        text, pattern = random_word(n, m, seed = i)
        
        # Run search and store results
        index, time, bo_count = BruteForceStringMatch(text, pattern)
        
        # Log full data row
        search_results[i] = n, m, 'Brute', i, time, bo_count, index
        
    print("Testing Horspool...")
    
    # Run Horspool search [iteration] times using the counter as the random seed
    for i in range(iterations):
        
        # Generate pseudo random text and pattern
        text, pattern = random_word(n, m, seed = i)
        
        # Run search and store results
        index, time, bo_count = HorspoolMatching(pattern, text)
        
        # Log full data row
        search_results[iterations + i] = n, m, 'Horspool', i, time, bo_count, index
            
    # Return array of results
    return(search_results)


#------------------------------------------------------------------------------
#                               Run Tests
#------------------------------------------------------------------------------


if __name__ == '__main__':
    
    iter_count = 200
    x = string_match_data(n = 100000, m = 5, iter_count = 200)
    
    found = 0
    for w in x:
        if w[6] > -1:
            found += 1
    
    #[print(w) for w in x] 
    print("Found pattern in " + str((found/(iter_count*2)) * 100) + "%")