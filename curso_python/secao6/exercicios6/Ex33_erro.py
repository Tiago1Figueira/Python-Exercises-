# print correto, contudo eu não entendi pq eu coloquei 3 no range e assim deu certo!
n = int(input('Informe quantos múltiplos deseja ver na sequência:'))
i = int(input('Informe um número, inteiro e positivo,usado como múltiplo da sequência:'))
j = int(input('Informe outro número, inteiro e positivo,usado como múltiplo da sequência:'))
for c in range(0, n + 3):
    if c % i == 0 or c % j == 0:
        print(c,end=' ')









