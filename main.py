# numero=int(input("digite o primeiro número")) #condicionais
# numero2=int(input("digite o segundo numero"))         

# if numero==numero2: #se o numero for igual ao numero2, vai ser mostrado "os numeros são iguais"
#     print("Os numeros são iguais")
# else:
#     print("os numeros são diferentes")


# sinal=str(input("digite a cor do sinal"))
# if sinal=="vermelho": #se for vermelho,mostre pare
#     print("pare")
# elif sinal=="amarelo": #se não for vermelho e sim amarelo, mostre reduzir
#     print("reduzir")
# elif sinal=="verde": #se não for vermelho e sim verde, mostre prossiga
#     print("prossiga")
# else:                #se não for nenhuma opção, mostre digite uma cor(...)
#     print("digite uma cor entre vermelho, amarelo ou verde")

numero=int(input("digite um numero"))
if numero==0:
    print("neutro")
elif numero>0:
    print("positivo")
elif numero<0:
    print("negativo")
