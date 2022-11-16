from connection.dbconf import PostgresConnection
import pandas as pd

class Query1():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT prescription.bnf_description, SUM(total_quantity) as "Quantity"
            FROM snow.fact_table 
            JOIN snow.prescription ON prescription.prescription_key = fact_table.prescription_key
            GROUP BY CUBE(prescription.bnf_description,fact_table.total_quantity) 
            ORDER BY SUM(fact_table.total_quantity) DESC"""
        # cur = con.cursor()
        medicine_with_quant = pd.read_sql_query(insert_stmt, con)
        medicine_with_quant = medicine_with_quant.dropna()
        medicine_with_quant = medicine_with_quant.drop_duplicates(['bnf_description'])
        medicine_with_quant=medicine_with_quant.head(10)
        return medicine_with_quant.to_dict(orient='records')

if __name__ == '__main__':
    query1 = Query1()
    result = query1.execute()
    print(result)