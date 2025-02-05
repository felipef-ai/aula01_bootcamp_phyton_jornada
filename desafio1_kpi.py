#informado pelo professor no início do exercício 
CONSTANTE_BONUS = 1000
nome_usuario = input("Digite o seu Nome: ")
sobrenome_usuario = input("Digite o seu Sobrenome: ")
salario_usuario = float(input("Digite o valor do seu Salário R$: "))
bonus_usuario = float(input("Digite o valor do Bônus informado pelo e-mail: "))
bonus_final = CONSTANTE_BONUS + salario_usuario * bonus_usuario
print(CONSTANTE_BONUS, "Essa é a sua KPI com valores em R$")
print(f"Parabéns {nome_usuario} {sobrenome_usuario}. Com muita dedicação e esforço, você recebeu o bonus de {bonus_final}")
print("Nossa organização agradece seu empenho, e contamos com você nesse novo ano!!!")