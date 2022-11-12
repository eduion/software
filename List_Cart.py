#!C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
import codecs,sys
import cgi
import cart



print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

cartList = cart.getList()
msg = ""
for (id,cart_name, cart_price, count) in cartList:
	msg = msg + f"<tr><td>編號 : {id}</td> <td>商品 : {cart_name}</td> <td>商品價格 : {cart_price}</td> <td>購買數量 : {count}</td> </tr>" 

with open("List_Cart.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###cart_msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()