# April 22: reading and writing files

In this exercise, we will read a file and print some output. Then, we'll write a new file by modifying that input. 

**Context:** the file we will be working with, `ex1.txt`, has names and scores (from 1 to 10) of a test. Anyone with a test score less than 3 has failed the test (sad). Your objective will be to:

1. Read the text file using Python scripts.
2. Having read the file, define who passed and who failed the test.
3. Write a new text file with a new column that says whether that person has failed (`fail`) or passed (`pass`) the test.

At the end of this excercise, you should have produced 3 new files:

- `Notebook.ipynb`, a notebook where you'll work on your results.
- `utils.py`, a Python script that has the functions necessary to do the work.
- `ex2.txt`, the output from that contains the same as `ex1.txt` but with an extra column indicating whether a student pass or failed.

## Part 1: reading the file

Let's first read this file using Python's core library `open`. To this end:

1. Create a Python notebook `Notebook.ipynb` (e.g., `jupyter notebook` -> then click on "New", call this notebook "Notebook").
2. Create a cell.
3. Now you can open the file by doing `myfile = open('ex1.txt','r')`.

The new object you've created following the above, `myfile`, has many attributes. The most fun is the `readline()` which you can try yourself:

4. Create a new cell.
5. Write "myfile.readline()".

The output should be something like `'carlos;6\n'`. Turns out this is the very first line of the file `ex1.txt`! If you run the cell once again, it should print the next line and so one. This is what `readline()` does --- it reads one line at a time.

You can keep doing this and eventually the returned string will be simply `''`. That means you've reached the end of the file.


**Task 1:** create a loop (my recommendation is a `while` loop) that reads each line with the technique described above, and saves each line into a python `list` called `output`. In other words, your final list, `output` should print:

```
In [13]: output
Out[13]: ['carlos;6\n', 'rene;9\n', 'juan;1\n', 'diego;2\n', 'romina;5\n']
```

**Hint 1:** your code should exit the `while` loop when the line that is read is `''`. In other words, something like

```
    line = myfile.readline()
    if line == '':
        break
```
should help you get out of the loop.

**Task 2:** once you complete the loop, add a line at the end of your code that closes the file as follows: `myfile.close()`.

## Part 2: writing a file

Congratulations! You now know how to read files. We will now go through the outputs of the file and create a new file with the results of whether the students passed or failed their tests.

With your new list, `output[0]` should give you as output `'carlos;6\n'`. This obviously has the name first, the score after the `;` and then a pesky `\n` at the end. The `\n` at the end is the way the string is telling us there is a "jump of a line" in the text file. The `;` in the string on the other hand is the "delimiter" of the string --- is telling us what separates columns in the format of the file (sometimes this is commas, sometimes this is blank space).

There's a handy function called `split` that allows you to separate information from a given string. To learn how to use it, suppose we have the string `s = 'a,b,c,d'`. If you then do `s.split(',')`, the output will be `['a', 'b', 'c', 'd']` (try it!).

**Task 2:** using the `split` functionality of strings, do a for loop over the `output` list, and save the name of each person in a list `names` and the score of each person in a list called `scores`.
