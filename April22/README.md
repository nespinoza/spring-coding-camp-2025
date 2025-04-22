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
- `ex3.txt`, an identical file to `ex2.txt`, but created with a sigle line of code (see below how to do this magic!).
- `ex4.txt`, an identical file to `ex2.txt` and `ex3.txt`, but created with another sigle line of code (see below how to do this magic!).

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

## Part 2: pre-formatting input

Congratulations! You now know how to read files. We will now go through the outputs of the file and create a new file with the results of whether the students passed or failed their tests.

With your new list, `output[0]` should give you as output `'carlos;6\n'`. This obviously has the name first, the score after the `;` and then a pesky `\n` at the end. The `\n` at the end is the way the string is telling us there is a "jump of a line" in the text file. The `;` in the string on the other hand is the "delimiter" of the string --- is telling us what separates columns in the format of the file (sometimes this is commas, sometimes this is blank space).

There's a handy function called `split` that allows you to separate information from a given string. To learn how to use it, suppose we have the string `s = 'a,b,c,d'`. If you then do `s.split(',')`, the output will be `['a', 'b', 'c', 'd']` (try it!).

**Task 2:** using the `split` functionality of strings, do a for loop over the `output` list, and save the name of each person in a list `names` and the score of each person in a list called `scores`. Make sure the `scores` list has only strings (to this end, you can convert strings to ints by doing `int(yourstring)`).

Your output should look like:

```
In [36]: names
Out[36]: ['carlos', 'rene', 'juan', 'diego', 'romina']

In [37]: scores
Out[37]: [6, 9, 1, 2, 5]
```

## Part 3: writing a file with outputs

Excellent! Now we have names and scores on two lists. The next task will be to write a file with outputs, and in particular decide if each student passed or failed the test. 

To this end, we will use the same `open` function we use at the beggining of this exercise, but with a `w` (write) instead of an `r` (read). In other words, we'll use the fact you can create your own files as follows:

```
yourfile = open('myfile.txt', 'w')
```

To add new lines to this files is very simple, you simply do:
```
yourfile.write('this is the first line! \n')
yourfile.write('this is the second \n')
yourfile.write('this is the third and final line')
```
Note above how we add the `\n` to the end of every line except the last.

And as above, you can also close the file once you've done writing on it by doing `yourfile.close()`. With this new knoweldge:

**Task 3:** Create a new file, `ex2.txt` that writes a file in the very same format as `ex1.txt` (i.e., columns separated by `;`), but that has a third column that says "pass" when a student passed the test (score is greater or equal than 3) or "fail" when a student did not pass the test (i.e., score is less than 3).

## Part 4: writing a callable script

In the above excercise, you've basically created the skeleton for a function that receives a filename `ex1.txt` and then outputs another filename `ex2.txt`. This is the next task --- to create a function that does all of this by a simple call.

**Task 4:** Create a python function `testcheck(input, output)` that takes a filename `input` (in your case `ex1.txt`) and writes a new file with a filename `output` (in the case above `ex2.txt`) which is identical to `ex1.txt` but with an extra column. In other words, write a function that does exactly all of the things you did above. Test your function by running it in a cell, i.e., `testcheck('ex1.txt', 'ex3.txt')` --- `ex3.txt` should be identical to `ex2.txt`.

**Hint:** Remember that to create functions, you do something like:

```
def sum_numbers(x,y):

    print(x+y)
```

The above function returns the sum of numbers (e.g., `sum_numbers(3,4)` returns `7`).

Another beautiful thing about functions is that they can go into their own little text file and you can call them from a Notebook. This is a process called **scripting** and is very useful for Python programmers. In the next task, you will create your first script.

**Task 5:** Create a new file in this same folder called `utils.py`. Inside, copy-paste the function you created in Task 4. Next, call it from your Notebook by creating a cell and writing `import utils`, and then `utils.testcheck('ex1.txt', 'ex4.txt')`. `ex4.txt` should look exactly the same as `ex2.txt` and `ex3.txt`.
