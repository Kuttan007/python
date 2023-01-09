""" Initialize dictionary with default values

In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

Expected o/p
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""

#!/usr/bin python3
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)


print(res["Kelly"])
