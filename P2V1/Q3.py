consumo = float(input("Informe o consumo de água em metros cúbicos (m³): "))

valor_total = 7 

if consumo > 10:
    valor_total += 20
if consumo > 30:
    valor_total += 140
if consumo > 100:
    valor_total += 100

print(f"O valor da conta de água para um consumo de {consumo} m³ é R$ {valor_total:.2f}")
