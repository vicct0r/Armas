class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self._arma = None


    def pegar_arma(self, arma):
        try:
            if self._arma is not None:
                print(f'{self.nome} já está com {self._arma.nome_arma} em mãos.')
            else:
                self._arma = arma
                print(f'{self.nome} pegou {self._arma.nome_arma}.')
        except ValueError as e:
            print(e)


    def soltar_arma(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está segurando nenhuma arma.')
            else:
                print(f'{self.nome} soltou {self._arma.nome_arma}.')
                self._arma = None
        except ValueError as e:
            print(e)


    def _montar_arma(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está portando uma arma.')
            elif self._arma.montada:
                print(f'A arma {self._arma.nome_arma} já está montada.')
            print(f'montando {self._arma.nome_arma}...')
            self._arma.montada = True
        except ValueError as e:
            print(e)


    def desmontar_arma(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está portando nenhuma arma.')
            elif self._arma.montada:
                print(f'desmontando {self._arma.nome_arma}.')
                self._arma.montada = False
            else:
                print(f'{self._arma.nome_arma} já está desmontada.')
        except ValueError as e:
            print(e)

    def _inserir_pente(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está com {self._arma.nome_arma} em mãos')
            elif self._arma.pente: 
                print(f'{self._arma.nome_arma} já esta com pente inserido.')
            elif not self._arma.montada:
                print(f'{self._arma.nome_arma} está desmontada!')
            else:
                print(f'{self.nome} inserindo pente em {self._arma.nome_arma}...')
                self._arma.pente = True
        except ValueError as e:
            print(e)


    def tirar_pente(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está com nenhuma arma em mãos.')
            elif self._arma.pente:
                print(f'retirando pente de {self._arma.nome_arma}.')
            else:
                print(f'{self._arma.nome_arma} já está sem pente.')
        except ValueError as e:
            print(e)


    def _destravar(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está com {self._arma.nome_arma} em mãos.')
            elif not self._arma.trava:
                print(f'{self._arma} já está destravada.')
            else:
                print(f'destravando {self._arma.nome_arma}.')
                self._arma.trava = False
        except ValueError as e:
            print(e)


    def travar(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está com nenhuma arma em mãos.')
            elif self._arma.trava:
                print(f'{self._arma.nome_arma} já está travada.')
            else:
                self._arma.trava = True
                print(f'{self._arma.nome_arma} foi travada.')
        except ValueError as e:
            print(e)


    def _atirar(self):
        try:
            if self._arma is None:
                print(f'{self.nome} não está com {self._arma.nome_arma} em mãos...')
            elif not self._arma.pente:
                print(f'{self._arma.nome_arma} está sem pente.')
            elif self._arma.trava:
                print(f'{self._arma.nome_arma} está travada.')
            else:
                print(f'{self.nome} está atirando com {self._arma.nome_arma}.')
        except ValueError as e:
            print(e)


class Arma:
    def __init__(self, nome_arma, pente=False, trava=True, montada=False):
        self.nome_arma = nome_arma
        self.pente = pente
        self.trava = trava
        self.montada = montada


p1 = Pessoa('Django')
a1 = Arma('Winchester')

p1.pegar_arma(a1)
p1._montar_arma()
p1._inserir_pente()
p1._destravar()
p1._atirar()
p1.tirar_pente()
p1.travar()
p1.desmontar_arma()
p1.soltar_arma()
