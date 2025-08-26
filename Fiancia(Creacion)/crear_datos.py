# simular_datos.py
import random
import csv

def generar_datos():
    Ingreso_mensual = random.randint(600000, 2000000)  # ingreso mensual
    Balance = random.randint(-300000, int(Ingreso_mensual * 0.3))  # entre 0 y 30% del ingreso
    Ahorro_total = random.randint(Balance, Balance + 600000)  # acumulado

    # Gastos necesarios
    Gasto_viveres = random.randint(int(Ingreso_mensual * 0.15), int(Ingreso_mensual * 0.35))
    Gasto_renta = random.randint(int(Ingreso_mensual * 0.2), int(Ingreso_mensual * 0.4))
    Gasto_electricidad = random.randint(30000, 80000)
    Gasto_agua = random.randint(20000, 70000)

    # Subimportantes
    Gasto_transporte = random.randint(50000, 110000)
    Gasto_educacion = random.randint(0, 100000)
    Gasto_equipamiento_mantenimiento_hogar = random.randint(0, 80000)
    Gasto_gas = random.randint(5000, 20000)

    # Secundarios
    Gasto_ocio = random.randint(0, 100000)
    Gasto_aficcion = random.randint(0, 80000)

    # Otros
    gastos_indefinidos = random.randint(0, 100000)
    deudas = random.randint(0, 300000)
    suscripciones = random.randint(2000, 15000)
    pagos_tarjeta = random.randint(10000, 150000)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def generar_datos_1():
    typecd = random.randint(1,3)

    if typecd == 1: #Ingreso bajo
        x = random.randint(600000, 800000)
    else: x = random.randint(800000, 1000000)
    Ingreso_mensual = x  # ingreso mensual

    if typecd == 2: #Balance negativo
        x = random.randint(-400000, -200000)
        y = random.randint(x, x + 200000)
    else: y = random.randint(-100000, int(Ingreso_mensual * 0.3))
    Balance = y # entre 0 y 30% del ingreso
    Ahorro_total = y  # acumulado

    if typecd == 3:
        exp = 0.20
    else: exp = 0
    # Gastos necesarios

    Gasto_viveres = random.randint(200000, 550000 + round(550000*exp))
    Gasto_renta = random.randint(int(Ingreso_mensual * 0.2), int(Ingreso_mensual * 0.4))
    Gasto_electricidad = random.randint(80000, 120000 + round(120000*exp))
    Gasto_agua = random.randint(35000, 90000 + round(90000*exp))

    # Subimportantes
    Gasto_transporte = random.randint(80000, 150000 + round(150000*exp))
    Gasto_educacion = random.randint(0, 100000 + round(100000*exp))
    Gasto_equipamiento_mantenimiento_hogar = random.randint(0, 120000 + round(120000*exp))
    Gasto_gas = random.randint(35000, 120000 + round(120000*exp))

    # Secundarios
    Gasto_ocio = random.randint(35000, 100000)
    Gasto_aficcion = random.randint(35000, 80000)

    # Otros
    gastos_indefinidos = random.randint(35000, 100000)
    deudas = random.randint(35000, 300000)
    suscripciones = random.randint(35000, 60000)
    pagos_tarjeta = random.randint(10000, 150000)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def generar_datos_2():
    typecd = random.randint(1,3)

    if typecd==1: x=random.randint(1400000, 1800000)
    else: x=random.randint(1400000, 1600000)
    Ingreso_mensual = x # ingreso mensual

    if typecd==1: x = random.randint(0, int(Ingreso_mensual * 0.3))
    else: x = random.randint(-150000, int(Ingreso_mensual * 0.3))

    Balance = x  # entre 0 y 30% del ingreso
    Ahorro_total = random.randint(Balance, Balance + 600000)  # acumulado

    # Gastos necesarios
    if typecd == 3:
        exp = 0.20
    else: exp = 0

    Gasto_viveres = random.randint(200000, 450000 - round(450000*exp))
    Gasto_renta = random.randint(300000, 450000 - round(450000*exp))
    Gasto_electricidad = random.randint(30000, 80000 - round(80000*exp))
    Gasto_agua = random.randint(20000, 70000 - round(70000*exp))

    # Subimportantes
    Gasto_transporte = random.randint(50000, 110000 - round(110000*exp))
    Gasto_educacion = random.randint(0, 100000 - round(100000*exp))
    Gasto_equipamiento_mantenimiento_hogar = random.randint(0, 120000 - round(120000*exp))
    Gasto_gas = random.randint(5000, 20000 - round(20000*exp))

    # Secundarios
    Gasto_ocio = random.randint(0, 100000)
    Gasto_aficcion = random.randint(0, 80000)

    # Otros
    gastos_indefinidos = random.randint(0, 100000)
    deudas = random.randint(0, 300000)
    suscripciones = random.randint(2000, 15000)
    pagos_tarjeta = random.randint(10000, 150000)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def generar_datos3():
    pass

