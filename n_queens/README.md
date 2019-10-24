# N-Queens-Problem
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. 
For example, following is a solution for 4 Queen problem.

The expected output is a binary matrix which has 1s for the blocks where queens are placed. For example, following is the output matrix for above 4 queen solution.

              { 0,  1,  0,  0}
              { 0,  0,  0,  1}
              { 1,  0,  0,  0}
              { 0,  0,  1,  0}


# Algorithms
In order to (efficiently) solve this problem the following 3 algorithms were used and compared:

* Simulated Annealing (SA)
* Min-Conflicts (MC)
* Hill climbing (HC) 

The results for the 16x16 problem can be found in the [results](result.txt) file.
       
#### Requirements:
* Python 3.6
* Numpy

Simply run runner.py without args for a small demo of a 8x8 board for each algorithm.


# Running the script

By default simply running the runner.py will execute the 3 algorithms for the N-Queen problem (N=16).

        python runner.py
        
For a full input arg list type (check the beginning of runner.py for more):
        
        python runner.py -h
