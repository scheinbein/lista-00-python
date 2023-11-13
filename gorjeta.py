def main():
    dollars = dollars_to_float(input("Quanto custou a refeição? "))
    percent = percent_to_float(input("Qual porcentagem você deseja dar de gorjeta? "))
    tip = dollars * percent
    print(f"Deixe uma gorjeta de ${tip:.2f}")

def dollars_to_float(d):
    # Remove o símbolo "$", se presente, e converte a string em float
    if '$' in d:
        d = d.replace('$', '')
    return float(d)

def percent_to_float(p):
    # Remove o símbolo "%", se presente, e converte a porcentagem em float
    if '%' in p:
        p = p.replace('%', '')
    return float(p) / 100  # Divida por 100 para obter a representação decimal da porcentagem

main()

