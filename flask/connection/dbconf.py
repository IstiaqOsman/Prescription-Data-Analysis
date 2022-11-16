import psycopg2
class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database = "presdb",
                                          user = "postgres",
                                          password = "amiIstiaq6045",
                                          host = "127.0.0.1",
                                          port = "5432")
    def getConnection(self):
        # print("Connection to DB established!")
        return self.connection