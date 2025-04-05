a = [1, 3, 1, 4, 2, 2, 1, 3, 1, 1, 1, 3, 4, 1, 2, 4, 1, 2, 4, 4, 0]

a1 = 0
a2 = 0
a3 = 0
a4 = 0

for voto in a:
    if voto == 0:
        break
    elif voto == 1:
        a1 += 1
    elif voto == 2:
        a2 += 1
    elif voto == 3:
        a3 += 1
    elif voto == 4:
        a4 += 1
    else:
        print(f"Voto inválido: {voto}")

total = a1 + a2 + a3 + a4

print(f"Candidato 1: {a1} votos ({a1 / total * 100}%)")
print(f"Candidato 2: {a2} votos ({a3 / total * 100}%)")
print(f"Candidato 3: {a3} votos ({a3 / total * 100}%)")
print(f"Candidato 4: {a4} votos ({a4 / total * 100}%)")

print(f"\nTotal de participantes: {total}")