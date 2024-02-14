
# Oculus

```markdown


    ▒█████   ▄████▄   █    ██  ██▓     ▒█████    ██████ 
    ▒██▒  ██▒▒██▀ ▀█   ██  ▓██▒▓██▒    ▒██▒  ██▒▒██    ▒ 
    ▒██░  ██▒▒▓█    ▄ ▓██  ▒██░▒██░    ▒██░  ██▒░ ▓██▄   
    ▒██   ██░▒▓▓▄ ▄██▒▓▓█  ░██░▒██░    ▒██   ██░  ▒   ██▒
    ░ ████▓▒░▒ ▓███▀ ░▒▒█████▓ ░██████▒░ ████▓▒░▒██████▒▒
    ░ ▒░▒░▒░ ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
      ░ ▒ ▒░   ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░
    ░ ░ ░ ▒  ░         ░░░ ░ ░   ░ ░   ░ ░ ░ ▒  ░  ░  ░  
        ░ ░  ░ ░         ░         ░  ░    ░ ░        ░  
            ░               
```

Bem-vindo ao Oculus, sua ferramenta Python definitiva para transformar imagens e vídeos comuns em obras-primas de alta definição. Utilizando o poder dos modelos de Redes Neurais Profundas (DNN), o Oculus é a ponte para um mundo onde a resolução elevada e a nitidez excepcional definem o novo padrão de qualidade visual. Além disso, o Oculus oferece uma gama de recursos adicionais para aprimorar suas criações visuais e facilitar seu fluxo de trabalho em análise de foto ou vídeo.

## 🌈 Funcionalidades

Oculus não é apenas uma ferramenta; é a solução para uma gama de desafios visuais, oferecendo:

- **Super-Resolução de Imagens e Vídeos:** Transforme conteúdo de baixa resolução em alta definição com apenas alguns cliques.
- **Transformação de Vídeos em Frames de Fotos:** Extraia frames de fotos de vídeos para análise e processamento individuais.
- **Suporte Diversificado de Modelos:** Escolha entre uma variedade de modelos de super-resolução para encontrar o ajuste perfeito para suas necessidades, como EDSR, ESPCN e FSRCNN.
- **Visualização de Metadados de Imagens:** Acesse informações detalhadas sobre suas imagens, como dados GPS, tipo de aparelho e muito mais.
- **Processamento Flexível:** Seja processando um único arquivo ou em lote, o Oculus adapta-se perfeitamente ao seu fluxo de trabalho.

## 🚀 Começando

**Pré-requisitos**

Antes de começar, certifique-se de ter instalado:

- Python na versão **3.11**

**Instalação**

Clone o repositório e instale as dependências necessárias para utilizar o Oculus:

```sh
git clone git@github.com:higordiego/oculus.git
```

```sh
pip3 install -r requirements.txt
```

## 🔍 Como Usar

**Super-Resolução de Imagens**

```sh
python3 main.py --input seu_arquivo.png --output saida.png --model models/edsr/edsr_x4.pb --type image
```

**Super-Resolução de Vídeos**

```sh
python3 main.py --input video.mp4 --output video.avi --model models/fsrcnn/fsrcnn-small_x4.pb --type video
```

**Transformação de Vídeos em Frames de Fotos:**

```sh
python3 main.py --input video.mp4 --type video -f
```

**Visualização de Metadados de Imagens:**

```sh
python3 main.py --type image --input image.png -s
```

## Escolha Seu Modelo

Atualmente, oferecemos suporte aos seguintes modelos:

- **EDSR (Enhanced Deep Super-Resolution) x2, x3 e x4:** Oferecem equilíbrio entre performance e qualidade, com opções para diferentes níveis de resolução.
- **ESPCN (Efficient Sub-Pixel Convolutional Neural Network) x2, x3 e x4:** Modelos eficientes para super-resolução.
- **FSRCNN (Fast Super-Resolution Convolutional Neural Network) x2, x3 e x4:** Rápidos e eficazes em aumentar a resolução de imagens.
- **FSRCNN-small_x2, x3 e x4:** Variantes do FSRCNN otimizadas para recursos computacionais limitados.
- **LAPSRN (Layer Aggregation-based Pixel-wise Super-Resolution Network) x2, x4 e x8:** Modelos avançados que agregam informações em múltiplas camadas para super-resolução.

<br>
Deseja experimentar outro modelo? 

Adicione-o facilmente ao projeto e especifique através do --model.

## 🤝 Contribua

Sua voz é essencial na jornada do Oculus. Contribuições, seja uma sugestão ou um código, são sempre bem-vindas.

## 📝 Licença

Este projeto é disponibilizado sob a licença MIT. Por favor, consulte o arquivo LICENÇA para mais detalhes.

## 💌 Contato

[Higor Diego](https://higordiego.com.br) - Para perguntas ou colaborações, não hesite em me enviar um [e-mail](mailto:me@higordiego.com.br).


