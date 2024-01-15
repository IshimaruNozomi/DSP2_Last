import sqlite3
from bs4 import BeautifulSoup
import requests
import time
import re
import pandas as pd

#URLのリストを作成
number_list = [2019105283,2019104740,2018103559,2019105346,2018105165,2020103532,2017101431,2020102899,2020103458,2017104691,2017105477,2018105269,2019103588,2019100109,2017102170,2017104936]

#Google Colab
path = '/Users/nozomi0407/DSP2_Last/'
#DBファイル名
db_name = 'arima.sqlite'
#DBに接続する（指定したファイルが存在しない場合は新規に作成される）
con = sqlite3.connect(path + db_name)
#DBへの接続を閉じる
con.close()
#１.DBに接続する
con = sqlite3.connect(path + db_name)
#print(type(con))
#２.SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．実行したいSQLを用意する
# テーブルを作成するSQL
sql_create_table_googlegithubs = 'CREATE TABLE arima(weather text, name text, popular int, rank int, jockey text, distance int, stage text, weight int);'
# 4．SQLを実行する
cur.execute(sql_create_table_googlegithubs)
# 5．必要があればコミットする（データ変更等があった場合）
# 6．DBへの接続を閉じる
con.close()