"""
Concerned with storing and retrieving papers from a list.

    Created by Nikolay on 9/23/18
"""
import sqlite3

def create_paper_table():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS papers(name text primary key, author text, read integer)')

    conn.commit()
    conn.close()


def add_paper(name, author):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO papers VALUES(?, ?, 0)', (name, author))

    conn.commit()
    conn.close()


def get_all_papers():
    return papers


def mark_paper_as_read(name):
    for paper in papers:
        if paper['name'] == name:
            paper['read'] = True

def delete_paper(name):
    global papers
    papers = [paper for paper in papers if paper['name']!=name]