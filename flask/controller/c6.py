import pandas as pd
import numpy as np
from connection.dbconf import PostgresConnection

class Query6():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT REGIONAL_OFFICE_NAME, SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY, T.MONTH , T.YEAR
            FROM snow.FACT_TABLE as f 
            inner JOIN snow.LOCATION as L ON L.LOCATION_KEY = f.LOCATION_KEY 
            inner JOIN snow.TIME as T ON T.TIME_KEY = f.TIME_KEY 
            GROUP BY CUBE(L.REGIONAL_OFFICE_NAME,T.MONTH, T.YEAR)
            ORDER BY TOTAL_QUANTITY DESC"""
        # cur = con.cursor()
        b = pd.read_sql_query(insert_stmt, con)
        b=b.replace("UNIDENTIFIED",np.nan, regex=True)
        b=b.dropna()
        b['month'] = b['month'].astype(int)
        b['year'] = b['year'].astype(int)
        ba=b.groupby(["month","year"]).head(1)
        ba.reset_index(drop=True, inplace=True)
        ba=ba.sort_values(by=['year','month'])
        return ba.to_dict(orient='records')

if __name__ == '__main__':
    query6 = Query6()
    result = query6.execute()
    print(result)


    