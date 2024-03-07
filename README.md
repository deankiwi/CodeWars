# cleanUpAnswers.py

## Description
`cleanUpAnswers.py` is a Python script that allows to continually code in a single file then when you are working through programming tests then once completed (using key word comment `# done`) will transfer out do new file


## Usage
To use `cleanUpAnswers.py`, follow these steps:

1. Ensure you have Python installed on your system.
2. clone repository `git clone https://github.com/deankiwi/CodeWars`
3. Open a terminal or command prompt and navigate to the directory containing the script. `cd CodeWars`
4. install dependance `pip install -r requirements.txt`
4. Run the script using the following command: `python cleanUpAnswers.py`
5. code in `liveCodingFile.py` then once completed add `# done` to the last line of your file and save for it to be moved to another file

## Example
Here's an example file `liveCodingFile.py`:
```python
# leetcode <--Website question is from, will play into folder
# square num <--This will be turned into file name

def solution(a):
    return a**2

# my comment on answer - took me 5mins to solve

# done
```
once `liveCodingFile.py` has been saved it will be updated to this
```python
# leetcode
# Name of question
```
a new file would have been created `/leetcode/square num.py`
```python
def solution(a):
    return a**2

# my comment on answer - took me 5mins to solve
```

![using cleanUpAnswers.py GIF](/docs/using_cleanUpAnsers.gif)

## TODO
[ ] - work with other languages 