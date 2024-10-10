#!/usr/bin/env python3
"""
This script tests the add function from the 0-add module.
"""
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
