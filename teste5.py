interruptores = {1: "Desconhecido", 2: "Desconhecido", 3: "Desconhecido"}
lâmpadas = {"A": "Desconhecida", "B": "Desconhecida", "C": "Desconhecida"}

interruptores[1] = "Desligado (mas estava ligado por 5 minutos)"
interruptores[2] = "Ligado"
interruptores[3] = "Desligado"

lâmpadas["A"] = "Acesa (controle pelo interruptor 2)"
lâmpadas["B"] = "Apagada e quente (controle pelo interruptor 1)"
lâmpadas["C"] = "Apagada e fria (controle pelo interruptor 3)"

for i in range(1, 4):
    print(f"Interruptor {i}: {interruptores[i]}")

for lâmpada, status in lâmpadas.items():
    print(f"Lâmpada {lâmpada}: {status}")