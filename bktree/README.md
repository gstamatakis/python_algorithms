# Description
Shortest path between 2 words using only words from a given dictionary and a BK-Tree implementation
in pure python. 


# Example
The script can be ran with just 3 args (dictionary file followed by the start and target words). 

For example, if we wanted to find the shortest distance between 'life' and 'death' using only the 
words in the word_dict.txt file we could simply:

    python word_morph.py word_dict.txt life death

should print the following
    
    life, lift, left, heft, heat, heath, death

