from db_1 import Database
db1 = Database('Tpk.db')
import time
def BASE_UESR_ID():
    qwe = db1.col_id()
    masiv = qwe.fetchall()
    i2 = []
    for i in masiv:
        c = str(i)
        i2.append(c)

    return i2

def BSD():
    MASIV = []
    for bcf in BASE_UESR_ID():
        MASIV.append(bcf)
    return MASIV
def con12(x):
    mas = []

    for qw in db1.cou_id_2(x):
        o = str(qw)
        mas.append(o)
    return mas

def CON(x):
    mas = []

    for qw in db1.cou_id_3(x):
        o = str(qw)
        mas.append(o)
    return mas

#def STEPI(x):
def TIMING():
    for i in range(30):
        time.sleep(1)
