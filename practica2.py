print ('Buenos días, por favor coopere ingresando datos lógicos')
dato_x= int(input('Si desea sumar, escriba 1; Si desea restar, escriba 2; Si desea dividir, escriba ; Si desea multiplicar, escriba 4: '))
#garantizar el ingreso de entero, sin flotantes o strings en dato_x
# agregar condicionales a propiedades no conmutativas
if dato_x > 4:
    print ('por favor ingrese uno de los valores indicados')
else:
    if dato_x == 1:
        dato_1= float(input('Ingrese un sumando: '))
        dato_2= float(input('Ingrese otro sumando: '))
        respuesta= dato_1 + dato_2
        print ('la respuesta es: ', respuesta)
    elif dato_x == 4:
        dato_1= float(input('Ingrese el multiplicando: '))
        dato_2= float(input('Ingrese el multiplicador: '))
        respuesta= dato_1 * dato_2
        print ('la respuesta es: ', respuesta)
    elif dato_x == 2:
        print('En las sustracciones del tipo a-b= c, "a" es el minuendo y "b" es el sustraendo')
        dato_1= float(input('Ingrese minuendo: '))
        dato_2= float(input('Ingrese sustraendo: '))
        respuesta= dato_1 - dato_2
        print ('la respuesta es: ', respuesta)
    elif dato_x==3:
        dato_1= float(input('Ingrese dividendo o numerador: '))
        dato_2= float(input('Ingrese divisor o denominador: '))
        if dato_2==0:
            raise ZeroDivisionError
            print("Debe ingresar un denominador distinto de cero")
        else:
            respuesta= dato_1 + dato_2
            print ('la respuesta es: ', respuesta)