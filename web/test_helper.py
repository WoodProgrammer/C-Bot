from helper import hash_file_name
import hashlib

hash_example_str = "TESTFILENAME"
def test_parse_function():
    assert hashlib.sha224(hash_example_str.encode('utf-8')).hexdigest() == hash_file_name(hash_example_str)
