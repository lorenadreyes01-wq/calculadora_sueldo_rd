TSS = 0.0591
BONIFICACION = 0.10

# Constantes
def calcular_isr(sueldo):

    if sueldo <= 34685:
        return 0

    elif sueldo <= 52027:
        excedente = sueldo - 34685
        return excedente * 0.15

    elif sueldo <= 72260:
        excedente = sueldo - 52027
        return 2601.33 + (excedente * 0.20)

    else:
        excedente = sueldo - 72260
        return 6648 + (excedente * 0.25)


def main():

    print("=== CALCULADORA DE SUELDO RD ===\n")

    nombre = input("Ingrese su nombre: ")
    anos = int(input("Años en la empresa: "))
    sueldo = float(input("¿Cuánto gana al mes? RD$: "))
    
   
    otros_descuentos = float(input("Ingrese otros descuentos RD$: "))

    bono = input("¿Aplica bonificación este mes? (si/no): ").lower()
    doble = input("¿Hay doble sueldo este mes? (si/no): ").lower()

    seguridad_social = sueldo * TSS

    isr = calcular_isr(sueldo)

    bonificacion = 0
    if bono == "si":
        bonificacion = sueldo * BONIFICACION

    doble_sueldo = 0
    if doble == "si":
        doble_sueldo = sueldo

    
    sueldo_neto = sueldo - seguridad_social - isr - otros_descuentos + bonificacion + doble_sueldo

    print("\n===== RESULTADO =====")
    print("Empleado:", nombre)
    print("Años en empresa:", anos)

    print("\nSueldo Bruto:", sueldo)
    print("Seguridad Social:", round(seguridad_social,2))
    print("ISR:", round(isr,2))
    print("Otros descuentos:", round(otros_descuentos,2))
    print("Bonificación:", round(bonificacion,2))
    print("Doble sueldo:", doble_sueldo)

    print("\nSUELDO NETO:", round(sueldo_neto,2))


if __name__ == "__main__":
    main()