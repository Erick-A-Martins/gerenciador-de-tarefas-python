# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

nome = input("Qual seu nome? ")
saudacao(nome)

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2 # ** - Número ao quadrado
    return resultado

print("\nChamando a função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:", resultado_quadrado)

# Função com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma dos numeros %s e %s é %s" % (numero1, numero2, resultado_soma))

