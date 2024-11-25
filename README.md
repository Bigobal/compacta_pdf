# Código fonte do compactador de PDF criado para a DEICOT para ajustar aos formatos do PJe. O programa possui alguns modulos de compactação que vão desde compactações simples até compatações extremas que podem comprometer inclusive a qualidade do material compactado. Na barra de navegação simples do aplicativo ele permite que você selecione qual o modelo deseja usar. Após selecionar o modelo e o arquivo ele iniciará a compactação do arquivo e fará a divisão das páginas para atender ao tamanho máximo do PJe, qual seja, 10MB por arquivo, portanto, caso após a compressão, o arquivo possua mais de 10MB de tamanho, o programa iniciará a divisão para garantir que ele seja repartido em partes que possam ser inseridas no PJe.

# Não foi possível disponibilizar o arquivo executável do script por conta de bibliotecas que aumentam o tamanho do executável.

# Para geração do arquivo executável, basta colocar o arquivo compacta.py em um diretório, garantir que o python esteja instalado na máquina, com as dependências pyinstaller e executar o comando: pyinstaller -onefile -noconsole "compacta.py".

# Dúvidas, entre em contato.
