from langchain.text_splitter import CharacterTextSplitter
# import PyPDF2

# テキスト読み込み関数
# サンプルテキストを読み込む
def read_txt(filename="sample.txt"):
    with open(filename, 'r') as file:
        text = file.read()
    return text

# def read_pdf(pdf_path):
#     # PDFファイルを読み込むためのファイルオブジェクトを開く
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfFileReader(file)
#         text = ""
#         # 各ページについてループ処理
#         for page_num in range(reader.numPages):
#             # ページオブジェクトを取得
#             page = reader.getPage(page_num)
#             # ページのテキストを取得
#             text += page.extractText()
#         return text


# テキスト分割
def text_splitter(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300, 
        chunk_overlap=30
        )

    docs = text_splitter.split_text(text)
    return docs

    # print(docs[1])
    
if __name__ == "__main__":
    text = read_txt("sample.txt")
    print(text)