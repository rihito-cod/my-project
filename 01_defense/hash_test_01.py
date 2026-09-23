import hashlib

def check_rock(func):
    def wrapper(self,*args,**kwargs):
        if self.rock:
            raise AttributeError("ログインできません")
        return func(self,*args,**kwargs)
    return wrapper

class Hash:
    def __init__(self,password):
        self.rock = False
        self.password = password
        self.MAX_ATTEMPTS = 5
        self.hashing()
    @check_rock
    def hashing(self):
        self._hash_pass = hashlib.sha256(self.password.encode()).hexdigest()
        return self._hash_pass

    @check_rock
    def plain_txt_show(self):
        return f"plain_txt {self.password}"

    @check_rock
    def judge(self):
        while True:
            password = hashlib.sha256(Hash.prompt().encode()).hexdigest()
            if password == self._hash_pass:
                return "success"
            if self.MAX_ATTEMPTS <= 0:
                self.rock = True
                print("ロックしました")
                return
            else:
                self.MAX_ATTEMPTS -= 1
                print(f"残り試行回数{self.MAX_ATTEMPTS}回")

    @property
    @check_rock
    def hash_pass(self):
        return f"ハッシュ化したパスワード:{self._hash_pass}"


    @staticmethod
    def prompt():
        while True:
            password = input("パスワードを入力")
            if password == "":
                continue
            else:
                break
        return password

