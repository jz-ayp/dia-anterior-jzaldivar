"""
Cadena de documentación.
"""

from dia_siguiente import es_bisiesto, dias_del_mes

def main():
    # Entradas
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anho = int(input("Año: "))

    # Proceso
    # Restarle uno al día y si da cero,
    # se trataría del último día del mes anterior.
    dia -= 1
    if dia == 0:
        mes -= 1
        if mes == 0:
            mes = 12
            anho -= 1
        dia = dias_del_mes(mes, anho)
    
    # Salidas
    print(dia)
    print(mes)
    print(anho)

if __name__ == "__main__":
    main()