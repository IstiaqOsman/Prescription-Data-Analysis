from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT chemical_substance_bnf_descr, SUM(TOTAL_QUANTITY) as Total_Quantity
                FROM epd_snow.fact_table as f
                INNER JOIN epd_snow.prescription as p ON p.prescription_key = f.prescription_key
                INNER JOIN epd_snow.bnf_chemical as b ON b.bnf_chemical_substance = p.bnf_chemical_substance
                GROUP BY chemical_substance_bnf_descr
                ORDER BY Total_Quantity desc"""
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Ingredient_Appliance', 'Total_Quantity'])
        pd_data['Total_Quantity'] = pd_data['Total_Quantity'].astype('float64')
        pd_data = pd_data.head(20)
        pd_data = pd_data.sort_values('Ingredient_Appliance')
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query1 = Query1()
    data = query1.execute()
    print(data)
