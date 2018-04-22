from helper import parse_function
import os

input = "def hebele(): \n print('hello') "
file = open('test_parse_method.py','w+')
def test_parse_function():

    data = parse_function(input)
    file.write(data)
    file.close()
