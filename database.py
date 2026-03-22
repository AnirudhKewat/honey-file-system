def insert_log(filename, user):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs(filename, user) VALUES (?, ?)",
        (filename, user)
    )

    conn.commit()

    conn.close()