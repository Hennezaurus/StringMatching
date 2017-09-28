# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:00:42 2017

@author: Matthew
"""
import unittest, time

#------------------------------------------------------------------------------
#                       Brute Force Implementation
#------------------------------------------------------------------------------

def BruteForceStringMatch(T, P):
    '''
    Implements brute-force string matching
    Inputs:
        @T:
            An array of characters representing some text 
        @P:
            An array of characters representing a pattern to search for
            within the text
    Output:
        @return: *Index, time taken, number of basic operations performed
            *The index of the first character in the text that starts
            a matching substring, or -1 if the search is unsuccessful
    '''
    # So we can use exact algorithm terminology
    n = len(T)
    m = len(P)
    
    # Take note of start time, and begin basic operation counter
    start = time.time()
    bo_count = 0
    
    # Loop through entire text up to 'm' characters from the end
    for i in range(n-m):
        
        bo_count += 1 # Every for loop
        
        # Check to see if we're still matching the pattern
        j = 0
        while(j < m and P[j] == T[i + j]):
            bo_count += 1 # Every inner loop
            j += 1
        # If we matched the pattern for the length of the pattern
        # number of times, then we found it, return i
        if j == m: return(i, time.time() - start, bo_count)

        
    # Pattern was not found, so return -1
    return(-1, time.time() - start, bo_count)


#------------------------------------------------------------------------------
#                        Brute Force Unit Tests
#------------------------------------------------------------------------------

class TestBruteForce(unittest.TestCase):

    # Simple test to find correct index    
    def test_brute_find(self):
        text    = 'text to search for pattern in'
        pattern = 'pattern'
        
        found_index, time, bo = BruteForceStringMatch(text, pattern)        
        self.assertEqual(found_index, 19)
    
    # Test to return -1 when not found
    def test_brute_not_find(self):
        text    = 'testtesttesttesttest'
        pattern = 'nope'
        
        found_index, time, bo = BruteForceStringMatch(text, pattern)
        self.assertEqual(found_index, -1)
    
    
    # Test cases where the pattern is longer than the text
    def test_brute_pattern_longer(self):
        text    = 'short'
        pattern = 'longerthantext'
        
        found_index, time, bo = BruteForceStringMatch(text, pattern)
        self.assertEqual(found_index, -1)
        
        
    # Test cases where the entered pattern is empty
    def test_brute_pattern_empty(self):
        text    = 'texttosearchwithin'
        pattern = ''
        
        found_index, time, bo = BruteForceStringMatch(text, pattern)
        self.assertEqual(found_index, -1)

        
    # Test cases where the entered text is empty
    def test_brute_text_empty(self):
        text    = ''
        pattern = 'test'
        
        found_index, time, bo = BruteForceStringMatch(text, pattern)
        self.assertEqual(found_index, -1)



#------------------------------------------------------------------------------
#                   Horsepool Matching Implementation
#------------------------------------------------------------------------------


def HorspoolMatching(P, T):
    '''
    Implements Horspool's algorithm for string matching
    Inputs:
        @P:
            Pattern to find
        @T:
            Text to search in
    Output:
        @return:
            The index of the left end of the first matching sub-string
            or -1 if there are no matches
    '''
    # So we can use exact algorithm terminology
    m = len(P)
    n = len(T)
    
    # Prepare start time and basic operation counter
    start = time.time()
    bo_count = 0
    
    # Generate table of shifts
    table = ShiftTable(P)
    
    # Initialize search location
    i = m - 1
    
    # Loop while still text to search
    while(i <= n-1):
        k = 0       # Number of matched characters
        
        bo_count += 1
        
        # While we haven't finished matching all pattern length elements
        #    and our current pattern element matches the text element
        while(k <= m-1 and P[m-1-k] == T[i-k]):
            bo_count += 1
            k += 1
        # Once we've bailed out of this loop, either we matched all elements...
        if(k == m):
            return(i-m+1, time.time() - start, bo_count)
        # Or we bailed out because the pattern no longer matched...
        else:
            # Shift pattern along by the shift table value of where this
            #     pattern matching began
            i += table[T[i]]
    
    # If we run the full while loop and got to the end of the text
    #   withing a match, then return -1
    return(-1, time.time() - start, bo_count)


def ShiftTable(P):
    '''
    Fills the shift table used by Horspool's and Boyer-Moore algorithms
    Input:
        @P:
            The pattern to search for
    Output:
        @return:
            Table indexed by the alphabet's characters and
            filled with shift sizes computed by formula (7.1)
    '''
    # So we can use exact algorithm terminology
    m = len(P)
    
    # Initialize all letters in dictionary with m
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    Table = {}
    for letter in alphabet:
        Table[letter] = m
    
    # Loop through each character in the pattern
    for j in range(len(P) - 1):
        # Set value to our given formula
        Table[P[j]] = m - 1 - j
    
    # Return shift table
    return(Table)


#------------------------------------------------------------------------------
#                    Horspool Matching Unit Tests
#------------------------------------------------------------------------------


class TestHorspool(unittest.TestCase):

    # Simple test to find correct index    
    def test_hors_find(self):
        text    = 'text to search for pattern in'
        pattern = 'pattern'
        
        found_index, time, bo = HorspoolMatching(pattern, text)        
        self.assertEqual(found_index, 19)
    
    # Test to return -1 when not found
    def test_hors_not_find(self):
        text    = 'testtesttesttesttest'
        pattern = 'nope'
        
        found_index, time, bo = HorspoolMatching(pattern, text)
        self.assertEqual(found_index, -1)
    
    
    # Test cases where the pattern is longer than the text
    def test_hors_pattern_longer(self):
        text    = 'short'
        pattern = 'longerthantext'
        
        found_index, time, bo = HorspoolMatching(pattern, text)
        self.assertEqual(found_index, -1)
        
        
    # Test cases where the entered pattern is empty
    def test_hors_pattern_empty(self):
        text    = 'texttosearchwithin'
        pattern = ''
        
        found_index, time, bo = HorspoolMatching(pattern, text)
        self.assertEqual(found_index, -1)

        
    # Test cases where the entered text is empty
    def test_hors_text_empty(self):
        text    = ''
        pattern = 'test'
        
        found_index, time, bo = HorspoolMatching(pattern, text)
        self.assertEqual(found_index, -1)
        
        
#------------------------------------------------------------------------------
#                               Run Tests
#------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()