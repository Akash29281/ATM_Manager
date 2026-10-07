from database.db import get_connection


def create_transactions(user_id, transaction_type, amount):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO transactions (user_id, transaction_type, amount)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (user_id, transaction_type, amount))
    conn.commit()
    cursor.close()
    conn.close()
    print("Transaction saved successfully")


def get_transactions(user_id):
    """CLI-compatible history: returns (type, amount)."""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT transaction_type, amount
    FROM transactions
    WHERE user_id = %s
    ORDER BY transaction_date DESC
    """
    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions


def get_transactions_with_date(user_id, limit=None):
    """Web history: returns (type, amount, date)."""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT transaction_type, amount, transaction_date
    FROM transactions
    WHERE user_id = %s
    ORDER BY transaction_date DESC
    """
    params = [user_id]

    if limit is not None:
        query += " LIMIT %s"
        params.append(int(limit))

    cursor.execute(query, tuple(params))
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions
