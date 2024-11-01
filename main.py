todos=[]
while True:
    user_action = input("What do you want to do? ")
    user_action.strip()
    match user_action:
        case "add":
            todo = input("What do you want to add? ")
            todos.append(todo)
        case "show":
            for i, todo in enumerate(todos):
                print(f"{i+1}. {todo}")
        case "edit":
            index = int(input("Which item do you want to edit? "))
            new_todo = input("What do you want to replace it with? ")
            todos[index-1] = new_todo
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid action")
    