FILEPATH = "todos.txt"

# function to get todos from todos.txt to avoid repetitive code
# setting a default parameters/arguments for filepath
def get_todos(filepath=FILEPATH):
    # this is a doc string
    """ Read a text file and return the list of to-do items. 
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

# print(help(get_todos))

# function to write todos in todos.txt, does not need to return
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# this is a conditional block and it will only activate if this functions.py file is run, will not show if you run in main.py
# print(__name__) <-- This will be "__main__" only when the file is run in functions.py, if you run the file main.py the print(__name__) will be "functions" so the conditional below will not be executed
# if __name__ == "__main__":
#     print('Hello')
#     print(get_todos())

# use multi-line strings for larger text
# text = """
# This is a larger paragraph 
# that has multiple lines
# it uses the triple quotes to allow 
# me to write more lines of text
# """
# print(text)
