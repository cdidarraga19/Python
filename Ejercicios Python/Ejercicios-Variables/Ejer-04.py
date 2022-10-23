from datetime import date

def calcu_edad(fecha_naci):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_naci.year
    resultado -= ((fecha_actual.month, fecha_actual.day) <(fecha_naci.month, fecha_naci.day))
    return resultado

fecha_nacimiento = date(1999, 6, 9)
edad = calcu_edad(fecha_nacimiento)

print(f"La edad es de {edad} años. ")