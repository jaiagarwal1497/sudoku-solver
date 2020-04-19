# Sudoku-Solver

The solver uses backtracking search with the minimum remaining value heuristic for solving the constraint satisfaction problem. 
For each domain value, forward checking is used to reduce variables domains.

The program has to be executed as follows:

---

$ python3 sudoku.py <input string>

---


The mean, standard deviation, min, and max of the runtime over all puzzles in sudokus start.txt are present in the file README.txt.
The modification for using a txt file with unsolved boards is present in the comments. It can be used for solving all the boards in start.txt. The results are generated in the file output.txt, where each line of text represents the finished Sudoku board.
