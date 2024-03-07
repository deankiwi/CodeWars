# cleanUpAnswers.py

## Description

`cleanUpAnswers.py` is a Python script designed to facilitate coding during programming tests in a single file. Once a coding task is completed (marked with the `# done` comment), the script automatically transfers the code to a new file.

## Usage

To use `cleanUpAnswers.py`, follow these steps:

1. Ensure Python is installed on your system.
2. Clone the repository: `git clone https://github.com/deankiwi/CodeWars`
3. Navigate to the script directory: `cd CodeWars`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the script: `python cleanUpAnswers.py`
6. Code in `liveCodingFile.py`, add `# done` to the last line, and save to move the code to a new file.

## Example

Example content of `liveCodingFile.py`:

```python
# leetcode <--Website question is from, will play into folder
# square num <--This will be turned into file name

def solution(a):
    return a**2

# my comment on answer - took me 5mins to solve

# done
```

After saving, `liveCodingFile.py` updates to:

```python
# leetcode
# Name of question
```

A new file is created at `/leetcode/square num.py`:

```python
def solution(a):
    return a**2

# my comment on answer - took me 5mins to solve
```

![using cleanUpAnswers.py GIF](/docs/using_cleanUpAnsers.gif)

## TODO

[ ] - work with other languages
