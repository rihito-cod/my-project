import hashlib
password = input("パスワードを入力")
print(f"base_pass: {password}")
password_bytes = password.encode()
password_sha256 = hashlib.sha256(password_bytes)
hex_password = password_sha256.hexdigest()
print(f"result_pass: {hex_password}")
input_pass = input("パスワードを入力")
if hashlib.sha256(input_pass.encode()).hexdigest() == hex_password:
    print("success")
else:
    print("failed")