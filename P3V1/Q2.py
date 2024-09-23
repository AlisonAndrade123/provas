N = int(input('Digite um número: '))
positivos = 0
cont = 0
for i in range(N):
    N_v = int(input('Digite os número: '))
    if N_v > 0:
        positivos += 1
        cont += N_v

media = cont / positivos

print(positivos)
print(f'{media:.1f}')