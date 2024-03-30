class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self._arma = None


    def pegar_arma(self, arma):
            self._arma = arma
            print(f'{self.nome} pegou a arma {self._arma.nome_arma}.')


    def _montar_arma(self):
        if not self._arma.montada:
            print(f'{self.nome} está montando {self._arma.nome_arma}.')
            self._arma.montada = True
        else:
            print(f'{self._arma.nome_arma} já está montada.')


    def _inserir_pente(self):
        if not self._arma.pente:
            print(f'inserindo pente em {self._arma.nome_arma}')
            self._arma.pente = True
        else:
            print(f'{self._arma.nome_arma} já está com pente inserido.')


    def _destravar(self):
        if self._arma.trava:
            print(f'destravando {self._arma.nome_arma}...')
            self._arma.trava = False
        else:  
            print(f'{self._arma.nome_arma} já está destravada.')


    def _atirar(self):
        if self._arma.pente and not self._arma.trava and self._arma.montada:
            print(f'{self._arma.nome_arma} está atirando.')
        else:
            print(f'{self.nome} aperta o gatilho')
            print(' -nada acontece...')


class Arma:
    def __init__(self, nome_arma, pente=False, trava=True, montada=False):
        self.nome_arma = nome_arma
        self.pente = pente
        self.trava = trava
        self.montada = montada


p1 = Pessoa('Victor')
a1 = Arma('glock')

p1.pegar_arma(a1)
p1._montar_arma()
p1._inserir_pente()
p1._destravar()
p1._atirar()
