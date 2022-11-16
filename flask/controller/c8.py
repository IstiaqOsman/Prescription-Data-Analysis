import pandas as pd
import numpy as np
from connection.dbconf import PostgresConnection

class Query8():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT PRACTICE_NAME,SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY,T.MONTH
            FROM snow.FACT_TABLE as f
            inner JOIN snow.SERVICE as S ON S.PRACTICE_CODE = f.PRACTICE_CODE 
            inner JOIN snow.TIME as T ON T.TIME_KEY = f.TIME_KEY 
            GROUP BY CUBE(S.PRACTICE_NAME,T.MONTH)
            ORDER BY MONTH ASC"""
        # cur = con.cursor()
        d = pd.read_sql_query(insert_stmt, con)
        d=d.replace("UNIDENTIFIED", np.nan, regex=True)
        d=d.dropna()
        da=d.groupby("month").head(1)
        da.reset_index(drop=True, inplace=True)
        da['month'] = da['month'].astype(int)
        da=da.sort_values(by=['month'])
        return da.to_dict(orient='records')

if __name__ == '__main__':
    query8 = Query8()
    result = query8.execute()
    print(result)