from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT T.MONTH,BNF_CHAPTER_PLUS_CODE, COUNT(BNF_CHAPTER_PLUS_CODE) " \
                      "FROM epd_snow.FACT_TABLE as f " \
                      "inner JOIN epd_snow.prescription as p ON p.prescription_key = f.prescription_key " \
                      "inner JOIN epd_snow.TIME as T ON T.TIME_KEY = f.TIME_KEY " \
                      "where T.YEAR = 2021" \
                      "GROUP BY (BNF_CHAPTER_PLUS_CODE, T.MONTH)" \
                      "ORDER BY T.MONTH, COUNT(BNF_CHAPTER_PLUS_CODE) desc  "
        cur.execute(select_stmt)
        records = cur.fetchall()
        month_chap_count_df = pd.DataFrame(list(records), columns=['MONTH', 'BNF_CHAPTER', 'COUNT'])
        month_chap_count_df = month_chap_count_df.groupby('MONTH').head(3)


        return month_chap_count_df.to_dict(orient='records')

if   __name__   ==   '__main__'  :
    query6 = Query6()
    data = query6.execute()
    print(data)