"""
main file for the papers app
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

Your choice: """


def menu():
    database.create_paper_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_paper()
        elif user_input == 'l':
            list_papers()
        elif user_input == 'r':
            prompt_read_paper()
        elif user_input == 'd':
            prompt_delete_paper()
        else:
            print('Unknown command. Please try again')
        user_input = input(USER_CHOICE)


def prompt_add_paper():
    name = input('Enter the name of the paper: ')
    author = input('Enter the name of the author: ')
    database.add_paper(name, author)


def list_papers():
    papers = database.get_all_papers()
    for paper in papers:
        read = 'Yes' if paper['read'] else 'No'
        print('{name}, {author}, read: {read}'.format(name=paper['name'],
                                                author=paper['author'],
                                                read=read))


def prompt_read_paper():
    name = input('Enter the name of the paper you finished reading: ')
    database.mark_paper_as_read(name)


def prompt_delete_paper():
    name = input('Enter the name of the paper you want to delete: ')
    database.delete_paper(name)


if __name__ == '__main__':
    menu()