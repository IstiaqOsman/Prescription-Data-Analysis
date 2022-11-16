import pandas as pd

from dbconnection.dbconf import PostgresConnection


class query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query1 = "SELECT REGIONAL_OFFICE_NAME,SUM(f.TOTAL_QUANTITY) as TOTAL_QUANTITY "\
                "FROM snow.FACT_TABLE as f "\
                "inner JOIN snow.LOCATION as L ON L.LOCATION_KEY = f.LOCATION_KEY "\
                "GROUP BY CUBE(L.REGIONAL_OFFICE_NAME)"\
                "ORDER BY SUM (f.TOTAL_QUANTITY) DESC"

        cur.execute(query1)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['REGIONAL_OFFICE_NAME', 'TOTAL_QUANTITY'])
       # pd_data['TOTAL_QUANTITY'] = pd_data['TOTAL_QUANTITY'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query1 = query1()
    data = query1.execute()
    print(data)

