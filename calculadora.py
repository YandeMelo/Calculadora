from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("520x550") 
janela.minsize(520, 550)
janela.maxsize(520, 550)

def tecla_pressionada(event):
    key = event.keysym
    if key in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        numero(key)
    elif key == "plus":
        numero("+")
    elif key == "minus":
        numero("-")
    elif key == "asterisk":
        numero("*")
    elif key == "slash":
        numero("/")
    elif key == "comma" or key == "period": #Ponto ou Vírgula
        numero(".")
    elif key == "Return": #Igual
        igualCalcular()
    elif key == "BackSpace":
        apagarUltimo()
    elif key == "Escape": #Esq
        apagarTudo()
    else:
        print("Tecla pressionada:", event.keysym)

def numero(char):
    global calcular
    
    if (calcular and calcular[-1] == "." and char == "." or (calcular and calcular[-1] == "," and char == ",")):
        return  # Evita repetição de pontos decimais
    
    if calcular and calcular[-1] in ("+", "-", "*", "/") and char in ("+", "-", "*", "/"):
        return  # Evita repetição de operadores
        
        
    calcular += str(char)
    entrada.set(calcular)

def apagarTudo():
    global calcular
    calcular = ""
    entrada.set(calcular)
    
def apagarUltimo():
    global calcular
    apagado = calcular[:-1]
    calcular = apagado
    entrada.set(calcular)

def igualCalcular():

    global calcular

    if(calcular[-1] in ("+", "-", "*", "/")):
        calcular = calcular[:-1]
        
    #eval - Avalia se é um calculo valido e efetua o calculo
    resultadoCalculo = str(eval(calcular))
    entrada.set(resultadoCalculo)  
    calcular = resultadoCalculo
    

calcular = ""
entrada = StringVar()
janela.bind("<Key>", tecla_pressionada)

resultado = Label(janela, textvariable=entrada, font=("Helvetica", 30, "bold"), foreground="black", background="light grey", relief=SUNKEN, borderwidth=5, width=20, anchor="w")
resultado.grid(row=1, columnspan=5, padx=15, pady= 20)
    
###################################
zero = Button(janela, text="0", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("0"))
zero.place(x=0, y=440)

um = Button(janela, text="1", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("1"))
um.place(x=0, y=330)

dois = Button(janela, text="2", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("2"))
dois.place(x=96, y=330)

tres = Button(janela, text="3", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("3"))
tres.place(x=192, y=330)

quatro = Button(janela, text="4", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("4"))
quatro.place(x=0, y=220)

cinco = Button(janela, text="5", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("5"))
cinco.place(x=96, y=220)

seis = Button(janela, text="6", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("6"))
seis.place(x=192, y=220)

sete = Button(janela, text="7", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("7"))
sete.place(x=0, y=110)

oito = Button(janela, text="8", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("8"))
oito.place(x=96, y=110)

nove = Button(janela, text="9", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("9"))
nove.place(x=192, y=110)
###################################

ponto = Button(janela, text=".", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=4, relief=RAISED, borderwidth=5, command=lambda:numero("."))
ponto.place(x=96, y=440)

igual = Button(janela, text="=", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=14, relief=RAISED, borderwidth=5, padx=17, command=igualCalcular)
igual.place(x=192, y=440)
###################################

soma = Button(janela, text="+", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=lambda:numero("+"))
soma.place(x=288, y=330)

subtracao = Button(janela, text="-", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=lambda:numero("-"))
subtracao.place(x=404, y=330)

multiplicar = Button(janela, text="*", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=lambda:numero("*"))
multiplicar.place(x=288, y=220)

dividir = Button(janela, text="/", background="light grey", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=lambda:numero("/"))
dividir.place(x=404, y=220)
###################################

delete = Button(janela, text="DEL", background="dark orange", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=apagarUltimo)
delete.place(x=288, y=110)

apagar = Button(janela, text="AC", background="dark orange", foreground="black", font=("Helvetica", 25, "bold"), height=2, width=5, relief=RAISED, borderwidth=5, command=apagarTudo)
apagar.place(x=404, y=110)
###################################


janela.mainloop()