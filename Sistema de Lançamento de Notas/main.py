# Autor: João Pedro Fernandes Uliana
# Sistema de Lançamento de Notas

def main():
    total_alunos = 10
    aprovados = 0
    reprovados = 0
    resultados = []

    print("=== Sistema de Lançamento de Notas ===")

    for i in range(1, total_alunos + 1):
        print(f"\n--- Aluno {i} ---")
        
        # Validação AOP1 [0 a 1]
        while True:
            aop1 = float(input("Digite a nota da AOP1 [0 a 1]: "))
            if 0 <= aop1 <= 1:
                break
            print("Nota inválida! Digite um valor entre 0 e 1.")

        # Validação AOP2 [0 a 2]
        while True:
            aop2 = float(input("Digite a nota da AOP2 [0 a 2]: "))
            if 0 <= aop2 <= 2:
                break
            print("Nota inválida! Digite um valor entre 0 e 2.")

        # Validação AOP3 [0 a 1]
        while True:
            aop3 = float(input("Digite a nota da AOP3 [0 a 1]: "))
            if 0 <= aop3 <= 1:
                break
            print("Nota inválida! Digite um valor entre 0 e 1.")

        # Validação Prova Regular [0 a 6]
        while True:
            prova_regular = float(input("Digite a nota da Prova Regular [0 a 6]: "))
            if 0 <= prova_regular <= 6:
                break
            print("Nota inválida! Digite um valor entre 0 e 6.")

        pontuacao_total = aop1 + aop2 + aop3 + prova_regular
        status = ""
        pontuacao_final = pontuacao_total

        if pontuacao_total >= 7.0:
            status = "Aprovado"
            aprovados += 1
        elif pontuacao_total < 3.0:
            status = "Reprovado"
            reprovados += 1
        else:
            print(f"Pontuação parcial: {pontuacao_total:.2f} (Aluno em recuperação)")
            
            # Validação Prova Final [0 a 10]
            while True:
                prova_final = float(input("Digite a nota da Prova Final [0 a 10]: "))
                if 0 <= prova_final <= 10:
                    break
                print("Nota inválida! Digite um valor entre 0 e 10.")
            
            media_final = (pontuacao_total + prova_final) / 2
            pontuacao_final = media_final

            if media_final >= 5.0:
                status = "Aprovado"
                aprovados += 1
            else:
                status = "Reprovado"
                reprovados += 1

        print(f"\n[Feedback] Aluno {i} | Pontuação: {pontuacao_final:.2f} | Status: {status}")

        resultados.append({
            "aluno": i,
            "pontuacao": pontuacao_final,
            "status": status
        })

    print("\n========================================")
    print("         RELATÓRIO FINAL DA TURMA       ")
    print("========================================")
    
    for r in resultados:
        print(f"Aluno {r['aluno']:02d} | Pontuação: {r['pontuacao']:.2f} | Status: {r['status']}")

    porcentagem_aprovados = (aprovados / total_alunos) * 100
    porcentagem_reprovados = (reprovados / total_alunos) * 100

    print("----------------------------------------")
    print(f"Total de Aprovados: {aprovados} ({porcentagem_aprovados:.1f}%)")
    print(f"Total de Reprovados: {reprovados} ({porcentagem_reprovados:.1f}%)")
    print("----------------------------------------")

if __name__ == "__main__":
    main()