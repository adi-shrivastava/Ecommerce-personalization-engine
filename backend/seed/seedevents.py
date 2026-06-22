import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
from db import conn,cursor
userid=cursor.execute("Select userid from users")
productid=cursor.execute("Select productid from products")
eventtype=["view","addtocart","purchased"]
for _ in range(10000):
    event=random.choice(eventtype)
    cursor.execute("INSERT INTO events (userid,productid,eventtype) values(%s,%s,%s)",random.choice(userid),
    random.choice(productid),event)
cursor.close()
conn.close()
    