import csv
def valid(file):
    with open(file,"r") as f:
        r=csv.DictReader(f)
        order_ids = [row["order_id"] for row in r]

    return len(order_ids) == len(set(order_ids))


'''
# validator.py
import csv

def valid(file):
    with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        order_ids = [row["order_id"] for row in reader]
        d=len(order_ids) == len(set(order_ids))
    return d

import os
print(os.getcwd())

import csv

def valid(file):
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        order_ids = [row["order_id"] for row in reader]

    return len(order_ids) == len(set(order_ids))'''