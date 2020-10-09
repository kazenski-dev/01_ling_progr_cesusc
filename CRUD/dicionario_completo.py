"""
nomes = ['Eduardo', 'MArtha', 'Felipi', 'Caio']
cpfs = ['00003455', '02430034530', '232323232', '232456777']
emails = ['gggggggggggg@', 'bbbbbbbbbbbbbbb@', 'ccccccccccccc@', 'ddddddddddddddddd@']

dicionario = {'Nomes: ', nomes, 'Cpfs: ', cpfs, 'Emails: ', emails}

print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())

for k, v in dicionario.items():
    print(k, v)


"""

dicionario = {'Nomes: ', 'aaa', 'Cpfs: ', 'aaa', 'Emails: ', 'aaa'}
dicionario2 = {'Nomes: ', 'bbb', 'Cpfs: ', 'bbb', 'Emails: ', 'bbb'}

cadastro = [dicionario, dicionario2]

print(cadastro)