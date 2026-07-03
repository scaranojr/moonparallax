import os
from astropy.io import fits
from astropy.time import Time

# Diretório atual (onde o script está)
pasta_fits = os.path.dirname(os.path.abspath(__file__))

# Arquivo de saída na mesma pasta
arquivo_saida = os.path.join(pasta_fits, "tempos_utc.txt")

# Lista para armazenar os resultados
resultados = []

# Percorre todos os arquivos na pasta atual
for nome_arquivo in os.listdir(pasta_fits):
    if nome_arquivo.lower().endswith(".fits"):
        caminho_arquivo = os.path.join(pasta_fits, nome_arquivo)
        try:
            with fits.open(caminho_arquivo) as hdul:
                header = hdul[0].header
                jd_utc = header.get("JD_UTC")
                if jd_utc:
                    # Converte JD para UTC
                    tempo = Time(jd_utc, format='jd', scale='utc')
                    utc_str = tempo.utc.iso  # formato ISO 8601
                    resultados.append(f"{nome_arquivo}\t{utc_str}")
                else:
                    resultados.append(f"{nome_arquivo}\tJD_UTC não encontrado")
        except Exception as e:
            resultados.append(f"{nome_arquivo}\tErro: {str(e)}")

# Grava os resultados no arquivo de saída
with open(arquivo_saida, "w") as f:
    f.write("Arquivo\tTempo_UTC\n")
    for linha in resultados:
        f.write(linha + "\n")

print(f" Processamento concluído. Resultados salvos em: {arquivo_saida}")