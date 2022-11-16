import pandas as pd

from dbconnection.dbconf import PostgresConnection


class query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT REGIONAL_OFFICE_NAME,SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY,T.MONTH "\
                "FROM snow.FACT_TABLE as f "\
                "inner JOIN snow.LOCATION as L ON L.LOCATION_KEY = f.LOCATION_KEY "\
                "inner JOIN snow.TIME as T ON T.TIME_KEY = f.TIME_KEY "\
                "WHERE T.YEAR='2021' "\
                "GROUP BY(L.REGIONAL_OFFICE_NAME,T.MONTH,TOTAL_QUANTITY)"\
                "ORDER BY TOTAL_QUANTITY DESC "

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['REGIONAL_OFFICE_NAME','TOTAL_QUANTITY','MONTH'])
        pd_data['MONTH'] = pd_data['MONTH'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('MONTH').head(1)
        pd_data = pd_data.sort_values('MONTH')
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2 = query2()
    data = query2.execute()
    print(data)
