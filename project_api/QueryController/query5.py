from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        insert_stmt = """SELECT s.practice_name, COUNT(s.practice_name)
        FROM epd_snow.fact_table as f
        INNER JOIN epd_snow.service as s ON s.practice_code = f.practice_code
        GROUP BY s.practice_name
        ORDER BY COUNT(s.practice_name) DESC"""
        cur.execute(insert_stmt)
        records = cur.fetchall()
        service_df = pd.DataFrame(list(records), columns=['Service_Name', 'Count'])
        service_df.drop(service_df[(service_df['Service_Name'] == 'UNIDENTIFIED DOCTORS')].index, inplace=True)
        service_df = service_df.head(10)

        return service_df.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
