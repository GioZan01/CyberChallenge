m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"


a = bytes.fromhex(m1)
b = bytes.fromhex(m2)

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

print(xor(a,b))
