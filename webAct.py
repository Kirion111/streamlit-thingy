import streamlit as st
import pandas as pnd

def Hi():
    st.markdown("# 1: Escribe tu Nombre")
    name = st.text_input("Tu nombre")
    accept = st.button("Confirmar", key=1)
    return [accept, "Hola ",name] #Input del boton, Presentacion del resultado, resultado

def plus():
    st.markdown("# 2: Escribe 2 numeros, yo los sumare")
    numbers = [st.number_input("Numero 1", step=1), st.number_input("Numero 2", step=1)]
    accept = st.button("Confirmar", key=2)
    return [accept, "El resultado es: ", (numbers[0] + numbers[1])]

def tri():
    st.markdown("# 3: Escribe La base y la altura de un triangulo, obtendre su area")
    triangle = [st.number_input("Base", step=1), st.number_input("Altura", step=1)]
    accept = st.button("Confirmar", key=3)
    return [accept, "El Area del triangulo es: ", (triangle[0] * triangle[1])/2]

def calcular_precio_final():
    st.markdown("# 4: Escribe el precio de un producto")
    st.markdown("## Un descuento [1 = 1%, 10 = 10%] (OPCIONAL)")
    st.markdown("## Y un Impuesto [1 = 1%, 10 = 10%] (OPCIONAL)")
    sat = [st.number_input("Precio", step=1), st.number_input("Descuento", value=10, min_value=0, max_value=100, step=1), st.number_input("Impuesto", value=16, min_value=0, max_value=100, step=1)]
    accept = st.button("Confirmar", key=4)
    return [accept, f"Su producto de {sat[0]} con descuento de {sat[1]}% ({sat[0]*(sat[1]/100)}) e impuesto de {sat[2]}% ({sat[0]*(sat[2]/100)}) es de:\n", (sat[0] - (sat[0]*(sat[1]/100))) + (sat[0]*(sat[2]/100))]

def sumar_lista():
    st.markdown("# 5: Sumare los numeros que tu desees")
    st.markdown("## Ejemplo: 3, 4, 5 (Sin caracteres especiales)")
    st.markdown("## Presiona 'Calcular' para ver el resultado total")
    numbers = st.text_input("Tus numeros")
    accept = st.button("Calcular", key=5)

    numbers.strip("")
    nums = numbers.rsplit(",")
    total = 0
    if(numbers != ""):
        for num in nums:
            if(num == ""):
                continue
            total += int(num)

    return [accept, "La suma de los numeros es: ", total]

def producto():
    st.markdown("# 6: Escreibe el Nombre de un producto Inventado")
    st.markdown("## La cantidad de unidades a vender")
    st.markdown("## Y su precio por unidad")
    mercado = [st.text_input("Nombre"), st.number_input("Cantidad", min_value=1, step=1), st.number_input("Precio unitario", min_value=1, step=1)]
    accept = st.button("Calcular", key=6)

    return [accept, f"El precio final del producto '{mercado[0]}' vendido en una cantidad de {mercado[1]} unidades\nes de: ", mercado[1] * mercado[2]]

def numeros_pares_e_impares():
    st.markdown("# 7: Puedo reconocer que numeros son pares e inpares")
    st.markdown("## Pon tus numeros de esta forma: 3, 4, 5 (Sin caracteres especiales)")
    st.markdown("## Presiona 'Mostrar' para ver tus numeros organizados")
    numbers = st.text_input("Tus numeros", key="Exc2")
    accept = st.button("Mostrar", key=7)

    numbers.strip("")
    nums = numbers.rsplit(",")
    pair = []
    noPair = []
    if(numbers != ""):
        for num in nums:
            if(num == ""):
                continue
            if(int(num) % 2 == 0):
                pair.insert(len(pair), int(num))
            else:
                noPair.insert(len(noPair), int(num))

    return [accept, "Estos son tus numeros organizados en 2 listas, pares e impares (respectivamente): \n", f"{pair}\n{noPair}"]

def multiplicar_todos():
    st.markdown("# 8: Multiplicare los numeros que tu desees")
    st.markdown("## Ejemplo: 3, 4, 5 (Sin caracteres especiales)")
    st.markdown("## Presiona 'Calcular' para ver el resultado total")
    numbers = st.text_input("Tus numeros", key="Exc3")
    accept = st.button("Calcular", key=8)

    numbers.strip("")
    nums = numbers.rsplit(",")
    args = []
    if(numbers != ""):
        args = doProduct(nums)

    return [accept, "La multiplicacion total de los numeros es: ", args]

def doProduct(*args):
    total = 1
    for values in args:
        for num in values:
            if(num == ''):
                continue
            total *= int(num)

    return total

def informacion_personal():
    st.markdown("# 9: Escribe tu informacion, yo la mostrare de forma organizada")
    st.markdown("## Presiona 'Mostrar' para ver el resultado")
    info = [st.text_input("Nombres", key="Exc4"), st.text_input("Apellidos", key="Exc5"), st.text_input("Codigo Postal", key="Exc6")]
    accept = st.button("Mostrar", key=9)

    return[accept, "Tu informacion es;\n", correctShow(nombre=info[0], apellidos=info[1], CP=info[2])]

def correctShow(**kwargs):
    formated = ""
    for key, data in kwargs.items():
        if(data == ""):
            formated = ""
            break
        formated += f"{key}: {data}\n"
    return formated

def calculadora_flexible():
    st.markdown("# 10: Esta calculadora puede hacerte 4 operaciones")
    st.markdown("## Elije entre suma, resta, multiplicacion y division")
    st.markdown("## Presiona 'Mostrar' para ver el resultado")
    numbers = [st.number_input("Numero 1", step=1, key=20), st.number_input("Numero 2", step=1, key=21)]

    opts = {"Suma": 1, "Resta": 2, "Multiplicacion": 3, "Division": 4}
    input = st.radio("Operacion", options=opts, key=51)
    accept = st.button("Mostrar", key=10)
    return [accept, "El resultado es: ", daC(input, numbers, accept)]

def daC(opt:int, nums:list, proceed:bool):

    match opt:
        case "Suma":
            return nums[0] + nums[1]
        case "Resta":
            return nums[0] - nums[1]
        case "Multiplicacion":
            return nums[0] * nums[1]
        case "Division":
            if(nums[1] == 0):
                return "Divisor Invalido"
            return nums[0] / nums[1]

def displayResult(function):
    v = function
    if(v[2] != "" and v[0]):
        st.text(f"{v[1]}{v[2]}")
    else: 
        st.text("")
    
displayResult(Hi())
displayResult(plus())
displayResult(tri())
displayResult(calcular_precio_final())
displayResult(sumar_lista())
displayResult(producto())
displayResult(numeros_pares_e_impares())
displayResult(multiplicar_todos())
displayResult(informacion_personal())
displayResult(calculadora_flexible())