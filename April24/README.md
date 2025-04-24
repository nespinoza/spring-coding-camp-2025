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

## Part 2: regular expressions

**Context:** when exploring files and extracting information from there, one is typically interested in extracting data using certain patterns. For instance, you might want to extract e-mail addresses from a file or a webpage, but the email addresses are embedded in the file with other strings making it hard to extract. Or you might want to extract information from a table online in an automatic fashion. This is where the `re` library comes handy. Here, we learn to use it and try it on some made-up and _real_ data.

**Task 1:** the file `ex1.txt` has a series of e-mails embedded into it. Read the tutorials [here][https://realpython.com/regex-python/] and [here][https://developers.google.com/edu/python/regular-expressions] to learn to use the `re` library, and use it to write a function that writes a file with a list of the e-mails found in the `ex1.txt` file.

**Hint 1:** the resulting file should read:

```
myname@stsci.edu
name-espin@gmail.com
my.name@gmail.com
n.p.a@gmail.com
```

**Task 2:** (a real world problem) The research directory of STScI [here](https://www.stsci.edu/stsci-research/research-directory) has a list of names and contact information of all the staff at STScI. This is, however, embedded in a website. Your objective will be to write a function that outputs a text file with the name of the staff and their e-mails, separated by a `;` (i.e., a CSV file). Note their e-mails are not included in the webpage, but you can get it by simply extracting the value under the "Contact" column (e.g., for Aguilar, Jonathan the "Contact" says `jaguilar` --- the e-mail is then simply `jaguilar@stsci.edu`). To perform this task, you should:

1. In Google Chrome, open the webpage, and go to "View -> Developer -> View Source" to see the source code of this page. Put that in a text file (or download it).
2. Find patterns in this text file with the code of the webpage that might help you extract the information you want. As a hint, note that the e-mails are always followed by a `<br />` code, so you coud use that in your `re` call to extract e-mails.

**Hint 2:** the resulting file should read something like:

```
Aguilar,Jonathan;jaguilar@stsci.edu
Alam, Munazza;malam@stsci.edu
.
.
.
```

**Task 3:** (optional) use the same tricks you learned above to write a text file that extracts all the information for all JWST proposals in [this webpage](https://www.stsci.edu/jwst/science-execution/approved-programs/general-observers/cycle-4-go).

**Hint 3:** the resulting file should read something like:

```
6915;Direct Detection and Characterization of a Nearby Temperate Giant Planet;PI: William Balmer;12;47.3/0.0;MIRI/Coronagraphy NIRCam/Coronagraphy;GO
6932;Bridging the generation gap with TOI-1801 b, a 700 Myr-old temperate sub-Neptune;PI: Rafael Luque Co-PIs:Matthew Nixon;12;47.3/0.0;NIRISS/SOSS NIRSpec/BOTS;GO
.
.
.
```
