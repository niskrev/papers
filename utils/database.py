"""
Concerned with storing and retrieving papers from a list.

    Created by Nikolay on 9/23/18
"""
from .database_connection import DatabaseConnection

def create_paper_table():
    with DatabaseConnection(host='data.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS papers(name text primary key, author text, read integer)')


def add_paper(name, author):
    with DatabaseConnection(host='data.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO papers VALUES(?, ?, 0)', (name, author))


def get_all_papers():
    with DatabaseConnection(host='data.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM papers')
        papers = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cur.fetchall()]

    return papers


def mark_paper_as_read(name):
    with DatabaseConnection(host='data.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE papers SET read=1 WHERE name==?", (name,))


def delete_paper(name):
    with DatabaseConnection(host='data.db') as conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM papers WHERE name=?', (name,))
