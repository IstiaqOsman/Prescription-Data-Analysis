import pandas as pd
from dbconnection.dbconf import PostgresConnection


class query7:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT b.CHEMICAL_SUBSTANCE_BNF_DESCR, SUM(f.TOTAL_QUANTITY) as Total_Quantity "\
                    "FROM snow.FACT_TABLE as f "\
                    "INNER JOIN snow.PRESCRIPTION as p ON p.PRESCRIPTION_KEY = f.PRESCRIPTION_KEY "\
                    "INNER JOIN snow.BNF_CHEMICAL as b ON b.BNF_CHEMICAL_SUBSTANCE = p.BNF_CHEMICAL_SUBSTANCE "\
                    "GROUP BY CHEMICAL_SUBSTANCE_BNF_DESCR "\
                    "ORDER BY Total_Quantity desc "

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Ingredient_Appliance', 'Total_Quantity'])
        pd_data['Total_Quantity'] = pd_data['Total_Quantity'].astype('float64')
        pd_data = pd_data.head(20)
        pd_data = pd_data.sort_values('Ingredient_Appliance')
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query7= query7()
    data = query7.execute()
    print(data)
