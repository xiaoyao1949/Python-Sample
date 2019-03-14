from pymysql import *
def main():
    conn = connect(host="172.21.114.172",
                   user="root",
                   passwd="qaz_1880_WSX",
                   db="test",
                   port=3306,
                   charset='utf8')
    cur = conn.cursor()  # 数据库链接对象
    sql = "select OFFERUNIT from T_PRODUCT"
    print(sql)
    res = cur.execute(sql)
    print(res)
    print(cur.fetchall)
    cur.close()
main()

