import streamlit as st
import functions

todos = functions.get_todos()

def add_to_do():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo..",
              on_change=add_to_do, key='new_todo')