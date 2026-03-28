# Sistema para calcular o consumo de energia por aparelho 

valor_kwh = 0.75

# Solicita os dados ao usuário

nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Calcula o consumo mensal (em kWh)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Calcula o custo estimado
custo_estimado = consumo_mensal * valor_kwh

# Exibe o resultado
print("\n--- Resultado ---")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
print(f"Custo estimado mensal: R$ {custo_estimado:.2f}")