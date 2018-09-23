"""
Concerned with storing and retrieving papers from a list.

    Created by Nikolay on 9/23/18
"""

papers = []


def add_paper(name, author):
    papers.append({'name': name, 'author': author, 'read': False})


def list_papers():
    for paper in papers:
        print('{name}, {author}, {read}'.format(name=paper['name'],
                                                author=paper['author'],
                                                read=paper['read']))

def read_paper(name):
    for paper in papers:
        if paper['name'] == name:
            paper['read'] = True

def delete_paper(name):
    papers = [paper for paper in papers if paper['name']!=name]