import pandas as pd
from dbconnection.dbconf import PostgresConnection


class query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        insert_stmt = """SELECT s.PRACTICE_NAME, COUNT(s.PRACTICE_NAME)
              FROM snow.FACT_TABLE as f
              INNER JOIN snow.SERVICE as s ON s.PRACTICE_CODE = f.PRACTICE_CODE
              GROUP BY s.PRACTICE_NAME
              ORDER BY COUNT(s.PRACTICE_NAME) DESC"""
        cur.execute(insert_stmt)
        records = cur.fetchall()
        service_df = pd.DataFrame(list(records), columns=['Service_Name', 'Count'])
        service_df.drop(service_df[(service_df['Service_Name'] == 'UNIDENTIFIED DOCTORS')].index, inplace=True)
        service_df = service_df.head(10)

        return service_df.to_dict(orient='records')


if __name__ == '__main__':
    query10= query10()
    data = query10.execute()
    print(data)
