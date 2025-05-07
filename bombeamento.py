class Bombeamento:
    def __init__(self, linguagem_func, p, palavra):
        """
        Inicializa o teste de bombeamento com a função da linguagem, valor de p e palavra a ser testada.
        :param linguagem_func: Função que verifica se uma palavra pertence à linguagem
        :param p: Valor do lema do bombeamento
        :param palavra: Palavra a ser testada
        """
        self.f = linguagem_func
        self.p = p
        self.w = palavra

    def testar_divisoes(self):
        """
        Testa todas as divisões possíveis de acordo com o lema do bombeamento.
        Exibe o relatório no terminal.
        """
        print(f"\n Testando...: '{self.w}', p = {self.p}")
        for i in range(1, self.p + 1):
            for j in range(i + 1, self.p + 1):
                x = self.w[:i]
                y = self.w[i:j]
                z = self.w[j:]
                if not y:
                    continue

                print(f"\nDivisão: x='{x}', y='{y}', z='{z}'")
                for k in [0, 1, 2]:
                    nova = x + y * k + z
                    status = self.f(nova)
                    print(f"  y^{k}: '{nova}' → {'✅' if status else '❌'}")
                    if not status:
                        print(" Irregularidade detectada: linguagem NÃO é regular.\n")
                        return True
        print(" Nenhuma irregularidade detectada. A linguagem pode ser regular.\n")
        return False


def pertence_linguagem_am_bm_cm(w):
    """
    Função que verifica se a palavra pertence à linguagem L = {a^n b^m c^m}.
    :param w: Palavra a ser verificada
    :return: True se a palavra pertence à linguagem, False caso contrário
    """
    i = 0
    while i < len(w) and w[i] == 'a':
        i += 1
    j = i
    while j < len(w) and w[j] == 'b':
        j += 1
    k = j
    while k < len(w) and w[k] == 'c':
        k += 1
    return j - i == k - j and k == len(w)


if __name__ == "__main__":
    print("=== Teste do Lema do Bombeamento ===\n")
    palavra = input("Digite a palavra a ser testada: ").strip()
    try:
        p = int(input("Digite o valor de p (≥ 1): "))
        if p < 1:
            raise ValueError
    except ValueError:
        print(" Valor inválido. 'p' deve ser um número inteiro maior ou igual a 1.")
    else:
        teste = Bombeamento(pertence_linguagem_am_bm_cm, p, palavra)
        teste.testar_divisoes()
