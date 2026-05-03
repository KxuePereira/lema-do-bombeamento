🔥 Lema do Bombeamento - Linguagens Formais 🔥
📝 Sobre o Projeto
O projeto implementa e testa o Lema do Bombeamento para linguagens formais. Esse lema é uma ferramenta teórica usada na área de Teoria de Linguagens e Autômatos para provar que determinadas linguagens não são regulares.

📚 O que é o Lema do Bombeamento?
O Lema do Bombeamento afirma que, para linguagens regulares, qualquer cadeia suficientemente longa pode ser dividida em três partes, 
𝑤
=
𝑥
𝑦
𝑧
w=xyz, onde:

𝑥
x pode ser repetido 
𝑘
k vezes, para 
𝑘
≥
0
k≥0, sem que a cadeia saia da linguagem.

𝑦
y é a parte que deve ser repetida (bombeada), e não pode estar vazia.

𝑧
z é a parte da cadeia que não será modificada.

Com isso, o lema fornece uma forma de verificar se uma linguagem é regular: se não for possível dividir uma cadeia dessa forma e ainda manter a cadeia dentro da linguagem após bombear, a linguagem não é regular.

🎯 Objetivo
Este projeto visa:

Implementar o Lema do Bombeamento em Python para testar a regularidade de uma linguagem.

Permitir a entrada de uma linguagem formal (definida por uma função), um valor de bombeamento 
𝑝
p, e uma cadeia 
𝑤
w (onde 
∣
𝑤
∣
≥
𝑝
∣w∣≥p).

Realizar a simulação do lema e verificar se as palavras geradas pelo bombeamento de 
𝑦
y ainda pertencem à linguagem.

Indicar se o lema foi violado (indicando que a linguagem não é regular).

🧑‍💻 Estrutura do Projeto
bombeamento.py: O código principal que implementa a lógica do Lema do Bombeamento.

README.md: Este arquivo de documentação.

🔧 Funcionalidade da Linguagem
Este projeto pode ser adaptado para testar diferentes linguagens. O código atualmente implementa um exemplo simples de linguagem:

Linguagem: 
𝐿
=
{
𝑎
𝑛
𝑏
𝑛
∣
𝑛
≥
0
}
L={a 
n
 b 
n
 ∣n≥0}

Você pode facilmente modificar a função de linguagem no código e adicionar novas linguagens para verificar se elas são regulares ou não, conforme o Lema do Bombeamento.

💡 Como Contribuir
Se você deseja contribuir para o projeto, siga os seguintes passos:

Faça um fork deste repositório.

Crie um branch para a nova funcionalidade:

bash
Copiar
Editar
git checkout -b minha-nova-feature
Faça alterações e commit:

bash
Copiar
Editar
git add .
git commit -m "Adiciona nova funcionalidade"
Envie para o seu repositório:

bash
Copiar
Editar
git push origin minha-nova-feature
Abra um Pull Request.

🤝 Contato
Se tiver dúvidas ou sugestões, não hesite em entrar em contato ou abrir uma issue neste repositório. Ficarei feliz em ajudar!

