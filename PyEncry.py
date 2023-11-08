import bcrypt
import rsa
import twofish

'''
Generalized convention:
encrypt - encryption function
decrypt/check - decryption function
info - input text
cipher - encrypted text
'''

'''
Bcrypt is basically a hash, it's good for info that we need to check but can't view
Things like passwords and stuff could work under this purely because we shouldn't be viewing them at all
It's virtually impossible to decrypt the hash also which makes it much better for privacy.
'''
class bcryptEncry:
    def encrypt(info):
        info = bytes(info, 'utf-32')
        salt = bcrypt.gensalt(rounds=15) #rounds mainly used for hashing itself
        cipher = bcrypt.hashpw(info, salt)
        return cipher
    def check(info, cipher):
        info = bytes(info, 'utf-32')
        flag = bcrypt.checkpw(info, cipher)
        return flag #0 for dissimilar, 1 for similar

'''
Twofish is the symmetric encryption that we can use for things like the chatbot and such
It's symmetric so either user can encrypt or decrypt with this
That way, the entire process can be automated purely down to the text.
Both sides can read, encrypt, decrypt and reply.

bs - block size
'''       
class tfEncry:
    bs = 32
    info = ''
    key = ''
    T = twofish.Twofish(str.encode(key)) 
    def __init__(self, size, info, key) -> None:
        self.bs = size
        self.info = bytes(info, 'utf-32') 
        self.key = key
    
    def encrypt(info, bs, key, T):
        if info == '' or key == '':
            print('Cannot encrypt empty string')
            return -1
        if len(info)%bs:
            padded = str(info+'%'*(bs-len(info)%bs)).encode('utf-32')
        else:
            padded = str(info).encode('utf-32')
        cipher = b''
        for i in range(int(len(padded)/bs)):
            cipher += T.encrypt(padded[i*bs: (i+1)*bs])
        return cipher
    
    def decrypt(cipher, key, bs, T):
        plain = b''
        for i in range(int(len(cipher)/bs)):
            plain += T.decrypt(cipher[i*bs: (i+1)*bs])
        info = str.encode(plain.decode('utf-32').strip('%'))
        return info
'''
RSA is our assymetric storage based algo
It's useful for longtime storage of any data and is the hardest to break through
It's also slower than Patrick's pet rock from Spongebob
Best case use is data that needs to be stored and periodically checked

pubKey - public key
privKey - private key
'''    
class rsaEncrypt:
    def encrypt(pubKey, info):
        cipher = rsa.encrypt(info.encode('utf-32'))
        return cipher
    
    def decrypt(privKey, cipher):
        info = rsa.decrypt(cipher, privKey)
        return info
    

