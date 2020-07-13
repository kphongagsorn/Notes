from Crypto.Cipher import AES
import binascii, sys

key = "\x27\x46\x5F\xFD\x4C\xCC\x47\x72\xAB\xFD\xD6\x77\xCD\x98\xA0\xFD\x52\x4F\x3C\x11\x7A\xCC\x86\x25\x7B\xA9\x39\x21\xD7\xA1\x66\xD7"
iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

ts0001 = "b70235c3dbf3a83ef6d520d48e7cf65f60a56cc84bddba3ab15a65f2d31e345c06f7da6b13b27c22309380a901940b8d"
ts0002 = "10a380a57e0825fa7df7034d0dd96154babf00338103bbcca99854e80d2974bff12e333ba11efe4abc70b17fd6362bff"
ts0003 = "153fba4c0c5008770a123c72bdfb43e2c7abe3bfdb7e0d0172548da92c4f1538d83015de29e07867a92112cb9db4f3eb"

def decrypt(ciphertext):
	obj2 = AES.new(key, AES.MODE_CBC,iv)
	plaintext = obj2.decrypt(ciphertext)
	return plaintext

def main():
	print "decrypted bank credentials\n" + decrypt(binascii.unhexlify(ts0002))
	#print "decrypted ts0001.enc:\n" + decrypt(binascii.unhexlify(ts0001))
	#print "decrypted ts0002.enc:\n" + decrypt(binascii.unhexlify(ts0002))
	#print "decrypted ts0003.enc:\n" + decrypt(binascii.unhexlify(ts0003))

if __name__ == "__main__":
	main()