FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    This is a function used to open the file from default filepath and read the file, save it to a variable and close it
    """
    with open(FILEPATH, 'r') as file:
        todos_local = file.readlines()
        return [todo.strip() for todo in todos_local]


def write_todos(todos_local, filepath=FILEPATH):
    """
    This is a function used to open the file from default filepath and write in it from the saved variable, and close it
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(todo + "\n" for todo in todos_local)
