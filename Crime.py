perguntas = ["Telefonou a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima?", "Já trabalhou com a vítima? "]
respostas = []
for pergunta in perguntas:
    resposta = int(input(pergunta + "(1) Sim (0) Não "))
    respostas.append(resposta)

soma = 0
for resposta in respostas:
    soma = soma + resposta

if soma < 2:
    print("Inocente")
elif soma == 2:
    print("Suspeito")
elif soma <= 4:
    print("Cúmplice")
else:
    print("Assaltante")