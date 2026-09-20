import hashlib
def check_pass(pw,stolen_pw):
    for i in pw:
        temp_pw = hashlib.sha256(i.encode()).hexdigest()
        if temp_pw == stolen_pw:
            return "success"
    return "failed"


with open("password_file.txt","r",encoding="utf-8") as f:
    reader = f.readlines()
    password_list = [row.strip() for row in reader]

print(check_pass(password_list,"c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646"))
