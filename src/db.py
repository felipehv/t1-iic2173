import psycopg2 as psql
from os import getenv
from dotenv import load_dotenv
load_dotenv()

DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
class DB():

    def __init__(self):
        while True:
            try:
                self.conn = psql.connect("dbname={} user={} password={} host={} port={}".format(
                DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT
                ))
                self.cur = self.conn.cursor()
                break
            except:
                pass

    def init_db(self):
        self.cur.execute("CREATE TABLE messages(id serial,  text)")
        self.conn.commit()

        return        

    def some_query(self, data):
        
        
        data = {}

        return data