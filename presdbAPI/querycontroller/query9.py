import pandas as pd
from dbconnection.dbconf import PostgresConnection


class query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT TIME.MONTH as "Month", SUM(NIC) as "NIC", SUM(ACTUAL_COST) as "total_sales"
                    FROM snow.FACT_TABLE
                    JOIN snow.TIME ON FACT_TABLE.TIME_KEY = TIME.TIME_KEY
                    JOIN snow.PRESCRIPTION ON PRESCRIPTION.PRESCRIPTION_KEY = FACT_TABLE.PRESCRIPTION_KEY
                    WHERE TIME.YEAR = '2021'
                    GROUP BY (TIME.MONTH)
                    ORDER BY (TIME.MONTH)"""
        m_tq_ac = pd.read_sql_query(insert_stmt, con)
        m_tq_ac.reset_index(drop=True, inplace=True)
        m_tq_ac['Month'] = m_tq_ac['Month'].astype('float64')
        return m_tq_ac.to_dict(orient='records')



if __name__ == '__main__':
    query9= query9()
    data = query9.execute()
    print(data)
