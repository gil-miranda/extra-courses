users = [['896675','123','985'],['Gil','João', 'Maria']]
i = input('Digite sua senha: ')
while i not in users[0]:
    i = str(input('Senha incorreta! \nDigite  sua senha:'))
j = users[0].index(i)
name = users[1][j]
print('Acesso permitido. Bem-vindo %s' % (name))
