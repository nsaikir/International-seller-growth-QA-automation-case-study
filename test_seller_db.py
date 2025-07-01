import psycopg2

def test_seller_record_exists():
    conn = psycopg2.connect("dbname=sellerdb user=qa password=qa123 host=localhost")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sellers WHERE email=%s", ("test@example.com",))
    result = cur.fetchone()
    assert result is not None
    conn.close()
