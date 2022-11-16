import numpy as np
import pandas as pd

from dbconnection.dbconf import PostgresConnection


class query6:
     def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
     # def execute(self):
     #    con = PostgresConnection().getConnection()
     #    insert_stmt = """SELECT STP_NAME, PCO_NAME FROM snow.LOCATION
     #    """
     #    cur = con.cursor()
     #    stp_pco = pd.read_sql_query(insert_stmt, con)
     #
     #    insert_stmt = """SELECT LOCATION.STP_NAME, BNF_CODE
     #    FROM snow.FACT_TABLE
     #    JOIN snow.PRESCRIPTION ON FACT_TABLE.prescription_key = PRESCRIPTION.PRESCRIPTION_KEY
     #    JOIN snow.LOCATION ON FACT_TABLE.LOCATION_KEY = LOCATION.LOCATION_KEY
     #    ORDER BY STP_NAME
     #    """
     #    stp_bnf = pd.read_sql_query(insert_stmt, con)
     #    x = stp_pco.drop_duplicates()
     #    x = pd.DataFrame(x.value_counts(subset=['STP_NAME']))
     #    x = x.sort_values('STP_NAME')
     #    x.reset_index(drop=True, inplace=True)
     #
     #    y = pd.DataFrame(stp_bnf.value_counts(subset=['STP_NAME']))
     #    y = y.sort_values('STP_NAME')
     #    y.reset_index(drop=True, inplace=True)
     #
     #    z = stp_pco.drop(['PCO_NAME'], axis=1)
     #    z = z.drop_duplicates()
     #    z = z.sort_values('STP_NAME')
     #    z.reset_index(drop=True, inplace=True)
     #
     #    xyz = pd.merge(z, x, left_index=True, right_index=True)
     #    xyz.rename(columns={0: 'count_of_pco'}, inplace=True)
     #
     #    xyz2 = pd.merge(z, y, left_index=True, right_index=True)
     #    xyz2.rename(columns={0: 'count_of_bnf'}, inplace=True)
     #
     #    stp_pcoc_bnfc = pd.merge(left=xyz, right=xyz2, how='left', left_on='STP_NAME', right_on='STP_NAME')
     #    stp_pcoc_bnfc = stp_pcoc_bnfc.replace("UNIDENTIFIED", np.nan, regex=True)
     #    stp_pcoc_bnfc = stp_pcoc_bnfc.dropna()
     #    stp_pcoc_bnfc.reset_index(drop=True, inplace=True)
     #    stp_pcoc_bnfc
     #
     #    return stp_pcoc_bnfc.to_dict(orient='records')


if __name__ == '__main__':
    query6= query6()
    data = query6.execute()
    print(data)
