import psycopg2

hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'Beornottobe1'
port_id = 5432

def db_connection():
    return psycopg2.connect(
        host="localhost",
        dbname = database,
         user = username,
        password = pwd,
        port = port_id

)

def read_dict():
    dbconn = db_connection()
    cur = dbconn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    dbconn.close()
    return rows


while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")

    if cmd == "list":
        rows = read_dict()
        for row in rows:
            print(f"id: {row[0]}, word: {row[1]}, translation: {row[2]}")
        
    elif cmd == "quit":
        exit()
    else:
        print("error")