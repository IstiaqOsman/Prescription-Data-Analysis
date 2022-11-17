from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = """SELECT location.stp_name,COUNT(prescription.bnf_code), SUM(actual_cost) as sales
        FROM epd_snow.location
        JOIN epd_snow.fact_table ON fact_table.location_key = location.location_key
        JOIN epd_snow.prescription ON fact_table.prescription_key = prescription.prescription_key
        GROUP BY (location.stp_name, prescription.bnf_code)
        ORDER BY COUNT(prescription.bnf_code) DESC """

        cur.execute(select_stmt)
        records = cur.fetchall()
        stp_count_sales_df = pd.DataFrame(list(records), columns=['STP_NAME', 'COUNT', 'Sales'])
        stp_count_sales_df = stp_count_sales_df.dropna()
        return stp_count_sales_df.to_dict(orient='records')

if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)