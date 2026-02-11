import sqlite3

def initDb():
    connection = sqlite3.connect('database.sqlite')
    with open('schema.sql', 'r') as schema:
        connection.executescript(schema.read())
    connection.commit()
    connection.close()

def get_prefix(bot, message):
    if not message.guild:
        return '!'

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('select value from settings where guild_id = ? and key = "prefix"', (message.guild.id,))
        prefix = cursor.fetchone()
        if prefix:
            return prefix[0]
        return '!'
    finally:
        conn.close()
        

def get_connection():
    return sqlite3.connect('database.sqlite')

def set_prefix(guild_id, prefix):
    conn = get_connection()
    try:
        with conn:
            conn.execute('''
                insert into settings(guild_id, key, value)
                values(?, 'prefix', ?)
                on conflict(guild_id, key) do update set value = excluded.value
            ''', (guild_id, prefix))
    finally:
        conn.close()