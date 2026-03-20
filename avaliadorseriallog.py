import os
import time
from multiprocessing import Pool


# ===============================
# Consolidação dos resultados
# ===============================

def consolidar_resultados(resultados):
    total_linhas = 0
    total_palavras = 0
    total_caracteres = 0

    contagem_global = {
        "erro": 0,
        "warning": 0,
        "info": 0
    }

    for r in resultados:
        total_linhas += r["linhas"]
        total_palavras += r["palavras"]
        total_caracteres += r["caracteres"]

        for chave in contagem_global:
            contagem_global[chave] += r["contagem"][chave]

    return {
        "linhas": total_linhas,
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "contagem": contagem_global
    }


# ===============================
# Processamento de arquivo
# ===============================

def processar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.readlines()

    total_linhas = len(conteudo)
    total_palavras = 0
    total_caracteres = 0

    contagem = {
        "erro": 0,
        "warning": 0,
        "info": 0
    }

    for linha in conteudo:
        palavras = linha.split()

        total_palavras += len(palavras)
        total_caracteres += len(linha)

        for p in palavras:
            if p in contagem:
                contagem[p] += 1

        # Simulação de processamento pesado
        for _ in range(1000):
            pass

    return {
        "linhas": total_linhas,
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "contagem": contagem
    }


# ===============================
# Execução paralela parametrizada
# ===============================

def executar_paralelo(pasta, num_processos):
    caminhos = [
        os.path.join(pasta, arquivo)
        for arquivo in os.listdir(pasta)
    ]

    inicio = time.time()

    # Pool com número configurável de processos
    with Pool(processes=num_processos) as pool:
        resultados = pool.map(processar_arquivo, caminhos)

    fim = time.time()

    resumo = consolidar_resultados(resultados)
    tempo_total = fim - inicio

    print(f"\n=== PARALELO ({num_processos} processos) ===")
    print(f"Arquivos processados: {len(resultados)}")
    print(f"Tempo total: {tempo_total:.4f} segundos")

    return tempo_total, resumo


# ===============================
# Experimento
# ===============================

def executar_experimentos(pasta):
    processos_teste = [2, 4, 8, 12]
    tempos = {}

    print("\n===== INICIANDO EXPERIMENTOS =====")

    for p in processos_teste:
        tempo, _ = executar_paralelo(pasta, p)
        tempos[p] = tempo

    print("\n===== RESULTADOS FINAIS =====")
    for p, t in tempos.items():
        print(f"{p} processos -> {t:.4f} segundos")

    return tempos


# ===============================
# Main
# ===============================

if __name__ == "__main__":
    pasta = "log2"

    executar_experimentos(pasta)
