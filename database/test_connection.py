from db import get_connection

def test_connection():
    conn = get_connection()

    if conn.is_connected():
        print("✅ Database Connected Successfully")

    conn.close()


if __name__ == "__main__":
    test_connection()