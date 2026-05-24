import pandas as pd
from accounting_classes import Razonete

caixa = Razonete('Caixa', 'Ativo')
# print(df.lancamentos_creditos)
caixa.insert_lancamento(1000.0, 'Débito','1a')
caixa.insert_lancamento(2000.0, 'Débito','2a')
caixa.insert_lancamento(500.0, 'Crédito','3a')
caixa.insert_lancamento(500.0, 'Crédito','4a')
caixa.remove_lancamento('2a')
caixa.remove_lancamento('2a')
print(caixa.totalizador())
print(caixa)