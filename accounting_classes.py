from typing import Dict

class Razonete:
    def __init__(self, natureza_contabil:str = 'Ativo', lanc_debito:Dict[str,float] = {}, lanc_credito:Dict[str,float] = {}) -> None:
        # estrutura do lancamentos: {'1a':1000.0}
        self.natureza_contabil = natureza_contabil
        self.lanc_credito = lanc_credito
        self.lanc_debito = lanc_debito

    def saldo(self):
        valor_saldo = (sum(self.lanc_debito.values()) - sum(self.lanc_credito.values()))
        tipo_saldo = 'Devedor' if valor_saldo >= 0 else 'Credor'
        return {'Tipo de saldo': tipo_saldo, 'Valor do saldo': valor_saldo}

# caixa = Razonete('Ativo', {'1':1000.0}, {'2':200.0})
# caixa = Razonete('Ativo', {'1':1000.0})
# caixa.saldo()

