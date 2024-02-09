import argparse
import cv2
import sys
import os

from src.banner import banner, info
from src.images import enhance_image, extract_info_image
from src.videos import super_resolve_video

def main():
    banner()
    info()  
    parser = argparse.ArgumentParser(description='Melhoria da qualidade de imagem e vídeo.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--input', '-i', type=str, required=True, help='Caminho para a imagem de entrada')
    parser.add_argument('--output', '-o', type=str, required=False, help='Caminho para o arquivo de saída')
    parser.add_argument('--type', '-t', choices=['image', 'video'], required=True, help='Tipo de entrada (imagem ou vídeo)')
    parser.add_argument('--show', '-s', action='store_true', help='Informa metadados da imagem')
    parser.add_argument('--model', type=str, required=False, default="models/edsr/edsr_x2.pb", help='Caminho para o arquivo do modelo. Ex: --model models/edsr/edsr_x2.pb')
    args = parser.parse_args()

    model_folder = None
    model_version = None
    model_directory = None
    if args.model: 
      model_folder = os.path.dirname(args.model)
      model_version = args.model.split('_')[1].split('.')[0] if len(args.model.split('_')) > 1 else None

      pwd_directory = os.getcwd()
      model_directory = os.path.join(pwd_directory, args.model)

    if args.type == 'image':
      if args.show:
        extract_info_image(args.input)
      else:
        print('[x] - Aguarde um momento enquanto processamos sua imagem...')
        enhanced_image = enhance_image(args.input, model_directory, args.model)
        cv2.imwrite(args.output, enhanced_image)
        
    elif args.type == 'video':
        if args.model is None:
          print('[o] - Parâmetro model é obrigatório para tipo de video')
          sys.exit(1)
        if args.output is None:
          print('[o] - Parâmetro output é obrigatório para tipo de video')
          sys.exit(1)
        print('[x] - Aguarde um momento enquanto processamos seu video...')
        super_resolve_video(args.input, args.output, model_directory, args.model)

if __name__ == "__main__":
  try:
    main()
    print('[x] - Processo finalizado, espero ter ajuda-lo.')
    sys.exit(1)
  except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
    sys.exit(0)
