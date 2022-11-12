# !C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
# 連線DB
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select id, goods_name,goods_price, number from goods where number>0 order by number desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delgoods(id):
    sql="delete from goods where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def addgoods(name,price,number):
    sql="insert into goods (goods_name,goods_price,number) values (%s,%s,%s);"
    cur.execute(sql,(name,price,number))
    conn.commit()
    return True

def getId(id):
    sql="select id, goods_name,goods_price, number from goods where id = %s"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records

def revise(id,name,price,number):
    sql = "update goods set goods_name=%s,goods_price=%s,number=%s where id=%s;"
    cur.execute(sql,(name,price,number,id))
    conn.commit()
    return True

# 結帳後庫存減少
def reduce(records):
    for record in records:
        sql = "update goods set number=number-%s where id = %s;"
        cur.execute(sql,(record[1],record[0]))
        conn.commit()

