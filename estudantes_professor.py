#chamando a bilbioteca
import PySimpleGUI as psg
#cadastro de estudantes
#Apresentação
print('\n\t\t\t  --  Cadastro de Estudantes  --')

#Estrutura do dicionário
estudante = {
    'Nome': 'Nome do estudante',
    'Curso': 'Teste',
    'Nota': 0,
    'Matricula': False
}

#Entrada
estudante['Nome'] = input('Informe o nome do estudante: ')
estudante['Nota'] = input('Informe a nota: ')
estudante['Curso'] = input('Informe o curso: ')
matricula = input('Estudante regular (s/n)? ')
#estudante['Matricula'] = True

if matricula.lower() == 's':
    estudante[matricula] = True

#Saída
print(f'Nome.....................{estudante["Nome"]}')
print(f'Curso....................{estudante["Curso"]}')
print(f'Nota.....................{estudante["Nota"]}')
print('Estudante regular') if estudante['Matricula'] else print('Matrícula trancada')


#psg.popup('Boa tarde!')