#Sistema de elevador de prédio
# o prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode 
# se mover para cima ou para baixo, e tem a capacidade de tranasportar até 5 pessoas
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa 
# O elevador deve exibir mensagens indicando o andar atula, o número de pessoas no elevador, e as ações realizadas
# O programa deve continuar rodando até que o usuario dedicada encerrar

# levantamento de requisitos:

# requisitos funcionais(RF):
# o elevador deve se mover para cima e para baixo
# o elevador deve ser chamado por qualquer pessoa em qualquer andar
# tem uma capacidade limite de pessoas
# o elevador deve se mover diretamente até o andar em que foi chamado.




# requisitos não funcionais:
# o elevador pode exibir mensagens mostrando o andar atual e o número de pessoas no elevador.
# O programa pode continuar rodando até que o usuario dedicada encerrar.
# o elevador pode começar do andar 0.
# indicar ações realizadas
import time
print("sistema de elevador de prédio")
andares = 10
quantidade_pessoas = int(input("quantas pessoas vão usar o elevador?"))
if quantidade_pessoas >5:
    print("limite de pessoas no elevador atingido! maximo de 5 pessoas.")
elif quantidade_pessoas <=5:
    time.sleep(1)
    andar_desejado = int(input("qual andar você deseja ir? 0-\n 1-\n 2-\n 3-\n 4-\n 5-\n 6-\n 7-\n 8- \n 9- \n 10- \n "))






























































