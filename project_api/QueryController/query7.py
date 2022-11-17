from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):

        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT BNF_CHAPTER_PLUS_CODE, COUNT(BNF_CHAPTER_PLUS_CODE), SUM(f.ACTUAL_COST) as Sales " \
                      "FROM epd_snow.FACT_TABLE as f " \
                      "inner JOIN epd_snow.prescription as p ON p.prescription_key = f.prescription_key " \
                      "inner JOIN epd_snow.TIME as T ON T.TIME_KEY = f.TIME_KEY " \
                      "where T.YEAR = 2021" \
                      "GROUP BY (BNF_CHAPTER_PLUS_CODE, T.MONTH)" \
                      "ORDER BY T.MONTH,  Sales desc"
        cur.execute(select_stmt)
        records = cur.fetchall()
        Total_Quantity_df = pd.DataFrame(list(records), columns=['MONTH', 'BNF_CHAPTER', 'Count', 'Sales'])
        Total_Quantity_df['Sales'] = Total_Quantity_df['Sales'].astype('int64')
        Total_Quantity_df = Total_Quantity_df.groupby('MONTH').head(3)

        return Total_Quantity_df.to_dict(orient='records')


if __name__ == '__main__':
    query7 = Query7
    data = query7.execute()
    print(data)

