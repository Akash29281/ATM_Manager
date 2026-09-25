from database.db import get_connection


def create_user(username, pin):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (username, pin, balance)
    VALUES (%s, %s, %s)
    """

    values = (username, pin, 0)

    cursor.execute(query, values)

    conn.commit()

    print("User created successfully")

    cursor.close()
    conn.close()


def get_user(username):

    conn = get_connection()
    cursor = conn.cursor(buffered=True)

    query = """
    SELECT id, username, pin, balance
    FROM users
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user