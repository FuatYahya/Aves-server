from Crypto.Util import Counter
from Crypto.Cipher import AES
import os, sys, time


class Custom_cipher():
    MODE_ENCRYPT = 1
    MODE_DECRYPT = 2
    BUFFER = 1024

    def __init__(self):
        pass

    @staticmethod
    def get_counter(nonce):
        return Counter.new(128 - (len(nonce) * 8), prefix=nonce, initial_value=0)

    @staticmethod
    def get_cipher(key, mode, counter):
        return AES.new(key, mode=mode, counter=counter)

    @staticmethod
    def do_cipher(cipher, mode, in_file, out_file, callback):
        try:
            # Remove file if it existes because we are appending to it
            if os.path.exists(out_file):
                os.remove(out_file)
            size = os.path.getsize(in_file)

            callback("Opening streams...")
            input_stream = open(in_file, 'rb')
            ouput_stream = open(out_file, 'ab')
            
            # read bytes length of 16 from in_file, cipher them and append cipher bytes to out_file 
            c = 0;
            while True:
                bytes = input_stream.read(Custom_cipher.BUFFER)
                if bytes == b'':
                    break
                if mode == Custom_cipher.MODE_ENCRYPT:
                    ouput_stream.write(cipher.encrypt(bytes))
                elif mode == Custom_cipher.MODE_DECRYPT:
                    ouput_stream.write(cipher.decrypt(bytes))
                callback(message='Ciphering', val=c, end=size, t='progress')
                c += Custom_cipher.BUFFER
        finally:
            callback("Closing streams...", t='text')
            input_stream.close()
            ouput_stream.close()

    @staticmethod
    def encrypt(key, nonce, in_file, out_file, callback):
        ctr = Custom_cipher.get_counter(nonce)
        cipher = Custom_cipher.get_cipher(key, AES.MODE_CTR, counter=ctr)
        Custom_cipher.do_cipher(cipher, Custom_cipher.MODE_ENCRYPT, in_file, out_file, callback)

    
    @staticmethod
    def decrypt(key, nonce, in_file, out_file, callback):
        ctr = Custom_cipher.get_counter(nonce)
        cipher = Custom_cipher.get_cipher(key, AES.MODE_CTR, counter=ctr)
        Custom_cipher.do_cipher(cipher, Custom_cipher.MODE_DECRYPT, in_file, out_file, callback)

def console_log(message, val=0, end=0, t=''):
    if t == 'progress':
        progressBar(message, value=val, endvalue=end)
        return
    sys.stdout.write(f'{message}\n')
    sys.stdout.flush()

def progressBar(message, value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\r{0}: [{1}] {2}%".format(message, arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()


key = b'abebe beso bela.'
nonce = 'chala ha'
in_file = '/home/jordan/Documents/Projects/openssl/enc-django.aves'
out_file = '/home/jordan/Documents/Projects/openssl/dec-django.aves'

Custom_cipher.decrypt(key, nonce, in_file, out_file, console_log)


