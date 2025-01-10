def inverter_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1): 
        invertida += string[i]
    return invertida


string = input("Informe uma string para inverter: ")

resultado = inverter_string(string)
print(f"String invertida: {resultado}")
