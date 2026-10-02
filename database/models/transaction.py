from database.db import get_connection
# from database.models.user import get_user_by_card
# Transactions data
def create_transactions(user_id, transaction_type,amount):
    conn = get_connection()
    cursor = conn.cursor()

    query = """INSERT INTO transactions(user_id,transaction_type,
    amount) VALUES (%s,%s,%s)
    """

    values = (
    user_id,transaction_type,amount
    )

    cursor.execute(query, values)
    conn.commit()
    print("Transaction saved successfully:")
    cursor.close()
    conn.close()



def get_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """ SELECT transaction_type,amount FROM transactions WHERE user_id = %s"""

    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()

    return transactions

