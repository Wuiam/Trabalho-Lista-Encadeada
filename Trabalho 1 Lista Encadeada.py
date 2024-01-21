class No:
    def __init__(self, palavra):
        self.palavra = palavra
        self.proxima = None  # Próximo elemento na lista básica
        self.proxima_alfabetica = None  # Próxima palavra na lista4


class Lista:
    def __init__(self):
        self.primeirinho = None

    def inserir_em_ordem(self, palavra):
        novo_no = No(palavra)

        if self.primeirinho is None or self.primeirinho.palavra >= palavra:
            novo_no.proxima = self.primeirinho
            self.primeirinho = novo_no
        else:
            leitor = self.primeirinho
            while leitor.proxima and leitor.proxima.palavra < palavra:
                leitor = leitor.proxima
            novo_no.proxima = leitor.proxima
            leitor.proxima = novo_no

    def remover(self, palavra):
        if not self.primeirinho:
            return "falhou"
        if self.primeirinho.palavra == palavra:
            self.primeirinho = self.primeirinho.proxima
            return "removido"

        leitor = self.primeirinho
        anterior = None
        while leitor and leitor.palavra != palavra:
            anterior = leitor
            leitor = leitor.proxima
        if leitor:
            anterior.proxima = leitor.proxima
            return "removido"
        else:
            return "falhou"

    def existe(self, palavra):
        leitor = self.primeirinho
        while leitor:
            if leitor.palavra == palavra:
                return True
            leitor = leitor.proxima
        return False

    def exibir(self):
        leitor = self.primeirinho
        while leitor:
            print(leitor.palavra)
            leitor = leitor.proxima


class Listas_Bizarras:
    def __init__(self):
        self.listas_bizarrinhas = Lista()  # lista 1
        self.listas_bizarrenhas = Lista()  # lista 2
        self.listas_bizarronas = Lista()  # lista 3
        self.listas_zibarro = Lista()  # lista 4

    def inserir_palavra(self, palavra_nova):
        if self.consultar(palavra_nova):
            print("palavra ja existente:", palavra_nova)
            return
        else:
            tamanho = len(palavra_nova)
            lista_a_inserir = None

            if tamanho <= 5:
                lista_a_inserir = self.listas_bizarrinhas
            elif 6 <= tamanho <= 10:
                lista_a_inserir = self.listas_bizarrenhas
            elif tamanho > 10:
                lista_a_inserir = self.listas_bizarronas

            if lista_a_inserir:
                lista_a_inserir.inserir_em_ordem(palavra_nova)

                # Inserir na lista4
                self.listas_zibarro.inserir_em_ordem(palavra_nova)

            print("palavra inserida:", palavra_nova)

    def remover_palavra(self, palavra):
        for i in range(1, 5):
            if i == 4:
                result = self.listas_zibarro.remover(palavra)
            else:
                lista = self.lista_palavras(i)
                result = lista.remover(palavra)

            if result == "removido":
                print("palavra removida:", palavra)
                return
        print("palavra inexistente:", palavra)

    def remover_zibarro(self, palavra):
        result = self.listas_zibarro.remover(palavra)
        return result

    def consultar(self, palavra):
        pescador = self.listas_zibarro.primeirinho
        while pescador:
            if pescador.palavra == palavra:
                return True
            pescador = pescador.proxima_alfabetica
        return False

    def lista_numero_letras(self, numero):
        lista = self.listas_zibarro
        atual = lista.primeirinho
        esconde = False
        while atual:
            if len(atual.palavra) == numero:
                esconde = True
                print(atual.palavra)
            atual = atual.proxima_alfabetica
        if not esconde:
            print("lista vazia")

    def lista_ordem_alfabetica(self, l1, l2):
        for i in range(1, 5):
            if i == 4:
                self.exibir_lista_ordem_alfabetica(self.listas_zibarro, l1, l2)
            else:
                self.exibir_lista_ordem_alfabetica(self.lista_palavras(i), l1, l2)

    def exibir_lista_ordem_alfabetica(self, lista, l1, l2):
        atual = lista.primeirinho
        pique = False
        while atual is not None:
            if l1 <= atual.palavra[0] <= l2:
                pique = True
                print(atual.palavra)
            atual = atual.proxima_alfabetica
        if not pique:
            print("lista vazia")

    def lista_palavras(self, tamanho):
        if tamanho == 1:
            return self.listas_bizarrinhas
        elif tamanho == 2:
            return self.listas_bizarrenhas
        elif tamanho == 3:
            return self.listas_bizarronas
        elif tamanho == 4:
            return self.listas_zibarro


listas_bizarras = Listas_Bizarras()

while True:
    ditador = input()
    if ditador == "i":
        palavra_nova = input()
        listas_bizarras.inserir_palavra(palavra_nova)
    elif ditador == "r":
        palavra_deletada = input()
        listas_bizarras.remover_palavra(palavra_deletada)
    elif ditador == "l":
        comprimento = int(input())
        listas_bizarras.lista_numero_letras(comprimento)
    elif ditador == "x":
        numero = int(input())
        listas_bizarras.lista_numero_letras(numero)
    elif ditador == "o":
        l1 = input()
        l2 = input()
        listas_bizarras.lista_ordem_alfabetica(l1, l2)
    elif ditador == "e":
        break
