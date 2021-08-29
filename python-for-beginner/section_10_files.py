"""
File
input() - accept standard input
print() - write standard output
File are great for storage that lasts beyond the execution of a program

# file seek(position)

# mode and auto close feature
with open(..., mode='a') as my_file:
    pass

"""

import os 
from datetime import datetime

# Utility method to determine the current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
print('dir_path {}'.format(dir_path))

# Read the whole file
notes = open(dir_path + '/documents/section_10/python-notes.txt')
notes_contents = notes.read()
print('Notes contents: \r\n{}'.format(notes_contents))
reread_notes_contents = notes.read()
# Re-read the file or read() twice results in empty string
assert not reread_notes_contents and reread_notes_contents == ''
notes.close()

# File position
"""
read() - returns the entire file.
seek(offset) - change the current position to offset.
seek(0) - go to the beginning of the file.
seek(5) - go to the 5th byte of the file.
tell() - determine the current position in the file
"""
notes_file = open(dir_path + '/documents/section_10/python-notes.txt')
print('Current position: {}'.format(notes_file.tell()))
assert notes_file.tell() == 0
content = notes_file.read()
print(content)

print('Current position: {}'.format(notes_file.tell()))
print(notes_file.read())
assert not notes_file.read()
print('-' * 10)

# Good to know this, just seek back to 0 and read() function works again
notes_file.seek(0)
print('Current position: {}'.format(notes_file.tell()))
print(notes_file.read())
print('File closed? {}'.format(notes_file.closed))
if not notes_file.closed:
    notes_file.close()
print('File closed? {}'.format(notes_file.closed))
print('-' * 10)

# Automatically closing a file
"""
with open(file_path) as content:
    # Code block
"""
print('Started reading a file.')
with open(dir_path + '/documents/section_10/python-notes.txt') as notes_file:
    print('File closed? {}'.format(notes_file.closed))
    for line in notes_file:
        print(line.rstrip())
    # print(notes_file.read())
print('Finished reading the file')
print('File closed? {}'.format(notes_file.closed))
print('-' * 10)

# File modes
"""
open(path_to_file, mode)
r: open for reading (default)
w: open for writing, truncating first
x: create a new file and open it for writing (safe approach compare to w)
a: open for writing, appending to file
+: open a file for updating (read/write)
b: binary mode
t: text mode (default)
"""
try:
    notes_file = open(dir_path + '/documents/section_10/python-notes.txt', mode='x')
except FileExistsError:
    print('Error on trying to open the existed file')

try:
    notes_file = open(dir_path + '/documents/section_10/not-exists-python-notes.txt', mode='r')
except FileNotFoundError:
    print('Error on trying to open the non-existed file')

# Read binary file
notes_file = open(dir_path + '/documents/section_10/Capture.PNG', 'rb')
print(notes_file.read())
print('-' * 10)

# Write to the file
with open(dir_path + '/documents/section_10/notes-tobeupdated.txt', mode='w') as notes_tobeupdated:
    notes_tobeupdated.write('Written at: {} \n'.format(datetime.now()));

with open(dir_path + '/documents/section_10/notes-tobeupdated.txt', mode='r') as notes_tobeupdated:
    for line in notes_tobeupdated:
        print(line)
print('-' * 10)

# Exercise 1
def prepare_files(file_name):
    str = """This is line one.
This is line two.
Finally, we are on the third and last line of the file."""
    with open(dir_path + '/documents/section_10/' + file_name, mode='w') as exercise_tobeupdated:
        exercise_tobeupdated.write(str)
def cleanup_files(file_name):
    try:
        os.remove(dir_path + '/documents/section_10/' + file_name)
    except:
        print('Could not perform the clean file: {}'.format(file_name))

def prepend_line_number(file_name):
    try:
        new_lines = []
        count = 1
        with open(dir_path + '/documents/section_10/' + file_name, mode='r') as exercise_content:
            lines = exercise_content.readlines()
            for line in lines:
                new_lines.append('{} {}'.format(count, line))
                count += 1
        
        for line in new_lines:
            print(line)
    except Exception as e:
        print('Could not prepend line number in each line {}'.format(e))

file_name = 'exercise.txt'
prepare_files(file_name)
prepend_line_number(file_name)
#cleanup_files(file_name)
print('Finished exercise 1')
print('-' * 10)

# Exercise 2
def prepare_files_exercise_2(file_name):
    str = """man
bear
pig
cow
duck
horse
dog
"""
    with open(dir_path + '/documents/section_10/' + file_name, mode='w') as exercise_tobeupdated:
        exercise_tobeupdated.write(str)

def sort_file_content(file_name):
    try:
        new_lines = []
        count = 1
        with open(dir_path + '/documents/section_10/' + file_name, mode='r') as exercise_content:
            new_lines = exercise_content.readlines()
    except Exception as e:
        print('Could not read the file for sorting: {}'.format(e))

    try:
        with open(dir_path + '/documents/section_10/' + file_name, mode='w') as exercise_content:
            exercise_content.writelines(sorted(new_lines))
    except Exception as e:
        print('Could not sort the content {}'.format(e))

file_name = 'exercise2-animals.txt'
prepare_files_exercise_2(file_name)
sort_file_content('exercise2-animals-sorted.txt')
#cleanup_files(file_name)
print('Finished exercise 2')
