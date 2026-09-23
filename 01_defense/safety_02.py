import hashlib
import sys
from hash_test_01 import Hash
sys.path.append("/Users/hiromurarihito/Desktop/Cecurity/02_attack")
import dictionary_01



password = Hash.prompt()
hash_code = Hash(password)

print(hash_code.hash_pass)


input_pass = input("ハッシュ値を入力: ")


print(dictionary_01.check_pass(dictionary_01.open_file("/Users/hiromurarihito/Desktop/Cecurity/02_attack/rockyou.txt"),input_pass))