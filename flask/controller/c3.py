from connection.dbconf import PostgresConnection
import pandas as pd

class Query3():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT COUNT(location.pco_code), location.stp_name
            FROM snow.location
            GROUP BY(location.stp_name)
            ORDER BY COUNT(location.pco_code) DESC"""
        # cur = con.cursor()
        stpwise_pco = pd.read_sql_query(insert_stmt, con)
        stpwise_pco=stpwise_pco.dropna()
        stpwise_pco=stpwise_pco.drop_duplicates(['stp_name'])
        stpwise_pco=stpwise_pco.head(20)
        return stpwise_pco.to_dict(orient='records')

if __name__ == '__main__':
    query3 = Query3()
    result = query3.execute()
    print(result)