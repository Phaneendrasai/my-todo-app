def get_todos(filepath='todos.txt'):
    """
    Read a text file and returns the list of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """
    Erite the to-do items list in text file
    :param todos_local:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

