# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:17:59 2019

@author: RayomandVatcha
"""
import base64
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

if __name__ == '__main__':
    sec = AESCipher("1234567890123456")
    Bytes =  'A' * 10
    eA = sec.encrypt(Bytes)
    print(eA)

    secR = AESCipher("1234567890123456")
    print(secR.decrypt(eA))