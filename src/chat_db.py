import sqlite3
from datetime import datetime
from sqlite3 import Connection


class ChatDB:
    def __init__(self, db_path: str = "history.sqlite3"):
        try:
            self.conn: Connection = sqlite3.connect(db_path)
            self.create_table()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to initialize database: {e}") from e

    def create_table(self):
        _ = self.conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact TEXT NOT NULL,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_message(self, contact: str, sender: str, message: str) -> None:
        timestamp: str = datetime.now().isoformat()
        _ = self.conn.execute(
            "INSERT INTO messages (contact, sender, message, timestamp) VALUES (?, ?, ?, ?)",  # noqa: E501
            (contact, sender, message, timestamp),
        )
        self.conn.commit()

    def load_messages(self, contact: str) -> list[tuple[str, str, str]]:
        cursor = self.conn.execute(
            "SELECT sender, message, timestamp FROM messages WHERE contact = ? ORDER BY timestamp",  # noqa: E501
            (contact,),
        )
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()
