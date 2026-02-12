import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / 'data' / 'database.sqlite'
SCHEMA_PATH = BASE_DIR / 'data' / 'schema.sql'

def initDb():
    print(f"Buscando base de datos en: {DB_PATH}")
    print(f"Buscando schema en: {SCHEMA_PATH}")
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    
    with open(SCHEMA_PATH, 'r') as schema:
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
    return sqlite3.connect(DB_PATH)

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