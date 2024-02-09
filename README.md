
# Oculus: Elevando a Qualidade Visual com Super-Resolução

Bem-vindo ao Oculus, sua ferramenta Python definitiva para transformar imagens e vídeos comuns em obras-primas de alta definição. Utilizando o poder dos modelos de Redes Neurais Profundas (DNN), o Oculus é a ponte para um mundo onde a resolução elevada e a nitidez excepcional definem o novo padrão de qualidade visual.

## 🌄 Exemplo

<p align="center">
  <img src="https://placehold.co/400x100" alt="Imagem 1" width="100%" />
  
</p>


## 🌈 Funcionalidades

Oculus não é apenas uma ferramenta; é a solução para uma gama de desafios visuais, oferecendo:

- **Super-Resolução de Imagens e Vídeos:** Transforme conteúdo de baixa resolução em alta definição com apenas alguns cliques.
- **Suporte Diversificado de Modelos:** Escolha entre uma variedade de modelos de super-resolução para encontrar o ajuste perfeito para suas necessidades.
- **Processamento Flexível:** Seja processando um único arquivo ou em lote, o Oculus adapta-se perfeitamente ao seu fluxo de trabalho.

## 🚀 Começando

### Pré-requisitos

Antes de mergulhar, certifique-se de ter instalado:

- OpenCV (`cv2`)
- Colorama

### Instalação

Clone o repositório e instale as dependências necessárias para dar vida ao Oculus:

```
pip3 install -r requirements.txt
```

## 🔍 Como Usar

Transformar suas imagens e vídeos é tão simples quanto executar:


```sh
python3 main.py --input seu_arquivo.png --output saida.png --model models/edsr/edsr_x4.pb --type image
```

```sh
python3 main.py --input video.mp4 --output video.avi --model models/fsrcnn/fsrcnn-small_x4.pb --type video
```

### Escolha Seu Modelo

Atualmente, oferecemos suporte a:

- **EDSR x3** para aqueles que buscam um equilíbrio entre performance e qualidade.
- **EDSR x4** para quem não se contenta com menos do que a máxima definição.

Deseja experimentar outro modelo? Adicione-o facilmente ao projeto e especifique através do `--model`.

## 🤝 Contribua

Sua voz é essencial na jornada do Oculus. Contribuições, seja uma sugestão ou um código, são sempre bem-vindas.

## 📝 Licença

Este projeto é disponibilizado sob a licença MIT. Por favor, consulte o arquivo LICENÇA para mais detalhes.

## 💌 Contato

[Higor Diego](https://higordiego.com.br) - Para perguntas ou colaborações, não hesite em me enviar um [e-mail](mailto:me@higordiego.com.br).


