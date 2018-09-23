"""
    Created by Nikolay on 9/23/18
"""
from utils import database

USER_CHOICE = """
ENTER:
- 'a' to add a new paper
- 'l' to list all papers
- 'r' to mark a papers as read
- 'd' to delete a paper
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_paper()
        elif user_input == 'l':
            pass
        elif user_input == 'r':
            pass
        elif user_input == 'd':
            pass
        else:
            print('Unknown command. Please try again')
        user_input = input(USER_CHOICE)


# def prompt_add_paper() ask for paper name and author
# def prompt_list_papers() show all papers in our list
# def prompt_read_paper() ask for paper name and change it to "read" in our list
# def promt_delete_paper() akd for paper name and remove the paper from list

if __name__ == '__main__':
    menu()