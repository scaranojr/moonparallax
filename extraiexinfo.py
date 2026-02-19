import os
from PIL import Image
from PIL.ExifTags import TAGS

# Caminho da pasta com as imagens
pasta_imagens = "C:\\Users\\scara\\OneDrive - academico.ufs.br\\UFS\\ProjetoExtensao\\CNPq2022\\Pesquisa\\Paralaxes\\OcultacaoAntares\\Atalaia"

arquivo_saida = os.path.join(pasta_imagens, "resultado_datetime.txt")

# Função para extrair o DateTime dos metadados EXIF
def extrair_datetime(imagem_path):
    try:
        imagem = Image.open(imagem_path)
        exif_data = imagem._getexif()
        if exif_data:
            for tag_id, valor in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTime":
                    return valor
        return "DateTime não encontrado"
    except Exception as e:
        return f"Erro ao processar {imagem_path}: {e}"

with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write("Arquivo\t\tDateTime\n")
    f.write("-" * 40 + "\n")

# Percorre os arquivos da pasta
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.lower().endswith(".jpg"):
            caminho_completo = os.path.join(pasta_imagens, arquivo)
            datetime = extrair_datetime(caminho_completo)
            print(f"{arquivo}: {datetime}")
            f.write(f"{arquivo}\t{datetime}\n")
print(f"✅ Resultado salvo em: {arquivo_saida}")
