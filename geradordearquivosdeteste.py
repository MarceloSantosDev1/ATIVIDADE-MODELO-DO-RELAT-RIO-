import os
import random
import argparse

def gerar_arquivos(pasta, qtd_arquivos=50, linhas_por_arquivo=200):
    os.makedirs(pasta, exist_ok=True)

    palavras = ["erro", "warning", "info", "processo", "dados", "sistema"]

    for i in range(qtd_arquivos):
        with open(os.path.join(pasta, f"arquivo_{i+1}.txt"), "w", encoding="utf-8") as f:
            for _ in range(linhas_por_arquivo):
                linha = " ".join(random.choices(palavras, k=20))
                f.write(linha + "\n")

    print(f"{qtd_arquivos} arquivos gerados em '{pasta}' com {linhas_por_arquivo} linhas cada.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de arquivos de teste para logs")
    parser.add_argument("--pasta", type=str, default="log2", help="Pasta onde os arquivos serão gerados")
    parser.add_argument("--qtd", type=int, default=50, help="Quantidade de arquivos a gerar")
    parser.add_argument("--linhas", type=int, default=200, help="Número de linhas por arquivo")

    args = parser.parse_args()

    gerar_arquivos(args.pasta, args.qtd, args.linhas)