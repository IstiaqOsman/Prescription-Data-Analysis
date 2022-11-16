from connection.dbconf import PostgresConnection
import pandas as pd
import numpy as np

class Query10():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT stp_name, pco_name 
            FROM snow.location"""
        cur = con.cursor()
        stp_pco = pd.read_sql_query(insert_stmt, con)

        insert_stmt = """SELECT stp_name, bnf_code
            FROM snow.fact_table
            JOIN snow.prescription ON fact_table.prescription_key = prescription.prescription_key
            JOIN snow.location ON fact_table.location_key = location.location_key 
            ORDER BY stp_name"""
        stp_bnf = pd.read_sql_query(insert_stmt, con)

        x=stp_pco.drop_duplicates()
        x = pd.DataFrame(x.value_counts(subset=['stp_name']))
        x = x.sort_values('stp_name')
        x.reset_index(drop=True, inplace=True)

        y = pd.DataFrame(stp_bnf.value_counts(subset=['stp_name']))
        y = y.sort_values('stp_name')
        y.reset_index(drop=True, inplace=True)

        z = stp_pco.drop(['pco_name'],axis=1)
        z = z.drop_duplicates()
        z = z.sort_values('stp_name')
        z.reset_index(drop=True, inplace=True)

        xyz=pd.merge(z, x, left_index=True, right_index=True)
        xyz.rename(columns = {0:'count_of_pco'}, inplace = True)

        xyz2=pd.merge(z, y, left_index=True, right_index=True)
        xyz2.rename(columns = {0:'count_of_bnf'}, inplace = True)

        stp_pcoc_bnfc = pd.merge(left=xyz, right=xyz2, how='left', left_on='stp_name', right_on='stp_name')
        stp_pcoc_bnfc=stp_pcoc_bnfc.replace("UNIDENTIFIED", np.nan, regex=True)
        stp_pcoc_bnfc=stp_pcoc_bnfc.dropna()
        stp_pcoc_bnfc.reset_index(drop=True, inplace=True)
        stp_pcoc_bnfc


        return stp_pcoc_bnfc.to_dict(orient='records')

if __name__ == '__main__':
    query10 = Query10()
    result = query10.execute()
    print(result)