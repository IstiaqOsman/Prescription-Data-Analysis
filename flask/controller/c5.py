import pandas as pd
import numpy as np
from connection.dbconf import PostgresConnection

class Query5():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT REGIONAL_OFFICE_NAME,SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY 
        FROM snow.FACT_TABLE as f 
        inner JOIN snow.LOCATION as L ON L.LOCATION_KEY = f.LOCATION_KEY 
        GROUP BY CUBE(L.REGIONAL_OFFICE_NAME) 
        ORDER BY SUM (f.TOTAL_QUANTITY) DESC
        """
        # cur = con.cursor()
        a = pd.read_sql_query(insert_stmt, con)
        a=a.dropna()
        return a.to_dict(orient='records')

if __name__ == '__main__':
    query5 = Query5()
    result = query5.execute()
    print(result)