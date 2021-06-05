"""
#1
# ano bissexto: se o ano for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
É divisível por 400.

#1.2
ex38 (bissexto)
bisexto = False
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    bisexto = True
"""