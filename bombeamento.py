import textwrap

class Bombeamento:
    """
    Classe que implementa a lógica do Lema do Bombeamento para testar a regularidade de linguagens.
    """
    def __init__(self, linguagem_func, p, palavra):
        """
        Inicializa o teste de bombeamento.
        
        :param linguagem_func: Função que verifica se uma palavra pertence à linguagem.
        :param p: Comprimento de bombeamento (p).
        :param palavra: Palavra (w) a ser testada, onde |w| >= p.
        """
        self.f = linguagem_func
        self.p = p
        self.w = palavra

    def testar_divisoes(self):
        """
        Testa todas as divisões w = xyz que satisfaçam as condições do lema:
        1. |xy| <= p
        2. |y| > 0
        3. Para todo k >= 0, x(y^k)z pertence à linguagem.
        """
        if len(self.w) < self.p:
            print(f"\n[!] Aviso: A palavra '{self.w}' tem comprimento {len(self.w)}, "
                  f"que é menor que p={self.p}. O teste pode não ser conclusivo.")

        print(f"\n--- Analisando palavra: '{self.w}' com p={self.p} ---")
        
        encontrou_irregularidade_geral = False

        # Condição do Lema: |xy| <= p
        # i é o fim de x, j é o fim de y
        for i in range(self.p):
            for j in range(i + 1, self.p + 1):
                x = self.w[:i]
                y = self.w[i:j]
                z = self.w[j:]

                if not y:
                    continue

                print(f"\nDivisão encontrada: x='{x}', y='{y}', z='{z}' (|xy|={len(x+y)})")
                divisao_valida = True
                
                # Testamos k=0 (remover y) e k=2 (duplicar y)
                for k in [0, 2]:
                    nova = x + y * k + z
                    status = self.f(nova)
                    simbolo = '✅' if status else '❌'
                    print(f"  y^{k}: '{nova}' → {simbolo}")
                    
                    if not status:
                        divisao_valida = False
                        break
                
                if not divisao_valida:
                    print(" >> Irregularidade detectada nesta divisão!")
                    encontrou_irregularidade_geral = True
                    # De acordo com o lema, se encontrarmos UMA divisão que falha o bombeamento,
                    # e o lema diz que para linguagens regulares EXISTE uma divisão que funciona,
                    # aqui a lógica é sutil: se testamos TODAS as divisões possíveis para |xy|<=p
                    # e TODAS falham, então a linguagem não é regular.
        
        print("\n" + "="*40)
        if encontrou_irregularidade_geral:
            print(" CONCLUSÃO: Irregularidades detectadas.")
            print(" Se TODAS as divisões possíveis falharam, a linguagem NÃO é regular.")
        else:
            print(" CONCLUSÃO: Nenhuma irregularidade detectada.")
            print(" A linguagem pode ser regular para este caso de teste.")
        print("="*40 + "\n")
        
        return encontrou_irregularidade_geral


def pertence_linguagem_an_bn(w):
    """
    Verifica se a palavra pertence à linguagem L = {a^n b^n | n >= 0}.
    """
    count_a = 0
    i = 0
    while i < len(w) and w[i] == 'a':
        count_a += 1
        i += 1
    
    count_b = 0
    while i < len(w) and w[i] == 'b':
        count_b += 1
        i += 1
        
    return i == len(w) and count_a == count_b


def main():
    header = """
    ===========================================
    💻 Simulador: Lema do Bombeamento
    Teoria da Computação e Linguagens Formais
    ===========================================
    """
    print(textwrap.dedent(header))
    
    print("Linguagem padrão: L = {a^n b^n | n >= 0}")
    palavra = input("Digite a palavra (ex: aaabbb): ").strip()
    
    try:
        p = int(input("Digite o valor de p (ex: 3): "))
        if p < 1:
            print("Erro: p deve ser >= 1")
            return
    except ValueError:
        print("Erro: p deve ser um número inteiro.")
        return

    teste = Bombeamento(pertence_linguagem_an_bn, p, palavra)
    teste.testar_divisoes()


if __name__ == "__main__":
    main()
