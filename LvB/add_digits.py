def f(Nx):
    Sx = str(Nx)
    RV = 0
    for sx in Sx:
        RV += int(sx) 
    return RV

def g(Ny):
    if Ny < 10:
        return Ny
    else:
        return g(f(Ny))

k = eval(input())
for i in range(k):
    s = int(input())
    print(g(s))