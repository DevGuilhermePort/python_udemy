print(12, 34, sep='',end=" ")  # Passando argumentos não nomeados para a função print. Por padrão, no fim do print o código executa uma quebra de linha "\n". Eu posso trocar essa quebra de linha pelo que eu quiser.
print(56, 78, sep='')  # Por padrão, o separador da função print é um espaço, passando o argumento nomeado como nada eu posso remover este espaço, ou trocalo por qualquer coisa.

help(print)