def codigo_1():
    Ingreso_mensual = random.randint(600, 800)  # Min 600 MAX 800  dif 0.75


    Balance = random.randint(-300, 100) #MIN -200 MAX +100
    Ahorro_total = random.randint(Balance, Balance + 100)  

    # Gastos1 Min 425
    Gasto_viveres = random.randint(150, 265) #0,35
    Gasto_renta = random.randint(150, 265) #0,35
    Gasto_electricidad = random.randint(75, 265) #0,18
    Gasto_agua = random.randint(50, 70) #0,12

    # Gastos 2 Min 330
    Gasto_transporte = random.randint(100, 175)
    Gasto_educacion = random.randint(30, 60)
    Gasto_equipamiento_mantenimiento_hogar = random.randint(150, 265)
    Gasto_gas = random.randint(50, 80)

    # Secundarios Min 100
    Gasto_ocio = random.randint(50, 80)
    Gasto_aficcion = random.randint(50, 80)

    # Otros Min 200
    gastos_indefinidos = random.randint(50, 80)
    deudas = random.randint(50, 80)
    suscripciones = random.randint(50, 80)
    pagos_tarjeta = random.randint(50, 80)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def detonar_gon():
    pass

def codigo_2():
    xd = random.randint(2,2)
    if xd==1: aum1 = 1.25
    else: aum1 = 0

    if xd==2: 
        aum2 = 3.5
        aum1 = -0.4
        aum3 = -0.3
    else: aum2 = 1

    if xd==3: 
        aum3 = 6
        aum4 = 25
    else: 
        aum3 = 0
        aum4 = 0

    Ingreso_mensual = random.randint(600, 800)  # Min 600 MAX 800 


    Balance = random.randint(-100, 100) #MIN -100 MAX +100
    Ahorro_total = random.randint(Balance+600, Balance + 800) #Min 200 Max +400

    # Gastos1 Min 330 MAX 440 (1 = 600)
    Gasto_viveres = random.randint(115 + round(115*aum1), 154+ round(154*aum1))
    Gasto_renta = random.randint(115 + round(115*aum1), 154+ round(154*aum1))
    Gasto_electricidad = random.randint(60 + round(60*aum1), 80 +  round(80*aum1))
    Gasto_agua = random.randint(40 + round(40*aum1), 52 +  round(52*aum1)) 

    # Gastos 2 Min 180 MAX 240 (2 = 600)
    Gasto_transporte = random.randint(58 * round(aum2), 77 * round(aum2))
    Gasto_educacion = random.randint(14 * round(aum2), 19 * round(aum2))
    Gasto_equipamiento_mantenimiento_hogar = random.randint(81 * round(aum2), 108 * round(aum2))
    Gasto_gas = random.randint(27 * round(aum2) , 36 * round(aum2))

    # Secundarios Min 90 MAX 120 (3 = 600)
    Gasto_ocio = random.randint(45 + round(45*aum3), round(80 + 80*aum3))
    Gasto_aficcion = random.randint(45 + round(45*aum3), 80 + round(80*aum3))

    # Otros Min 30 MAX 40 
    gastos_indefinidos = random.randint(8 + round(8*aum4), 10 + round(10*aum4))
    deudas = random.randint(10 + round(10*aum4), 14 + round(14*aum4))
    suscripciones = random.randint(6 + round(6*aum4), 8 + round(8*aum4))
    pagos_tarjeta = random.randint(6 + round(6*aum4), 8 + round(8*aum4))

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def codigo_3():
    Ingreso_mensual = random.randint(600, 800)  # Min 600 MAX 800  dif 0.75


    Balance = random.randint(-100, 100) #MIN -100 MAX +100
    Ahorro_total = random.randint(Balance+300, Balance + 600) #Min 200 Max +400

    # Gastos1 Min 330 MAX 440
    Gasto_viveres = random.randint(115, 154)
    Gasto_renta = random.randint(115, 154)
    Gasto_electricidad = random.randint(60, 80)
    Gasto_agua = random.randint(40, 52)

    # Gastos 2 Min 180 MAX 240
    Gasto_transporte = random.randint(58, 77)
    Gasto_educacion = random.randint(14, 19)
    Gasto_equipamiento_mantenimiento_hogar = random.randint(81, 108)
    Gasto_gas = random.randint(27, 36)

    # Secundarios Min 90 MAX 120
    Gasto_ocio = random.randint(45, 80)
    Gasto_aficcion = random.randint(45, 80)

    # Otros Min 30 MAX 40
    gastos_indefinidos = random.randint(8, 10)
    deudas = random.randint(10, 14)
    suscripciones = random.randint(6, 8)
    pagos_tarjeta = random.randint(6, 8)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]

