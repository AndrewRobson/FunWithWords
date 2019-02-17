# FunWithWords

### Task 1

This task takes a file as input which it will process and return back a dictionary describing how many lines each word appeared inside the file.

### Task 2

This task takes a directory of files and processes them so that when a requested file is given it will return those files back with the duplicate lines across files are removed.


## Running the unit tests

Using the terminal for the following:

Inside Task 1 directory run: 
```sh
$ python -m unittest discover -t ../
```
Inside Task2 directory run: 
``` sh
$ python -m unittest discover -t ../
```
Global package: 
``` sh
$ python -m unittest discover
```

## Todo

- Add more tests
- Intergration tests
- Store common lines in a file or database so data can be built up over time

## Assumptions

- There is always a directory specified
- Users will only input the same file once