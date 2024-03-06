
lampadas = [False, False, False]

def verifica_lampadas(lampadas):
    for i in range(len(lampadas)):
        print("Lâmpada", i+1, ":", "Acesa" if lampadas[i] else "Apagada")

for i in range(len(lampadas)):
    lampadas[i] = True

print("Primeira verificação:")
verifica_lampadas(lampadas)

for i in range(len(lampadas)):
    lampadas[i] = False

lampadas[0] = True

print("\nSegunda verificação:")
verifica_lampadas(lampadas)
