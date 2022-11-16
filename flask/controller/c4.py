from connection.dbconf import PostgresConnection
import pandas as pd
import numpy as np

class Query4():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT prescription.bnf_code, location.address_1
            FROM snow.fact_table
            JOIN snow."location" ON "location".location_key = fact_table.location_key
            JOIN snow.prescription ON prescription.prescription_key = fact_table.prescription_key
            GROUP BY CUBE(bnf_code, address_1) 
            ORDER BY address_1"""
        # cur = con.cursor()
        most_patients_area = pd.read_sql_query(insert_stmt, con)
        most_patients_area = most_patients_area.replace('NaN', np.nan,regex=True)
        most_patients_area = most_patients_area.replace('-', np.nan,regex=True)
        most_patients_area=most_patients_area.dropna()
        x = most_patients_area['address_1'].value_counts()
        most_patients_area = pd.DataFrame(x)
        most_patients_area=most_patients_area.head(20)
        return most_patients_area.to_dict(orient='records')

if __name__ == '__main__':
    query4 = Query4()
    result = query4.execute()
    print(result)