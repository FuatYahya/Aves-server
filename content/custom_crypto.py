from os import read
import random
from Crypto.Util import Counter
from Crypto.Cipher import AES


class Custom_cipher():
    def __init__(self):
        pass

    @staticmethod
    def get_counter(nonce):
        return Counter.new(128 - (len(nonce) * 8), prefix=nonce, initial_value=0)

    @staticmethod
    def get_cipher(key, mode, counter):
        return AES.new(key, mode=mode, counter=counter)

    @staticmethod
    def encrypt(key, nonce, in_file, out_file, callback):
        ctr = Custom_cipher.get_counter(nonce)
        cipher = Custom_cipher.get_cipher(key, AES.MODE_CTR, counter=ctr)
        callback("reading")
        with open(in_file, 'rb') as file:
            cipher_text = cipher.encrypt(file.read())

        with open(out_file, 'wb') as file:
            file.write(cipher_text)

        callback("finished")
    
    @staticmethod
    def decrypt(key, nonce, in_file, out_file, callback):
        ctr = Custom_cipher.get_counter(nonce)
        cipher = Custom_cipher.get_cipher(key, AES.MODE_CTR, counter=ctr)
        with open(in_file, 'rb') as file:
            cipher_text = cipher.decrypt(file.read())

        with open(out_file, 'wb') as file:
            file.write(cipher_text)
        
        callback("finished")

