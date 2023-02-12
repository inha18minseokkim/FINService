from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import declaration
DB_URL = f'mysql+pymysql://{declaration.USERNAME_DB}:{declaration.PASSWORD_DB}@{declaration.HOST_DB}:{declaration.PORT_DB}/{declaration.NAME_DB}'

class engineConn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
if __name__ == "__main__":
    ec = engineConn()