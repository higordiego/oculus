import argparse
import cv2
import sys
import os

from src.banner import banner, info
from src.images import enhance_image
from src.videos import super_resolve_video

def main():
    banner()
    info()  
    
    parser = argparse.ArgumentParser(description='Melhoria da qualidade de imagem e vídeo.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--input', type=str, required=True, help='Caminho para a imagem de entrada')
    parser.add_argument('--output', type=str, required=True, help='Caminho para o arquivo de saída')
    parser.add_argument('--type', choices=['image', 'video'], required=True, help='Tipo de entrada (imagem ou vídeo)')
    parser.add_argument('--model', type=str, required=True, help='Caminho para o arquivo do modelo. Ex: --model edsr/edsr_x2.pb')
    args = parser.parse_args()

    model_folder = os.path.dirname(args.model)
    model_version = args.model.split('_')[1].split('.')[0] if len(args.model.split('_')) > 1 else None


    pwd_directory = os.getcwd()
    model_directory = os.path.join(pwd_directory, args.model)

    if args.type == 'image':
        print('[x] - Aguarde um momento enquanto processamos sua imagem...')
        enhanced_image = enhance_image(args.input, model_directory, args.model)
        cv2.imwrite(args.output, enhanced_image)
    elif args.type == 'video':
        print('[x] - Aguarde um momento enquanto processamos sua video...')
        super_resolve_video(args.input, args.output, model_directory, args.model)

if __name__ == "__main__":
  try:
    main()
    print('[x] - Processamento finalizado, espero ter ajuda-lo.')
    sys.exit(1)
  except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
    sys.exit(0)
