import PyPDF2
import rarfile

def extrair_palavras_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        palavras = set()
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            texto = page.extractText()
            palavras.update(texto.split())
    return palavras

def testar_senhas_rar(rar_path, palavras):
    rar = rarfile.RarFile(rar_path)
    for palavra in palavras:
        try:
            rar.extractall(pwd=palavra.encode('utf-8'))
            print(f'Senha encontrada: {palavra}')
            return palavra
        except rarfile.BadRarFile:
            continue
    print('Nenhuma senha encontrada.')
    return None

# Caminhos para os arquivos PDF e RAR
pdf_path = 'C:\Users\cs504\Downloads\a.rar'
rar_path = 'C:\Users\cs504\Downloads\Apostila-03.pdf'

palavras = extrair_palavras_pdf(pdf_path)
testar_senhas_rar(rar_path, palavras)
