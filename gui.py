import FreeSimpleGUI as sg
import functions

layout=[
    [sg.Text("Enter your to-do in the box")],
    [sg.InputText(tooltip="Enter To-do", key="todo"),sg.Button("Add")],
    [sg.Listbox(values=functions.get_todos(), key = 'todos', enable_events=True, size=[45,10]), sg.Button("Edit"), sg.Button("Complete"),
    [sg.Button("Exit")]]
]
window=sg.Window("My to-do list", layout, font=("Helvetica", 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos=functions.get_todos()
            todos.append(values['todo'])
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todos_to_edit = values['todos'][0]
            new_todo=values['todo']

            todos=functions.get_todos()
            index=todos.index(todos_to_edit)

            todos[index]=new_todo
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            todo_remove = values['todos'][0]

            todos=functions.get_todos()
            todos.remove(todo_remove)
            functions.write_todos(todos)

            windows['todos'].update(values=todos)
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break        


