
# oculus
Melhoria de Qualidade de Imagem com Super-Resolução

Este projeto é uma ferramenta em Python para melhorar a qualidade de imagens por meio de super-resolução, usando modelos de rede neural profunda (DNN). 
Ele permite aumentar a resolução e a nitidez das imagens e videos, resultando em uma imagem e videos de maior qualidade e detalhes mais nítidos.

## Funcionalidades

- Melhoria da qualidade de imagem por meio de super-resolução
- Suporte para diferentes modelos de super-resolução
- Processamento de imagens e videos em lote ou de imagens individuais

## Dependências

Para executar este projeto, você precisará ter as seguintes bibliotecas Python instaladas:

- OpenCV (cv2)
- Colorama

Você pode instalar essas dependências usando o pip:

```sh
pip3 install -r requirements.txt
```

## Como Utilizar

Para melhorar a qualidade de uma imagem individual, execute o script `main.py`, fornecendo o caminho para a imagem de entrada e o modelo de super-resolução desejado. Por exemplo:

```sh
python3 main.py --input image.png --output output.png --model edsr/edsr_x4.pb --type image
```

## Modelos Disponíveis

Atualmente, este projeto suporta os seguintes modelos de super-resolução:

- EDSR (Enhanced Deep Super-Resolution) com fator de escala x3 (EDSR_x3)
- EDSR com fator de escala x4 (EDSR_x4)
- Outros modelos podem ser adicionados facilmente ao projeto conforme necessário.

Para utilizar um modelo diferente, basta fornecer o nome do arquivo do modelo correspondente no parâmetro `--model`.

## Autor

Este projeto foi desenvolvido por [Higor Diego](https://higordiego.com.br). 

Se você tiver alguma dúvida ou sugestão, entre em contato pelo email [contato@higordiego.com.br](mailto:contato@higordiego.com.br).





