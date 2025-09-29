import sqlite3
from datetime import datetime


class ChatDB:
    def __init__(self, db_path="chat_history.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact TEXT NOT NULL,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_message(self, contact, sender, message):
        timestamp = datetime.now().isoformat()
        self.conn.execute(
            "INSERT INTO messages (contact, sender, message, timestamp) VALUES (?, ?, ?, ?)",
            (contact, sender, message, timestamp),
        )
        self.conn.commit()

    def load_messages(self, contact):
        cursor = self.conn.execute(
            "SELECT sender, message, timestamp FROM messages WHERE contact = ? ORDER BY timestamp",
            (contact,),
        )
        return cursor.fetchall()

    def close(self):
        self.conn.close()
