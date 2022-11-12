# !C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe連線DB
# 連線DB
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select id, cart_name,cart_price, count from cart where count>0 order by count desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delcart(id):
    sql="update cart set count=0 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

# 判斷貨品是否已在購物車 不在的話就要添加
def exist(id):
    sql = "select id,cart_price from cart where id = %s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records

def addcart(id):
    if exist(id) ==  []:
        sql = "select id,goods_name,goods_price from goods where id = %s;"
        cur.execute(sql,(id,))
        records = cur.fetchall()
        i = records[0][0]
        name = records[0][1]
        price = records[0][2]
        sql2="insert into cart (id,cart_name,cart_price,count) values (%s,%s,%s,1);"
        cur.execute(sql2,(i,name,price))
        conn.commit()
    else:
        sql="update cart set count=count+1 where id=%s;"
        cur.execute(sql,(id,))
        conn.commit()
    return True

def buy():
    money = 0
    records = []
    sql = "select id, cart_name,cart_price, count from cart where count>0;"
    cur.execute(sql)
    lists = cur.fetchall()
    for list in lists:
        tmp = []
        money = money + list[2] * list[3]
        tmp.append(list[0])
        tmp.append(list[3])
        records.append(tmp)
    sql2 = "Delete from cart;"
    cur.execute(sql2)
    conn.commit()
    return money,records
