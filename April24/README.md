# April 24: Github & regular expressions (RegEx).

In this set of exercises, you will practice doing commits, forking repositories and performing pull requests via Github. In addition, you will learn to use the `re` (regular expressions) library to deal with complex tasks involving files and strings.

## Part 1: Github commits, forks and Pull Requests (PR)

**Context:** As you are starting to see, you are creating several files for each folder. If this were a collaborative project, you would like to update your results and "submit" those to the original repository (i.e., in `https://github.com/nespinoza/spring-coding-camp-2025`). In this exercise, you will do exactly that via GitHub. To do this, you will:

1. Fork the repository via GitHub.
2. Clone **your** fork of the repository.
3. `add` the new files you've created, create a `commit` message and then `push` them to **your** fork of the repository.
4. Create a Pull Request (PR) from **your** fork of the repository to the original repository.

Let's do this next.

**Task 1:** create a fork of the original repository (`https://github.com/nespinoza/spring-coding-camp-2025`) in your Github repositories. To this end, login to your Github account and then go to the original repository (`https://github.com/nespinoza/spring-coding-camp-2025`) and click "Fork" (on the top, righthand side). This should create a "copy" of the repository in your own repositories.

**Task 2:** *clone* the repository in your account to your computer somewhere in your computer. To this end, open a Terminal in the folder where you want to clone this (make this different to where you have been working so far) and do `git clone [website to your repository]`. It should be something like `git clone https://github.com/mpmarti/spring-coding-camp-2025`.

**Task 3:** *add* the files you have been working so far into this newly cloned repository. Note this repository is linked directly to your repository, while the one you cloned a few days back is not really linked to anything (in practice is cloned to `nespinoza`'s repository, but you don't have write permissions to that repository). To this end, first copy the files. Then, in a terminal, write `git add yourfile.txt` for all your files (or do `git add *` to "add" all the files). This will "register" them within `git`. Then, write `git commit -m "added files"`. Finally, do `git push`. This should "push" the files to *your* repository.

**Task 4:** create a Pull Request (PR) from your forked repository (in `mpmarti`) to the original repository (in `nespinoza`). To this end, go to the original respository (in `nespinoza`) and click on "Pull requests" on the top. Then, click on "New pull request", and make sure the order of the submission is correct. Then, submit the PR.
