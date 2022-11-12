#!C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
import codecs,sys
import cgi
import goods
from dbConfig import conn, cur

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

sql="select id, goods_name,goods_price, number from goods order by number desc;"
cur.execute(sql)
goodsList = records = cur.fetchall()

msg = ""
for (id,goods_name, goods_price, number) in goodsList:
	msg = msg + f"<tr><td>編號 : {id}</td> <td>商品 : {goods_name}</td> <td>商品價格 : {goods_price}</td> <td>庫存 : {number}</td> </tr>" 

with open("manage.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()