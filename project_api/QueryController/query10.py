from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        insert_stmt = """SELECT REGIONAL_OFFICE_NAME,STP_NAME, PCO_NAME,PRACTICE_NAME,SUM(ACTUAL_COST)
                        FROM epd_snow.fact_table as f
                        INNER JOIN epd_snow.location as l ON l.location_key = f.location_key
                        INNER JOIN epd_snow.service as s ON s.practice_code = f.practice_code
                        GROUP BY REGIONAL_OFFICE_NAME, STP_NAME, PCO_NAME,PRACTICE_NAME
                        ORDER BY SUM(ACTUAL_COST) desc """
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        cur.execute(insert_stmt)
        records = cur.fetchall()
        chapter_quantity_df = pd.DataFrame(list(records),
                                           columns=['REGIONAL_OFFICE_NAME', 'STP_NAME', 'PCO_NAME', 'PRACTICE_NAME',
                                                    'Sales'])


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)