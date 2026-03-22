import sqlite3

DB_NAME = "logs.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            risk TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_log(event, risk):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO logs (event, risk) VALUES (?, ?)",
        (event, risk)
    )

    conn.commit()
    conn.close()


def fetch_logs():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("SELECT * FROM logs")

    rows = cur.fetchall()

    conn.close()

    return rows