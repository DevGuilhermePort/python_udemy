# Typecasting.
print('a' + 'a')  # O sinal de mais quando usado em string, concatena uma na outra.
print(10.5 + 4.5)  # O sinal de mais em números, sejam inteiros ou flutuantes, soma um valor com o outro.
print('10.5' + 4.5)  # Como python é uma linguagem de tipagem forte, ele não pode realizar essa ação. Pra isso, deve ser feito a coerção de tipo.

print(int('10,5') + float('4.5'))  # Usando as classes `int()`, `float()`, `str()`, `bool()` posso fazer a coerção dos dados.