def codigo_4():
    Ingreso_mensual = random.randint(800, 1000)  # Min 600 MAX 800  dif 0.75


    Balance = random.randint(-200, 100) #MIN -100 MAX +100
    Ahorro_total = random.randint(Balance+200, Balance + 400) #Min 200 Max +400

    # Gastos1 Min 400 MAX 500
    Gasto_viveres = random.randint(140, 165)
    Gasto_renta = random.randint(140, 155)
    Gasto_electricidad = random.randint(72, 85)
    Gasto_agua = random.randint(48, 55)

    # Gastos 2 Min 200 MAX 250
    Gasto_transporte = random.randint(64, 75)
    Gasto_educacion = random.randint(16, 20)
    Gasto_equipamiento_mantenimiento_hogar = random.randint(90, 110)
    Gasto_gas = random.randint(30, 35)

    # Secundarios Min 120 MAX 150
    Gasto_ocio = random.randint(60, 75)
    Gasto_aficcion = random.randint(60, 75)

    # Otros Min 40 MAX 50
    gastos_indefinidos = random.randint(10, 12)
    deudas = random.randint(10, 12)
    suscripciones = random.randint(10, 12)
    pagos_tarjeta = random.randint(10, 12)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]



def codigo_5():
    Ingreso_mensual = random.randint(1000, 1200)  # Min 600 MAX 800  dif 0.75


    Balance = random.randint(-100, 100) #MIN -100 MAX +100
    Ahorro_total = random.randint(Balance+300, Balance + 600) #Min 200 Max +400

    # Gastos1 Min 330 MAX 440
    Gasto_viveres = random.randint(115, 154)
    Gasto_renta = random.randint(115, 154)
    Gasto_electricidad = random.randint(60, 80)
    Gasto_agua = random.randint(40, 52)

    # Gastos 2 Min 180 MAX 240
    Gasto_transporte = random.randint(58, 77)
    Gasto_educacion = random.randint(14, 19)
    Gasto_equipamiento_mantenimiento_hogar = random.randint(81, 108)
    Gasto_gas = random.randint(27, 36)

    # Secundarios Min 90 MAX 120
    Gasto_ocio = random.randint(45, 80)
    Gasto_aficcion = random.randint(45, 80)

    # Otros Min 30 MAX 40
    gastos_indefinidos = random.randint(8, 10)
    deudas = random.randint(10, 14)
    suscripciones = random.randint(6, 8)
    pagos_tarjeta = random.randint(6, 8)

    return [
        Ingreso_mensual, Balance, Ahorro_total,
        Gasto_viveres, Gasto_renta, Gasto_electricidad, Gasto_agua,
        Gasto_transporte, Gasto_educacion, Gasto_equipamiento_mantenimiento_hogar, Gasto_gas,
        Gasto_ocio, Gasto_aficcion, gastos_indefinidos, deudas, suscripciones, pagos_tarjeta
    ]




def guardar_datos_csv(nombre_archivo, cantidad):
    list = [
        "Ingreso_mensual", "Balance", "Ahorro_total",
        "Gasto_viveres", "Gasto_renta", "Gasto_electricidad", "Gasto_agua",
        "Gasto_transporte", "Gasto_educacion", "Gasto_equipamiento_mantenimiento_hogar", "Gasto_gas",
        "Gasto_ocio", "Gasto_aficcion", "gastos_indefinidos", "deudas", "suscripciones", "pagos_tarjeta"
    ]

    with open(nombre_archivo, mode="w", newline="") as f:
        writer = csv.writer(f) #Crea un objeto que escribe en formato csv
        writer.writerow(list) #Escribe una primera columna.
        for i in range(cantidad):
            writer.writerow(codigo_5())
            writer.writerow(codigo_4())
            writer.writerow(codigo_3())
            writer.writerow(codigo_2())
            writer.writerow(codigo_1())






guardar_datos_csv("Fiancia(Creacion)/dataset1.csv", 1500)