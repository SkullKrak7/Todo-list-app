from functions import write_todos, get_todos
import FreeSimpleGUI

FILEPATH = 'todos.txt'

while True:

    user_action = input("Please enter add, show, edit, complete, exit:")
    user_action = user_action.strip()

    if "add" in user_action[0:3]:
        todos = get_todos(FILEPATH)
        todo = user_action[4:]
        todos.append(todo)
        write_todos(FILEPATH, todos)

    if "show" in user_action[0:4]:
        todos = get_todos(FILEPATH)
        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

    if "edit" in user_action[0:4]:
        todos = get_todos(FILEPATH)
        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

        index = int(input("Enter item number what you want to edit: ")) - 1
        replace = input("Type what you want to replace with: ") m

        todos[index] = replace

        write_todos(FILEPATH, todos)

    if "complete" in user_action[0:8]:
        todos = get_todos(FILEPATH)

        index = int(input("Which item number do you want to mark as complete? "))
        todos.pop(index - 1)

        write_todos(FILEPATH, todos)

    if "exit" in user_action[0:4]:

        print("Your current list is:")

        todos = get_todos(FILEPATH)

        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

        print("Goodbye!")

        break
