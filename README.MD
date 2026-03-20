import os

os.makedirs("log1", exist_ok=True)

linhas_base = [
    "info sistema inicializado com sucesso",
    "warning uso elevado de memoria detectado",
    "erro falha ao conectar ao banco de dados",
    "info usuario autenticado corretamente",
    "warning disco proximo do limite",
    "erro timeout na requisicao"
]

for i in range(3):
    with open(f"log1/log_{i+1}.txt", "w", encoding="utf-8") as f:
        for _ in range(200):
            for linha in linhas_base:
                f.write(linha + "\n")

print("log1 gerado com sucesso!")