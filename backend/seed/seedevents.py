import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
from db import conn,cursor
cursor.execute("Select userid from users")
userid=[row[0] for row in cursor.fetchall()]
cursor.execute("Select productid from products")
productid=[row[0] for row in cursor.fetchall()]
eventtype=["view","addtocart","purchased"]
for _ in range(10000):
    
    cursor.execute("""INSERT INTO events (userid,productid,eventtype) values(%s,%s,%s)""",(random.choice(userid),
    random.choice(productid),random.choice(eventtype)))
print("events seeded")
conn.commit()
cursor.close()
conn.close()

    