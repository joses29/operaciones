class Operaciones:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        suma = self.numero1 + self.numero2
        return suma


    def resta(self):
        if self.numero1 >= self.numero2:
            return self.numero1 - self.numero2
        return 0

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0
        

    def divisionEntera(self):
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2

    def mostrar(self):
        print("Operando1={},Operando2={}".format(self.numero1,self.numero2))

print("Menu Operaciones Matematicas")
print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Division Entera\n6) Reciduo\n7) Exponente")
opc='0'
while opc !='0':
    opc = input("Elija opcio[1...0]: ")
    num1= int(input("Ingrese Numero1: "))
    num2= int(input("Ingrese Numero2: "))
    opc = Operaciones(num1,num2)
    if opc == '1':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.suma()))
    elif opc == '2':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.resta()))
    elif opc == '3':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.multiplicacion()))
    elif opc == '4':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.division()))
    elif opc == '5':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.divisionEntera()))
    elif opc == '6':
        print("{}={}={}".format(opc.numero1,opc.numero2,opc.exponente()))

print("Gracias por su visita esperamos fuera de su agrado")

















operacion = Operaciones(20,30)
x= operacion.suma() 
print(operacion.suma())
print(operacion.division())
y = operacion.resta()
x = x ** y 
print(x)
operacion.mostrar()
