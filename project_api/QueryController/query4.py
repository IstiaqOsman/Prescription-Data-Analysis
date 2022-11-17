from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        insert_stmt = """SELECT month, AVG(actual_cost) as Total_Sales
                        FROM epd_snow.fact_table as f
                        INNER JOIN epd_snow.time as t ON t.time_key = f.time_key
                        GROUP BY month
                        ORDER BY month """
        cur.execute(insert_stmt)
        records = cur.fetchall()
        monthly_Total_Sales_df = pd.DataFrame(list(records), columns=['Month', 'Total_Sales'])
        #print(Monthly_Total_Sales_df)
        return monthly_Total_Sales_df.to_dict(orient='records')


if __name__ == '__main__':
    query4 = Query4()
    data = query4.execute()
    print(data)