from pandas import DataFrame

class Razonete:
    def __init__(self, nome_conta:str, natureza_contabil:str = 'Ativo') -> None:
        colunas_esperadas = [
            'indice_debitos',
            'lancamentos_debitos',
            'lancamentos_creditos',
            'indice_creditos',
        ]
        
        naturezas_esperadas = [
            'Ativo',
            'Passivo',
            'PL',
        ]

        if natureza_contabil not in naturezas_esperadas:
            raise ValueError(f'Natureza contábil só aceita: {str(naturezas_esperadas)}')

        self.nome_conta = nome_conta
        self.livro_razao = DataFrame(columns=colunas_esperadas)
        self.natureza_contabil = natureza_contabil

    def __repr__(self):
        return f'Razonete({self.nome_conta} - {self.natureza_contabil}, livro_razao={self.livro_razao})'

    def totalizador(self):
        coeficiente = 1 if self.natureza_contabil == 'Ativo' else -1
        total = self.livro_razao.lancamentos_debitos.sum() -\
                self.livro_razao.lancamentos_creditos.sum()
        total = total * coeficiente
        return total

    def is_already_index(self, indice:str) -> bool:
        mask_lines = (
            (self.livro_razao['indice_debitos'] == indice) |
            (self.livro_razao['indice_creditos'] == indice)
        )

        lines_qtd = len(self.livro_razao.loc[mask_lines])

        return lines_qtd > 0
    
    def insert_lancamento(self, valor:float, debito_credito:str, indice_lancamento:str=''):
        if not isinstance(valor, float):
            raise TypeError('valor deve ser float')

        if not isinstance(indice_lancamento, str):
            raise TypeError('indice_lancamento deve ser str')
        
        if self.is_already_index(indice_lancamento):
            raise IndexError('Index já existe. Escolha um novo')

        valor_credito = valor if debito_credito == 'Crédito' else float()
        valor_debito = valor if debito_credito == 'Débito' else float()
        indice_credito = indice_lancamento if debito_credito == 'Crédito' else str(None)
        indice_debito = indice_lancamento if debito_credito == 'Débito' else str(None)

        self.livro_razao.loc[len(self.livro_razao)] = [indice_debito, valor_debito, valor_credito, indice_credito]

    def remove_lancamento(self, indice):
        if not isinstance(indice, str):
            raise TypeError('indice deve ser str')

        mask = (
            (self.livro_razao['indice_debitos'] == indice) |
            (self.livro_razao['indice_creditos'] == indice)
        )

        if not mask.any():
            raise ValueError('This index doesn\'t exist')

        self.livro_razao = self.livro_razao.loc[~mask].reset_index(drop=True)
