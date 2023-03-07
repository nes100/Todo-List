from functions import read, write
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

user_prompt = "Type add, show, edit, complete, or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = read()

        todos.append(todo + "\n")

        write(todos, )

    elif user_action.startswith("show"):

        todos = read()

        for index, item in enumerate(todos):
            item = item.strip("\n")  # easiest way to remove \n
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = read()

            new_todo = input("Enter a new item: ")
            todos[number] = new_todo + "\n"

            write(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = read()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(index + 1, "-", item, sep="")

            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            write(todos)

            message = f"Todo {todo_to_remove} was removed from list"
            print(message)

        except IndexError:
            print("There is no item with that number, try again")
        except ValueError:
            print("You must enter a number of the item you want to complete")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye")
