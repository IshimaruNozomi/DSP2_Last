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
#sql_create_table_googlegithubs = 'CREATE TABLE arima(weather text, name text, popular int, rank int, jockey text, distance int, stage text, weight int);'
# 4．SQLを実行する
#cur.execute(sql_create_table_googlegithubs)
# 5．必要があればコミットする（データ変更等があった場合）
# 6．DBへの接続を閉じる
con.close()

#URL取得
for i in number_list:
  time.sleep(1)
  url = f'https://db.netkeiba.com/horse/{i}/'
  print(url)
  r = requests.get(url)
  r.encoding = r.apparent_encoding
  html_soup = BeautifulSoup(r.text, 'html.parser')

  #各リストの作成
  race_list = []
  weather_list = []
  popular_list = []
  rank_list = []
  jockey_list = []
  distance_list = []
  stage_list = []
  weight_list = []

  if i in [2019105283, 2019104740, 2018103559, 2020103532]:
    df = pd.read_html(url)[4]
  else:
    df = pd.read_html(url)[3]
  df = df.drop(columns = ["日付","開催","R","映 像","頭 数","枠 番","馬 番","オ ッ ズ","斤 量","馬場 指数","タイム","ﾀｲﾑ 指数","厩舎 ｺﾒﾝﾄ","備考","着差","通過","ペース","上り","勝ち馬 (2着馬)","賞金"])
  df = df.dropna(how='any')
  #print(df)
  for _, row in df.iterrows():
    race_list.append(row["レース名"])
    weather_list.append(row["天 気"])
    popular_list.append(row["人 気"])
    rank_list.append(row["着 順"])
    jockey_list.append(row["騎手"])
    distance_list.append(row["距離"])
    stage_list.append(row["馬 場"])
    weight_list.append(row["馬体重"])

  all_list = list(zip(race_list, weather_list, popular_list, rank_list, jockey_list,distance_list, stage_list,weight_list))
  #print(all_list)

#データの挿入
  # 1．DBに接続する
  con = sqlite3.connect(path + db_name)
  # print(type(con))
  # 2．SQLを実行するためのオブジェクトを取得
  cur = con.cursor()
  # 3．SQLを用意
  # データを挿入するSQL
  # INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
  sql_insert_many = "INSERT INTO arima VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
  # 4．SQLを実行
  cur.executemany(sql_insert_many, all_list)
  # 5．コミット処理（データ操作を反映させる）
  con.commit()
  # 6．DBへの接続を閉じる
  con.close()

  #DB内のデータ参照
# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))
# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．SQLを用意
# SELECT * FROM テーブル名;
# *の部分は取得したい列の名前をカンマ区切りで指定することもできる
sql_select = 'SELECT * FROM arima;'
# 4．SQLを実行
cur.execute(sql_select)
for r in cur:
  print(r)
# 6．DBへの接続を閉じる
con.close()