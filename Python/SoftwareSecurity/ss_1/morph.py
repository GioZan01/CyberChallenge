lista="47 43 9b 16 2d 52 1e 94 db 13 11 11 f8 b6 13 11 11 74 70 a8 25 1e 6b 2d a7 9b 20 22 22 cb b4 20 22 22 65 61 b9 34 0f 67 3c b6 9b 31 33 33 da b6 31 33 33 12 16 ce 43 78 3f 4b c1 d3 46 44 44 ad 30 46 44 44 03 07 df 52 69 3c 5a d0 d3 57 55 55 bc 36 57 55 55 30 34 ec 61 5a 12 69 e3 13 64 66 66 8f 34 64 66 66 21 25 fd 70 4b 0d 78 f2 13 75 77 77 9e 36 75 77 77 de da 02 8f b4 d7 87 0d db 8a 88 88 61 b8 8a 88 88 cf cb 13 9e a5 f4 96 1c db 9b 99 99 70 86 9b 99 99 fc f8 20 ad 96 9a a5 2f 9b a8 aa aa 43 a4 a8 aa aa ed e9 31 bc 87 c9 b4 3e 9b b9 bb bb 52 46 ba bb bb 9a 9e 46 cb f0 bc c3 49 c3 ce cc cc 25 20 cd cc cc 8b 8f 57 da e1 b5 d2 58 23 dc dd dd 34 06 dc dd dd b8 bc 64 e9 d2 b1 e1 6b 03 ef ee ee 07 24 ef ee ee a9 ad 75 f8 c3 cc f0 7a 23 fe ff ff 16 46 fe ff ff 46 42 9a 17 2c 24 1f 95 db 11 10 10 f9 b8 11 10 10 77 73 ab 26 1d 62 2e a4 9b 20 21 21 c8 b6 20 21 21 64 60 b8 35 0e 01 3d b7 9b 33 32 32 db b4 33 32 32 15 11 c9 44 7f 62 4c c6 db 42 43 43 aa 36 42 43 43 02 06 de 53 68 75 5b d1 d3 55 54 54 bd 30 55 54 54 33 37 ef 62 59 44 6a e0 13 64 65 65 8c 36 64 65 65 20 24 fc 71 4a 0b 79 f3 13 77 76 76 9f 34 77 76 76"

lista=lista.split(" ")
flag='C'
for i in range(22):
	flag += (chr(int((lista[5+17*i]),16)^(17*(i+1))%256))
print(flag)
