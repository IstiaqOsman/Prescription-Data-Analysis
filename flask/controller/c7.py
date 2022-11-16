import pandas as pd
import numpy as np
from connection.dbconf import PostgresConnection

class Query7():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT BNF_DESCRIPTION ,SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY,T.MONTH 
            FROM snow.FACT_TABLE as f 
            inner JOIN snow.PRESCRIPTION as P ON P.PRESCRIPTION_KEY = f.PRESCRIPTION_KEY
            inner JOIN snow.TIME as T ON T.TIME_KEY = f.TIME_KEY 
            GROUP BY CUBE(P.BNF_DESCRIPTION,T.MONTH)
            ORDER BY TOTAL_QUANTITY DESC"""
        # cur = con.cursor()
        c = pd.read_sql_query(insert_stmt, con)
        c=c.replace("None", np.nan, regex=True)
        c=c.dropna()
        ca=c.groupby("month").head(1)
        ca.reset_index(drop=True, inplace=True)
        ca['month'] = ca['month'].astype(int)
        ca=ca.sort_values(by=['month'])
        return ca.to_dict(orient='records')

if __name__ == '__main__':
    query7 = Query7()
    result = query7.execute()
    print(result)