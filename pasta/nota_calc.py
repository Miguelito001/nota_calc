quantidade_notas = int(input("Digite a quantidade de notas do aluno: "))
media_escola = float(input("Digite a média da escola: "))

notas = []
for i in range(quantidade_notas):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    notas.append(nota)

media_aluno = sum(notas) / quantidade_notas

if media_aluno >= media_escola:
    resultado = "Aprovado"
    nota_minima = None
else:
    resultado = "Reprovado"
    nota_minima = min(notas)
    nota_necessaria = (media_escola * quantidade_notas) - sum(notas) + nota_minima

print("Média do aluno: {:.2f}".format(media_aluno))
print("Resultado: {}".format(resultado))

if nota_minima is not None:
    print("Para alcançar a média, substitua a nota {:.2f} pela nota {:.2f}".format(nota_minima, nota_necessaria))
