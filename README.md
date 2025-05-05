Projeto: Teste do Lema do Bombeamento

Este projeto em Python aplica o Lema do Bombeamento para verificar se uma linguagem formal é regular. Utiliza uma função que representa a linguagem  e testa uma cadeia conforme as regras do lema.

📌 Linguagem Testada

L = { aⁿ bᵐ cᵐ | n ≥ 0, m ≥ 0 }A linguagem contém:

Um número qualquer de símbolos 'a'

Seguidos por a mesma quantidade de 'b's e 'c's

Exemplo de cadeia válida: aaabbbccc

⚙️ Como Rodar o Código

Certifique-se de ter Python 3 instalado.

Execute o script com:

python main.py

📥 Entrada do Programa

Função da linguagem: pertence_linguagem_am_bm_cm

Palavra: aaabbbccc

Valor de bombeamento: p = 5

🔍 Objetivo

O programa simula todas as possíveis divisões da cadeia w = xyz com:

|xy| ≤ p

|y| ≥ 1

Testa as palavras xy⁰z, xyz, xy²z

Caso alguma dessas palavras não pertença à linguagem, isso mostra que a linguagem não é regular.

✅ Resultado Esperado

Se alguma cadeia gerada pela repetição de y não pertencer à linguagem, o lema é quebrado. Isso indica que a linguagem não pode ser reconhecida por um autômato finito.

📄 Autor

Projeto acadêmico para disciplina de Linguagens Formais — 2025.
