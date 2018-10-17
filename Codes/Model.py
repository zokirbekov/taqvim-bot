import json
from pathlib import Path

class Vaqt(object):
    def __init__(self):
        self.Tong = ""
        self.Quyosh = ""
        self.Peshin = ""
        self.Asr = ""
        self.Shom = ""
        self.Xufton = ""

    def set(self, tong, quyosh, peshin, asr, shom, xufton):
        self.Tong = tong
        self.Quyosh = quyosh
        self.Peshin = peshin
        self.Asr = asr
        self.Shom = shom
        self.Xufton = xufton

    def getAll(self):
        return "Tong : " + self.Tong + "\n" \
               + "Quyosh : " + self.Quyosh + "\n" \
               + "Peshin : " + self.Peshin + "\n" \
               + "Asr : " + self.Asr + "\n" \
               + "Shom : " + self.Shom + "\n" \
               + "Xufton : " + self.Xufton



# class UserModel:
#     def __init__(self):
#         self.ID = id
#         pass
#     pass

class FileWorker:

    @staticmethod
    def addUser(file_name, user):
        users = FileWorker.getAllUser(file_name)
        users_list = []
        if isinstance(users,list):
            for i in users:
                users_list.append(i)

        users_list.append(user)
        json_text = json.dumps(users_list)
        FileWorker.writeToFile(file_name,json_text)
        print("User added : " + str(user))

    @staticmethod
    def getAllUser(file_name):
        with open(file_name, "r") as reader:
            try:
                users = json.load(reader)
            except Exception:
                return None
        return users

    @staticmethod
    def writeToFile(file_name, text):
        with open(file_name, 'w') as writer:
            writer.writelines(text)

    @staticmethod
    def createFile(file_name):
        my_file = Path(file_name)
        if not my_file.exists():
            with open(file_name,'w+') as writer:
                pass
