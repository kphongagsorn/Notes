from Crypto.Cipher import AES
import binascii, sys

key = ""
iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" #16 bytes

# cipher text
ts0001 = ""
ts0002 = ""
ts0003 = ""

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
