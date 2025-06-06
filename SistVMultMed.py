from datetime import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def eliminarMedicamento(self, nombre_med):
        for med in self.__lista_medicamentos:
            if med.verNombre().lower() == nombre_med.lower():
                self.__lista_medicamentos.remove(med)
                return True
        return False
    
class sistemaV:
    def __init__(self):
        self.caninos = {}
        self.felinos = {}

    def verificarExiste(self, historia):
        return historia in self.caninos or historia in self.felinos

    def verNumeroMascotas(self):
        return len(self.caninos) + len(self.felinos)

    def ingresarMascota(self, mascota):
        if mascota.verTipo().lower() == "canino":
            self.caninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo().lower() == "felino":
            self.felinos[mascota.verHistoria()] = mascota

    def buscarMascota(self, historia):
        return self.caninos.get(historia) or self.felinos.get(historia)

    def verFechaIngreso(self, historia):
        mascota = self.buscarMascota(historia)
        return mascota.verFecha() if mascota else None

    def verMedicamento(self, historia):
        mascota = self.buscarMascota(historia)
        return mascota.verLista_Medicamentos() if mascota else None

    def eliminarMascota(self, historia):
        if historia in self.caninos:
            del self.caninos[historia]
            return True
        elif historia in self.felinos:
            del self.felinos[historia]
            return True
        return False
    
    def eliminarMedicamentoMascota(self, historia, nombre_medicamento):
        mascota = self.buscarMascota(historia)
        if mascota:
            return mascota.eliminarMedicamento(nombre_medicamento)
        return False
    def validar_fecha(fecha):
     try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
     except ValueError:
        return False

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                if tipo not in ["canino", "felino"]:
                 print("Tipo inválido.")
                 continue
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                if not validar_fecha(fecha):
                 print("Formato de fecha inválido. Use dd/mm/aaaa.")
                 continue
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]
                nombres_usados = set()

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos.lower() in nombres_usados:
                     print("Medicamento repetido. No se puede ingresar dos veces.")
                     continue
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            historia = int(input("Historia clínica: "))
            nombre_med = input("Nombre del medicamento a eliminar: ")
            if servicio_hospitalario.eliminarMedicamentoMascota(historia, nombre_med):
                print("Medicamento eliminado.")
            else:
                print("No se encontró ese medicamento o mascota.")
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

