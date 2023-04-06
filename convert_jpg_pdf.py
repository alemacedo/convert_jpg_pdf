import os
import img2pdf
import time

print('>>> Converter JPG para PDF')

print('> Em qual diretório está o JPG?')

path = input()

print('> Qual o nome do arquivo que deseja converter para PDF?')

file_name = input()

for i in os.listdir(path):

    if i == file_name:

        new_file_name = file_name.replace('.jpg', '.pdf')

        print('> Convertendo...', end='\r')

        time.sleep(2)

        full_path = f'{ path }{ file_name }'

        with open(f'{ path }{ new_file_name }', "wb") as f:

            f.write(img2pdf.convert(full_path))
        
        print(f'> Arquivo { file_name } convertido com sucesso.')
        print(f'> Criado novo arquivo { new_file_name }.')