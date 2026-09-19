import hashlib

class Hash:
    def __init__(self,password):
        self.password = password

    def hashing(self):
        self.hash_pass = hashlib.sha256(self.password.encode()).hexdigest()
        return self.hash_pass

    def plain_txt_show(self):
        return f"plain_txt{self.hash_pass}"

    def judge(self):
        while True:
            password = hashlib.sha256(Hash.prompt().encode()).hexdigest()
            if password == self.hash_pass:
                return "success"
            else:
                return "failed"
    
    @staticmethod
    def prompt():
        while True:
            password = input("パスワードを入力")
            if password == "":
                continue
            else:
                break
        return password



password = Hash.prompt()
hash_code = Hash(password)
hash_code.hashing()
print(hash_code.judge())