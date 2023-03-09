import streamlit as st
import functions

todos = functions.read()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)

st.title("My Todo App ")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ",placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")

st.session_state