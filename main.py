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
        if model_folder != 'edsr':
            print("Modelo incorreto para melhoria de imagem. Use um modelo EDSR.")
            sys.exit(1)
        elif model_version and model_version not in ['x3', 'x4']:
            print("Versão do modelo incorreta para melhoria de imagem. Use uma versão EDSR_x3 ou EDSR_x4.")
            sys.exit(1)

    if args.type == 'image':
        print('[x] - Aguarde um momento enquanto processamos sua imagem...')
        enhanced_image = enhance_image(args.input, model_directory, args.model)
        cv2.imwrite(args.output, enhanced_image)
        sys.exit(1)
    elif args.type == 'video':
        print('[x] - Aguarde um momento enquanto processamos sua video...')
        super_resolve_video(args.input, args.output, model_directory, args.model)
        sys.exit(1)

if __name__ == "__main__":
  try:
    main()
    print('[x] - Processamento finalizado, espero ter ajuda-lo.')
  except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
    sys.exit(0)
