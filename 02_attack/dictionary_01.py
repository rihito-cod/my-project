import hashlib

def check_pass(pw,stolen_pw):
    for i in pw:
        temp_pw = hashlib.sha256(i.encode()).hexdigest()
        if temp_pw == stolen_pw:
            return "success"
    return "failed"

def open_file(path):
    with open(path,"r",encoding="latin-1") as f:
        reader = f.readlines()
        password_list = [row.strip() for row in reader]
    return password_list





