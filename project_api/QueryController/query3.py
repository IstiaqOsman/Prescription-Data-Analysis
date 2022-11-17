from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = """SELECT PCO_NAME, SUM(actual_cost) as Total_Sales
                FROM epd_snow.fact_table as f
                INNER JOIN epd_snow.location as l ON l.location_key = f.location_key
                GROUP BY PCO_NAME
                ORDER BY Total_Sales desc"""
        cur.execute(select_stmt)
        records = cur.fetchall()
        pco_df = pd.DataFrame(list(records), columns=['PCO', 'Total_Sales'])
        pco_df['Total_Sales'] = pco_df['Total_Sales'].astype('float64')
        pco_df = pco_df.head(20)
        # print(pd_data)
        return pco_df.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    print(data)