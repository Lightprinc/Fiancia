import pandas as pd 

acum1 = 0
acum2 = 0
acum3 = 0
acum4 = 0
acum5 = 0

datos = pd.read_csv("IAFLASK\Fiancia(Formacion)\Fiancia(Creacion)\dataset1.csv")

gastos_necesarios = ["Gasto_viveres","Gasto_renta", "Gasto_electricidad", "Gasto_agua"]
gastos_subimportantes = ["Gasto_transporte", "Gasto_educacion", "Gasto_equipamiento_mantenimiento_hogar", "Gasto_gas"]


class PROGRAM():
    def __init__(self, fila): #Iniciar todos los datos necesarios
        self.datos = fila  # Diccionario con los datos de una fila

        self.ingreso = float(fila.get("Ingreso_mensual", 0))
        self.balance = float(fila.get("Balance", 0))
        self.ahorroTOT = float(fila.get("Ahorro_total", 0))
        self.deudas = float(fila.get("deudas"))

        self.tot = self.ingreso + self.balance + self.ahorroTOT + self.deudas 

        self.acumprym = 0
        self.acumsec = 0
        self.acum_total = 0
        self.mensajes = []
        self.codigo_recomendacion = 5#5 = Muy bien 4 = Bien, pero no se puede hacer la compra 3#Cuidado de los gastos 4#Se esta gastando mas de lo que se gana 5# Se generan dedudas
    
    def verificar_limite(self, gasto, limite, descripcion):
        if gasto > self.ingreso * limite:
            self.mensajes.append(f"Advertencia. Gasto alto en {descripcion} ({gasto})")
            
    def gastos_importantes(self): #Gastos importantes
        for gasto in gastos_necesarios:
            valor = float(self.datos.get(gasto, 0))
            self.acumprym += valor
            self.acum_total += valor

            if gasto == "Gasto_viveres":
                self.verificar_limite(valor, 0.4, "Comida")
            elif gasto == "Gasto_renta":
                self.verificar_limite(valor, 0.4, "Renta")
            elif gasto == "Gasto_electricidad":
                self.verificar_limite(valor, 0.2, "Electricidad")
            elif gasto == "Gasto_agua":
                self.verificar_limite(valor, 0.2, "Agua")

        dif = self.acumprym / self.ingreso * 100 if self.ingreso else 0
        if dif >= 100: #Si supera el acumulado el 100% del ingreso
            if self.acumprym > (self.ingreso + self.balance):
                if self.acumprym > (self.ingreso + self.balance + self.ahorroTOT): self.mensajes.append("CRITICO. Los gastos primarios generan deudas.")
                    
                else: self.mensajes.append("IMPORTANTE. Los gastos primarios superan ingreso + ahorro.")
                
        elif dif > 60:
            self.mensajes.append("Advertencia. Gastos primarios altos.")

    def gastos_sub_importantes(self): #Gastos sub-importantes
        for gasto in gastos_subimportantes:
            valor = float(self.datos.get(gasto, 0))
            self.acumsec += valor
            self.acum_total += valor

            if gasto == "Gasto_transporte":
                self.verificar_limite(valor, 0.1, "Transporte")
            elif gasto == "Gasto_educacion":
                self.verificar_limite(valor, 0.1, "Educación")
            elif gasto == "Gasto_equipamiento_mantenimiento_hogar":
                self.verificar_limite(valor, 0.2, "Mantenimiento del hogar")
            elif gasto == "Gasto_gas":
                self.verificar_limite(valor, 0.15, "Gas")

        dif = self.acumsec / self.ingreso * 100 if self.ingreso else 0
        if dif >= 100: #Si supera el acumulado el 100% del ingreso
            if self.acumsec > (self.ingreso + self.balance):
                self.mensajes.append("IMPORTANTE. Los gastos subimportantes superan ingreso + ahorro.")
            else:
                self.mensajes.append("CRITICO. Los gastos subimportantes generan deudas.")
        elif dif > 60:
            self.mensajes.append("Advertencia. Subgastos altos.")

    def acumulado_total_imp(self):
        total = self.acumprym + self.acumsec
        dif = total / self.ingreso * 100 if self.ingreso else 0
        if dif >= 100:
            if total > (self.ingreso + self.balance) and self.balance>0:
                self.mensajes.append("IMPORTANTE. Acumulado general supera ingreso + ahorro.")
            elif total > self.tot:
                self.mensajes.append("CRITICO. Acumulado general genera deudas.")
            else:
                self.mensajes.append("Advertencia. Acumulado general superior al ingreso.")
        elif dif > 85:
            self.mensajes.append("Advertencia. Acumulado general alto.")

    def gastos_secundarios(self):
        ocio = float(self.datos.get("Gasto_ocio", 0))
        aficcion = float(self.datos.get("Gasto_aficcion", 0))
        total = ocio + aficcion
        porcentaje = total / self.ingreso * 100 if self.ingreso else 0
        if porcentaje > 20:
            self.mensajes.append("Advertencia. Gasto alto en ocio y aficiones.")
        self.acum_total += total

    def otros_gastos(self):
        indef = float(self.datos.get("gastos_indefinidos", 0))
        deudas = float(self.datos.get("deudas", 0))
        suscripciones = float(self.datos.get("suscripciones", 0))
        tarjeta = float(self.datos.get("pagos_tarjeta", 0))
        total = indef + deudas + suscripciones + tarjeta

        if (deudas / self.ingreso * 100) > 20:
            self.mensajes.append("Advertencia. Deudas altas.")
        if (indef / self.ingreso * 100) > 20:
            self.mensajes.append("Advertencia. Gastos indefinidos altos.")
        if (suscripciones + tarjeta) / self.ingreso * 100 > 10:
            self.mensajes.append("Advertencia. Muchos gastos en tarjeta/suscripciones.")

        self.acum_total += total

    def compcomprobar_compra(self):
        global acum4, acum3, acum5
        if self.ingreso>self.acum_total:
            dif = self.ingreso- self.acum_total  # Restante
            dif = dif / self.ingreso * 100 # Porcentaje sobrante
            print("sobrante:" + str(dif))
            if  dif <= 15:
                self.codigo_recomendacion = 4
                acum4= acum4+1
            else:
                self.codigo_recomendacion = 5
                acum5= acum5+1
        else: 
            self.codigo_recomendacion = 3
            acum3 = acum3 + 1
            print("3")

        
    def conclusion(self):
        global acum1,acum2,acum3
        print("\n🧾 Resumen:")
        for m in self.mensajes:
            print("•", m)
        if any("CRITICO" in m for m in self.mensajes):
            self.codigo_recomendacion = 1
            acum1= acum1 +1
        elif any("IMPORTANTE" in m for m in self.mensajes):
            self.codigo_recomendacion = 2
            acum2= acum2+1
        elif any("Advertencia" in m for m in self.mensajes):
            self.codigo_recomendacion = 3
            acum3= acum3+1
        else:
            self.compcomprobar_compra()

        print("→ Código de recomendación:", self.codigo_recomendacion)

resultados = []

def Start(fila):
    global resultados
    analisis = PROGRAM(fila)
    analisis.gastos_importantes()
    analisis.gastos_sub_importantes()
    analisis.acumulado_total_imp()
    analisis.gastos_secundarios()
    analisis.otros_gastos()
    analisis.conclusion()

    fila_resultado = fila.to_dict()
    fila_resultado["codigo_recomendacion"] = analisis.codigo_recomendacion

    if analisis.codigo_recomendacion==1 and acum1>1000: print("do not")
    elif analisis.codigo_recomendacion==2 and acum2>1000: print("do not")
    elif analisis.codigo_recomendacion==3 and acum3>1000: print("do not")
    elif analisis.codigo_recomendacion==4 and acum4>1000: print("do not")
    elif analisis.codigo_recomendacion==5 and acum5>1000: print("do not")
    else: resultados.append(fila_resultado)

    

    

    


for i, fila in datos.iterrows():
    Start(fila)

fn_resultado = pd.DataFrame(resultados) #Convierte a "fn_resultado", en un 
fn_resultado.to_csv("resultado_analisis.csv", index=False)


print("1:", str(acum1), "2:", str(acum2), "3:", str(acum3), "4:", str(acum4), "5:", str(acum5))

