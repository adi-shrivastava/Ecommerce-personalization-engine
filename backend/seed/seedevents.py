import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
from db import conn,cursor
eventtype=["view","addtocart","purchased"]
for _ in range(10000):
    event=random.choice(eventtype)
    