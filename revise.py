#!C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import goods


#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>revise</title>
</head>
<body>
""")

form = cgi.FieldStorage()
id=form.getvalue('id')

records = goods.getId(id)

old_name = records[0][1]
old_price = records[0][2]
old_number = records[0][3]

name=form.getvalue('name')
price=form.getvalue('price')
number=form.getvalue('number')

if name == None:
    name = old_name
if price == None:
    price = old_price
if number == None:
    number = old_number

goods.revise(id,name,price,number)
print("商品已修改!")

print("<br><a href='manage.py'>回庫存清單</a>")
print("</body></html>")

