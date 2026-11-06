# Sistema de Lançamento de Notas em Python

## 📌 Sobre o Projeto
O objetivo deste programa é automatizar o cálculo e o lançamento de notas de uma turma de 10 alunos de um curso EAD. O sistema processa as notas parciais de atividades e provas, aplica regras de aprovação direta, reprovação direta ou direcionamento para a prova final (recuperação), e gera um relatório estatístico completo da turma.

## ⚙️ Regras de Negócio Implementadas
* **Validação de Entradas:** Utilização de estruturas de repetição (`while`) para impedir o lançamento de notas fora dos limites permitidos em cada avaliação:
  * **AOP1:** 0 a 1 ponto
  * **AOP2:** 0 a 2 pontos
  * **AOP3:** 0 a 1 ponto
  * **Prova Regular:** 0 a 6 pontos
  * **Prova Final (Recuperação):** 0 a 10 pontos
* **Critérios de Aprovação:**
  * **Aprovado Direto:** Pontuação total $\ge 7.0$
  * **Reprovado Direto:** Pontuação total $< 3.0$ (sem direito à recuperação)
  * **Recuperação:** Pontuação total entre $3.0$ e $6.9$. O aluno realiza a Prova Final e a média é calculada por: $\frac{\text{Pontuação Parcial} + \text{Prova Final}}{2}$. Se a média for $\ge 5.0$, o aluno é aprovado.
* **Relatório Final:** Exibe a pontuação final e o status de cada aluno, acompanhado da quantidade total e porcentagem de aprovados e reprovados na turma.

## 🚀 Como Executar
1. Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.
2. Clone o repositório ou baixe o arquivo `main.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python main.py
