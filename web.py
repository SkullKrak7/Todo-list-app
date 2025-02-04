import streamlit as st
import functions


def add_todo():
    """Adds a new to-do item from user input."""
    todo = st.session_state["new_todo"].strip()  # Trim spaces
    if todo:  # Prevent empty todos
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Always clear input


#  Ensure todos is always a list
todos = functions.get_todos() or []

st.title("My Todo App ✅")
st.subheader("Increase your productivity with this simple todo app!")

# Track items to remove (fixing pop index issue)
todos_to_remove = []

for index, todo in enumerate(todos):
    todo = todo.strip()  # Remove newline characters
    if st.checkbox(todo, key=f"todo_{index}"):
        todos_to_remove.append(index)  # Store index to remove

# Remove todos outside the loop to prevent indexing errors
if todos_to_remove:
    for index in sorted(todos_to_remove, reverse=True):  # Reverse to avoid shifting
        todos.pop(index)
    functions.write_todos(todos)
    st.rerun()  # Refresh the UI safely

# Prevent empty input + Hide label for accessibility
st.text_input(label="Add a Task", placeholder="Click here to add a new todo...",
              on_change=add_todo, key='new_todo', label_visibility="collapsed")
