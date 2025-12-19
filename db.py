# ==============================
# db.py
# ==============================

import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    is_premium INTEGER DEFAULT 0,
    daily_count INTEGER DEFAULT 0
)
""")
conn.commit()


def add_user(user_id):
    cur.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    conn.commit()


def get_user(user_id):
    cur.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )
    return cur.fetchone()


def increment_count(user_id):
    cur.execute(
        "UPDATE users SET daily_count = daily_count + 1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()


def can_user_chat(user):
    if user[1] == 1:  # premium
        return True
    return user[2] < 10  # free limit
