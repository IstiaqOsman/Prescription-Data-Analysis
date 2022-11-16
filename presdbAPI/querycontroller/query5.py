import pandas as pd
from dbconnection.dbconf import PostgresConnection


class query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT BNF_DESCRIPTION, SUM(f.TOTAL_QUANTITY) as Quantity "\
                "FROM snow.FACT_TABLE as f "\
                "inner JOIN snow.PRESCRIPTION as P ON P.PRESCRIPTION_KEY = f.PRESCRIPTION_KEY "\
                "GROUP BY CUBE(P.BNF_DESCRIPTION,f.Quantity) "\
                "ORDER BY SUM(f.TOTAL_QUANTITY) DESC"


        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['BNF_DESCRIPTION', 'TOTAL_QUANTITY'])
        pd_data = pd_data.dropna()
        pd_data=pd_data.head(10)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5= query5()
    data = query5.execute()
    print(data)
