class Bombeamento:
    def __init__(self, linguagem_func, p, palavra):
        self.f = linguagem_func
        self.p = p
        self.w = palavra

    def testar_divisoes(self):
        print(f"\n🔍 Testando: '{self.w}', p = {self.p}")
        for i in range(1, self.p + 1):
            for j in range(i + 1, self.p + 1):
                x = self.w[:i]
                y = self.w[i:j]
                z = self.w[j:]
                if not y:
                    continue

                print(f"Divisão: x='{x}', y='{y}', z='{z}'")
                for k in [0, 1, 2]:
                    nova = x + y * k + z
                    status = self.f(nova)
                    print(f"  y^{k}: '{nova}' → {'✅' if status else '❌'}")
                    if not status:
                        print("🚫 Violação detectada: linguagem NÃO é regular.\n")
                        return True
        print("✔️ Nenhuma violação detectada.\n")
        return False


# ---------- Função da linguagem L = { a^n b^m c^m }
def pertence_linguagem_am_bm_cm(w):
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


# ---------- Execução ----------
palavra = "aaabbbccc"
p = 5

teste = Bombeamento(pertence_linguagem_am_bm_cm, p, palavra)
teste.testar_divisoes()
