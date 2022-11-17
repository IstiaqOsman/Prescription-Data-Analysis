from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        insert_stmts = """SELECT chemical_substance_bnf_descr, SUM(actual_cost) as Total_Sales
                FROM epd_snow.fact_table as f
                INNER JOIN epd_snow.prescription as p ON p.prescription_key = f.prescription_key
                INNER JOIN epd_snow.bnf_chemical as b ON b.bnf_chemical_substance = p.bnf_chemical_substance
                GROUP BY chemical_substance_bnf_descr
                ORDER BY Total_Sales desc"""
        cur.execute(insert_stmts)
        records_type = cur.fetchall()
        type_df = pd.DataFrame(list(records_type), columns=['Ingredient_Appliance', 'Total_Sales'])
        type_df = type_df.head(20)
        type_df = type_df.sort_values('Ingredient_Appliance')
        # print(pd_data)
        return type_df.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)