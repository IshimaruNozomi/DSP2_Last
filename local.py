# -*- coding: utf-8 -*-
import sqlite3
#DBファイルを保存するためのファイルパス
#Google Colab
path = '/Users/nozomi0407/DSP2_Last'

#DBファイル名
db_name = 'arima_local.sqlite'
#DBに接続する（指定したファイルが存在しない場合は新規に作成される）
con = sqlite3.connect(path + '/' + db_name)
#DBへの接続を閉じる
con.close()
#１.DBに接続する
con = sqlite3.connect(path + '/' + db_name)
#print(type(con))
#２.SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．実行したいSQLを用意する
# テーブルを作成するSQL
sql_create_table_arima_local = 'CREATE TABLE arima_local(r1name text, r2name text, r3name text);'
# 4．SQLを実行する
cur.execute(sql_create_table_arima_local)
# 5．必要があればコミットする（データ変更等があった場合）
# 6．DBへの接続を閉じる
con.close()

#データの挿入
# 1．DBに接続する
con = sqlite3.connect(path + '/' + db_name)
# print(type(con))
# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO arima_local VALUES (?, ?, ?);" 
data_into = [("ジャスティンパレス", "ジャスティンパレス", "タイトルホルダー"),("ヒートオンビート", "シャフリヤール", "アイアンバローズ"),("ハーパー", "シャフリヤール", "シャフリヤール"),("タスティエーラ", "ドウデュース", "スターズオンアース"),("タイトルホルダー", "アイアンバローズ", "ドウデュース"),("ディープボンド", "ハーパー", "ウインマリリン"),("タイトルホルダー", "タスティエーラ", "スターズオンアース"),("ディープボンド", "ドウデュース", "スターズオンアース"),("ディープボンド", "シャフリヤール", "ドウデュース"),("ジャスティンパレス", "スルーセブンシーズ", "スターズオンアース"),("ディープボンド", "スターズオンアース", "ソールオリエンス"),("スターズオンアース", "ジャスティンパレス", "タスティエーラ"),("スターズオンアース", "タイトルホルダー", "ジャスティンパレス"),("ホウオウエミーズ", "ライラック", "ジャスティンパレス"),("シャフリヤール", "タイトルホルダー", "ソールオリエンス"),("スターズオンアース", "ハーパー", "アイアンバローズ"),("タイトルホルダー", "ジャスティンパレス", "ドウデュース"),("スターズオンアース", "ジャスティンパレス", "ドウデュース")]

# 4．SQLを実行 
cur.executemany(sql_insert_many,data_into)
# 5．コミット処理（データ操作を反映させる）
con.commit()
# 6．DBへの接続を閉じる
con.close()
#DB内のデータ参照
# 1．DBに接続する
con = sqlite3.connect(path + '/' + db_name)
# print(type(con))
# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．SQLを用意
# SELECT * FROM テーブル名;
# *の部分は取得したい列の名前をカンマ区切りで指定することもできる
sql_select = 'SELECT * FROM arima_local;'
# 4．SQLを実行
cur.execute(sql_select)
for r in cur:
  print(r)
# 6．DBへの接続を閉じる
con.close()