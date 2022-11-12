#!C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
import codecs,sys
import cgi
import goods

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()
#查詢
form = cgi.FieldStorage()
id=form.getvalue('id')
records = goods.getId(id)

id = str(id)
name = str(records[0][1])
price = str(records[0][2])
number = str(records[0][3])


with open("revise_Goods.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###id###",id.encode())
    st = st.replace(b"###name###",name.encode())
    st = st.replace(b"###price###",price.encode())
    st = st.replace(b"###number###",number.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()


