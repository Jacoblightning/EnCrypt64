from cryptography.fernet import Fernet
import secrets
import pickle
import base64
import os
from os.path import exists, abspath


def MAXIMUM_ENCRYPT(message, encryptname):
    key = Fernet(base64.b64encode(bytes(secrets.token_urlsafe(64)[:32], "utf-8")))
    if exists(os.getcwd() + "\\" + encryptname + ".pickle"):
        raise FileExistsError(encryptname + ".pickle exists")
    with open(encryptname + ".pickle", "wb") as encryption:
        pickle.dump(key, encryption)
    return key.encrypt(message.encode())


def MAXIMUM_DECRYPT(message, encryptname, keep=False):
    if not exists(os.getcwd() + "\\" + encryptname + ".pickle"):
        raise FileNotFoundError(encryptname + ".pickle does not exist")
    with open(encryptname + ".pickle", "rb") as encryption:
        key = pickle.load(encryption)
    if not keep:
        os.remove(os.getcwd() + "\\" + encryptname + ".pickle")
    return key.decrypt(message).decode()
