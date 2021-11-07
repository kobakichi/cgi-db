#!/usr/bin/env python3
import sqlite3
import sys
import cgi
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

#フォームを受け取る時に使う
form = cgi.FieldStorage()
#htmlのformタグ、user,passwordから入力内容を受け取る
user = form.getfirst('user')
password = form.getfirst('password')

con = sqlite3.connect('shop.db')
cur = con.cursor()

cur.execute("SELECT * FROM account WHERE user=? AND password=?", (user, password))

result = 'ログインが成功しました。' if list(cur) else 'ログインに失敗しました。'
con.close()

print(f'''
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>リザルト</title>
</head>
<body>
  {result}
</body>
</html>
''')