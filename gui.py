import FreeSimpleGUI as sg
import functions
import time

clock=sg.Text("", key='clock')
label = sg.Text("Enter your to-do in the box")
textinput = sg.InputText(tooltip="Enter To-do", key="todo")
add = sg.Button("Add")
edit = sg.Button("Edit")
complete = sg.Button("Complete")
exit = sg.Button("Exit")
listbox=sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
layout=[
    [clock],
    [label],
    [textinput,add],
    [listbox, [edit, complete]],
    [exit]
]
window=sg.Window("My to-do list", layout, font=("Helvetica", 20))
while True:
    event, values = window.read()
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos=functions.get_todos()
            todos.append(values['todo'])
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todos_to_edit = values['todos'][0]
                new_todo=values['todo']

                todos=functions.get_todos()
                index=todos.index(todos_to_edit)

                todos[index]=new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            todo_remove = values['todos'][0]

            todos=functions.get_todos()
            todos.remove(todo_remove)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break        
window.close()

