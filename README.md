Este repositório corresponde à distribuição da base de dados observacionais e códigos utilizados para sua extração e análise, conforme artigo aprovado na RBEF intitulado "Distância Lunar por Meio da Paralaxe Telescópica a partir de
Linhas de Base Ultracurtas". Neles se encontram os seguintes arquivos:

MoonParallax_Antares_DataAnalysis.xlsx: Planilha com todos os resultados e nossas analises, separadas em abas para o SETUP 1, 2 e 3. O dados estão organizados em colunas contendo o nome do arquivo utilizado para extração dos dados (Arquivo), o tempo em minutos após a ocultação de Antares (Tempo [min]), a distância angular em relação ao centro da Lua (Distância [arcmin]), resíduos em relação ao ajuste (Resíduos [arcmin]), distância corrigida dos desvíos sistemáticos (Dist_Corrigida [arcmin]), respectivo resíduo (Resíduos_Correção [arcmin]), tempo final após correções temporais (td_f[min]), distância final após correções temporais (dd_f[arcmin]), desvios finais em relação ao SETUP 1 (res_d[arcmin]). Para o SETUP 1 não há todas estas colunas, pois ele é tomado como referência para as demais colunas, nos outros setups.

Setup1a.tar.bz2: Arquivo compactado com as imagens das observações feitas com o Setup 1. As informações de metadados deste arquivo foram retiradas utilizando o código extraiexinfo.py.

Setup1b.tar.bz2: Segunda parte do arquivo compactado com as imagens das observações feitas com o Setup 1

Setup2.tar.bz2: Arquivo compactado com as imagens das observações feitas com o Setup 2. Informações detalhadas deste arquivo obtidas com o código readhedertime.py.

Setup3.tar.bz2: Arquivo compactado com as imagens das observações feitas com o Setup 3. Os vídeos de onde eles foram retirados encontram-se disponíveis no canal ASTUTOS-UFS: https://youtube.com/shorts/ygSyb7Yv9PQ, https://youtube.com/shorts/zUnp3_ZlaW4, https://youtu.be/YxBuY5bwhF4 e https://youtube.com/shorts/CWqLFjTxpdo. As informações temporais foram retiradas diretamente do registro do nome dos arquivos para o primeiro frame de cada vídeo, respectivamente 20240524_012046.mp4, 20240524_012358.mp4, 20240524_012914.mp4 e 20240524_014047.mp4.

extraiexinfo.py: Código para extração dos metadados dos arquivos jpeg obtidos com o Setup 1.

readhedertime.py: Código para extração das informações do header dos arquivos fits obtidos com o Setup 2.
