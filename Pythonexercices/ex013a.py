salario = float(input('Vencimento inicial: R$'))
primeira_correcao = salario * 12.5/100 + salario
segunda_correcao = primeira_correcao * 5/100 + primeira_correcao
terceira_correcao = segunda_correcao * 5/100 + segunda_correcao
print('\033[33mJaneiro de 2022:\033[m Com a correção de 12.5%, o vencimento total é de \033[36mR${:.2f}\033[m.\n (Acréscimo de \033[4mR${:.2f}\033[m).'.format(primeira_correcao, primeira_correcao - salario))
print('\033[33mJaneiro de 2023:\033[m Com a correção de 5%, o vencimento total é de \033[36mR${:.2f}\033[m.\n (Acréscimo de \033[4mR${:.2f}\033[m).'.format(segunda_correcao, segunda_correcao - primeira_correcao))
print('\033[33mJaneiro de 2024:\033[m Com a correção de 5%, o vencimento total é de \033[36mR${:.2f}\033[m.\n (Acréscimo de \033[4mR${:.2f}\033[m).'.format(terceira_correcao, terceira_correcao - segunda_correcao))
