import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'x') as file:
        pass

clock = sg.Text("", key='clock')
label = sg.Text("Enter your to-do:")
textinput = sg.InputText(tooltip="Enter To-do", key="todo")
add = sg.Button("Add")
edit = sg.Button("Edit")
complete = sg.Button("Complete")
exit = sg.Button("Exit")
listbox = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))

layout = [
    [clock],
    [label],
    [textinput, add],
    [listbox, edit, complete],
    [exit]
]

window = sg.Window("My To-Do List", layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):  # Handle window close or Exit button
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todo = values['todo'].strip()
            if todo:
                todos = functions.get_todos()
                todos.append(todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            else:
                sg.popup("Please enter a valid to-do!", font=("Helvetica", 20))

        case "Edit":
            try:
                selected_todo = values['todos'][0]
                edited_todo = values['todo'].strip()

                if edited_todo:
                    todos = functions.get_todos()
                    index = todos.index(selected_todo)
                    todos[index] = edited_todo
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value="")
                else:
                    sg.popup("Please enter a valid to-do!", font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select an item to edit!", font=("Helvetica", 20))

        case "Complete":
            try:
                selected_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(selected_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                sg.popup(f"'{selected_todo}' has been completed!", font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select a task to complete!", font=("Helvetica", 20))

        case "todos":
            if values['todos']:
                window['todo'].update(value=values['todos'][0])
            else:
                window['todo'].update(value="")

window.close()
