from connection.dbconf import PostgresConnection
import pandas as pd

class Query9():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT time.month as "Month", SUM(nic) as "NIC", SUM(actual_cost) as "total_sales"
            FROM snow.fact_table
            JOIN snow.time ON fact_table.time_key = time.time_key
            JOIN snow.prescription ON prescription.prescription_key = fact_table.prescription_key
            WHERE time.year = 2021
            GROUP BY (time.month)
            ORDER BY (time.month)"""
        m_tq_ac = pd.read_sql_query(insert_stmt, con)
        m_tq_ac.reset_index(drop=True, inplace=True)
        return m_tq_ac.to_dict(orient='records')

if __name__ == '__main__':
    query9 = Query9()
    result = query9.execute()
    print(result)