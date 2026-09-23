import hashlib
import os

class Salt_pass:

    user_db = {}

    def __init__(self,user_name,pass_word):
        self.un = user_name
        self.pw = pass_word
        self.rock = False
        self.failed_count = 0
        self.hash_password_with_salt()

        Salt_pass.user_db[self.un] = {"salt":self.salt,
                                      "hash":self.hash}        

    def hash_password_with_salt(self):
        self.salt = os.urandom(16).hex()
        self.hash = hashlib.sha256((self.pw + self.salt).encode()).hexdigest()


    def login(self,user_name,pass_word):
        try:

            db = Salt_pass.user_db[user_name]
            hash_pass = hashlib.sha256((pass_word + db["salt"]).encode()).hexdigest()

            if hash_pass == db["hash"]:
                self.failed_count = 0
                return f"{user_name}:ログイン成功"
            else:
                self.failed_count += 1
                return f"{user_name}:ログイン失敗"

        except KeyError:
            self.failed_count += 1
            return "_____エラー_____ ユーザーネームを確認してください"

        finally:
            if self.failed_count > 4:
                raise AttributeError("このアカウントをロックしました")



salt = Salt_pass("rihito","443858")

print(salt.login("rihto","443858"))
print(salt.login("rihto","443858"))
print(salt.login("rihto","443858"))
print(salt.login("rihito","44858"))
print(salt.login("rihito","443858"))


