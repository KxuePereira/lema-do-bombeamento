🚀 Lema do Bombeamento - Linguagens Formais
🎯 Objetivo do Projeto
O Lema do Bombeamento é uma ferramenta fundamental na teoria de linguagens formais usada para provar que certas linguagens não são regulares. Este projeto tem como objetivo implementar e testar esse lema em Python, de forma interativa, permitindo que os usuários verifiquem se uma linguagem definida é regular ou não.

Como funciona?
O código recebe como entrada:

Uma função que define a linguagem.

Um valor de bombeamento 
𝑝
p.

Uma cadeia 
𝑤
w da linguagem 
𝐿
L (onde 
∣
𝑤
∣
≥
𝑝
∣w∣≥p).

O código simula todas as possíveis divisões de 
𝑤
=
𝑥
𝑦
𝑧
w=xyz e aplica o bombeamento de 
𝑦
y (para 
𝑖
=
0
,
1
,
2
,
…
i=0,1,2,…).

Se qualquer cadeia gerada pelo bombeamento não pertencer à linguagem, o lema é violado, indicando que a linguagem não é regular.

🧰 Estrutura do Projeto
main.py: Código principal que implementa o Lema do Bombeamento.

README.md: Este arquivo de documentação.

relatorio.pdf: Relatório final com explicações detalhadas e análise do lema.

saida_terminal.png: Imagem mostrando a saída do terminal durante a execução de um exemplo de teste.

⚡ Como Rodar o Código
Pré-Requisitos
Python 3.x ou superior

Passos para Execução
Clone o repositório para sua máquina local:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/lema-do-bombeamento.git
cd lema-do-bombeamento
Configuração de Entrada: Abra o arquivo main.py e defina os seguintes parâmetros:

A cadeia 
𝑤
w (ex: "aaaabbbb")

O valor de bombeamento 
𝑝
p (ex: 4)

A função que verifica a linguagem (ex: pertence_linguagem)

Exemplo de configuração no arquivo:

python
Copiar
Editar
w = "aaaabbbb"  # Exemplo de cadeia na linguagem
p = 4           # Valor do bombeamento
Execute o Código:

bash
Copiar
Editar
python main.py
O código vai realizar o teste do Lema do Bombeamento e mostrar a saída no terminal, indicando se a linguagem é regular ou não.

🔍 Exemplo de Saída
Dado o exemplo 
𝑤
=
"
𝑎
𝑎
𝑎
𝑎
𝑏
𝑏
𝑏
𝑏
"
w="aaaabbbb" e 
𝑝
=
4
p=4, o programa vai tentar dividir a palavra em diferentes combinações de 
𝑥
x, 
𝑦
y, e 
𝑧
z, e então vai "bombeá-la" para diferentes valores de 
𝑖
i. A saída será algo como:

bash
Copiar
Editar
Testando palavra: 'aaaabbbb' com p = 4
Divisão: x = 'a', y = 'a', z = 'aabbbb'
  i = 0: 'abbbb' → Não pertence
❌ Quebrou o lema → Linguagem NÃO é regular.
Saída Esperada
Se a linguagem for regular, o programa confirmará que o lema não foi violado. Caso contrário, o código indicará uma violação e que a linguagem não é regular.

⚙️ Definições de Linguagem
Este projeto permite a definição de linguagens personalizadas para testar o lema do bombeamento. O código atualmente implementa um exemplo de linguagem simples:

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

Você pode adicionar novas funções que definem linguagens e testar o lema com diferentes palavras.

📝 Relatório do Projeto
Para mais detalhes sobre o funcionamento do lema e os testes realizados, consulte o relatório PDF no arquivo relatorio.pdf.

Diagrama de Funcionamento

Exemplo de diagrama explicativo do processo do Lema do Bombeamento

🔧 Contribuindo
Sinta-se à vontade para contribuir! Se você tem sugestões de melhorias ou deseja adicionar novas funcionalidades, basta fazer um Fork do repositório e abrir um Pull Request.

Passos para Contribuir:
Faça um fork deste repositório

Crie um branch para a sua feature:

bash
Copiar
Editar
git checkout -b minha-nova-feature
Adicione suas modificações:

bash
Copiar
Editar
git add .
git commit -m "Adiciona nova funcionalidade"
Faça o push para o seu repositório:

bash
Copiar
Editar
git push origin minha-nova-feature
Abra um Pull Request!

📄 Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.

🏅 Feedback e Discussões
Se você tiver dúvidas ou sugestões sobre o projeto, fique à vontade para abrir uma Issue ou discutir nos comentários. A colaboração é bem-vinda!

