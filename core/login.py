from .utils import connect_to_database, create_database_cursor


def validate_user(username, password):
    cnx = connect_to_database()
    cur = create_database_cursor(cnx)
    cur.execute("SELECT * FROM Users;")

    for row in cur:
        if row[1] == username and row[2] == password:
            return (username, row[3])
    return -1
