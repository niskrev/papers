"""
Concerned with storing and retrieving papers from a list.

    Created by Nikolay on 9/23/18
"""
import sqlite3
from typing import List, Dict, Union
from .database_connection import DatabaseConnection

Paper = Dict[str, Union[str, int]]


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS papers(name text primary key, author text, read integer)')
        self.conn.commit()

    def add_paper(self, name: str, author: str) -> None:
        self.cur.execute('INSERT INTO papers VALUES(?, ?, 0)', (name, author))
        self.conn.commit()

    def get_all_papers(self) -> List[Paper]:
        self.cur.execute('SELECT * FROM papers')
        papers = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in self.cur.fetchall()]
        return papers

    def mark_paper_as_read(self, name: str) -> None:
        self.cur.execute("UPDATE papers SET read=1 WHERE name==?", (name,))
        self.conn.commit()

    def delete_paper(self, name: str) -> None:
        self.cur = self.conn.cursor()
        self.cur.execute('DELETE FROM papers WHERE name=?', (name,))

    def __del__(self):
        self.conn.close()
