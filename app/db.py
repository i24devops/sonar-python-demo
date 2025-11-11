import sqlite3

def find_user_by_name(db_path, name):
    # Noncompliant: potential SQL injection (string formatting instead of params)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT id, name FROM users WHERE name = '{name}'"  # Noncompliant
    try:
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        conn.close()

# TODO: switch to parameterized queries (good practice)
# cursor.execute("SELECT id, name FROM users WHERE name = ?", (name,))
