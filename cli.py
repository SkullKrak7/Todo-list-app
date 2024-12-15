from functions import write_todos, get_todos

while True:

    user_action = input("Please enter add, show, edit, complete, exit:")
    user_action = user_action.strip()

    if "add" in user_action[0:3]:
        todos = get_todos()
        todo = user_action[4:]
        todos.append(todo)
        write_todos(todos)

    if "show" in user_action[0:4]:
        todos = get_todos()
        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

    if "edit" in user_action[0:4]:
        todos = get_todos()
        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

        index = int(input("Enter item number what you want to edit: ")) - 1
        replace = input("Type what you want to replace with: ")

        todos[index] = replace

        write_todos(todos)

    if "complete" in user_action[0:8]:
        todos = get_todos()

        index = int(input("Which item number do you want to mark as complete? "))
        todos.pop(index - 1)

        write_todos(todos)

    if "exit" in user_action[0:4]:

        print("Your current list is:")

        todos = get_todos()

        for i, todo in enumerate(todos):
            todo.strip('\n')
            print(f"{i + 1}. {todo}")

        print("Goodbye!")

        break
