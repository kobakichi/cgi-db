import sqlite3
#データベースに接続、新規作成
con = sqlite3.connect('shop.db')
#カーソルの取得
cur = con.cursor()
#SQL文の実行 もしaccountテーブルが存在していたら削除する
cur.execute("DROP TABLE IF EXISTS account")
#accountテーブルの作成
cur.execute("CREATE TABLE account (user TEXT PRIMARY KEY, password TEXT)")
#変更を確定するcommit
#テーブルにデータ追加
account = [('suzuki', 'abc123'), ('satou', 'def456'), ('tanaka', 'ghi789')]

cur.executemany("INSERT INTO account VALUES (?, ?)", account)

con.commit()
con.close()