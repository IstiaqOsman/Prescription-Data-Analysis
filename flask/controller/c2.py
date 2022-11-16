from connection.dbconf import PostgresConnection
import pandas as pd

class Query2():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT COUNT(prescription.bnf_code) as "Total Counts", location.stp_name
            FROM snow.fact_table 
            JOIN snow.prescription ON prescription.prescription_key = fact_table.prescription_key
            JOIN snow.location ON fact_table.location_key = location.location_key
            GROUP BY CUBE(prescription.bnf_code,location.stp_name) 
            ORDER BY COUNT(prescription.bnf_code) DESC"""
        # cur = con.cursor()
        setting_branch = pd.read_sql_query(insert_stmt, con)
        setting_branch=setting_branch.dropna()
        setting_branch=setting_branch.drop_duplicates()
        setting_branch=setting_branch.head(15)
        return setting_branch.to_dict(orient='records')

if __name__ == '__main__':
    query2 = Query2()
    result = query2.execute()
    print(result)