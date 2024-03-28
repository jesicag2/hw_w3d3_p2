# HW2_P2: Set Operations in Data Analysis

# Task 1: Duplicate Entries Cleanup
'''
You are given a list of customer IDs, some of which are duplicated. Write a Python 
script to remove duplicates and display the unique customer IDs.

Expected Outcome:
A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.
'''

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

set_customer_ids = set(customer_ids)
sorted_customer_ids = sorted(set_customer_ids)

print(sorted_customer_ids)
