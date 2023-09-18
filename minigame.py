from turtle import Turtle
t = Turtle()
t.speed(10)
print(f'Sentido : Frente (f), Trás (t) \nRotação: Direita (d), Esquerda (e))')
while True:
    direcao = input('Anda para qual direção?: ')
    distancia = int(input('Quantos pixels?: '))
    if direcao == 'f':
        t.forward(distancia)
        input()    
    else:
        t.backward(distancia)
        input()
    girar = input('Rotacionar? (s ou n): ')
    if girar =='s':
        rotacao = input('Gira para qual lado?: ')
        angulo = int(input('Qual o ângulo: '))
        if rotacao == 'd':
            t.right(angulo)
            input()
        elif rotacao == 'e':
            t.left(angulo)
            input()  
        continua = input('Coninuar andando? (s ou n) :')
        if continua == 'n':
            break
    elif girar =='n':
        continua = input('Coninuar andando? (s ou n) :')
        if continua == 'n':
            break
    



