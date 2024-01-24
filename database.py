import request as es
import text_processing as tp
from tqdm import tqdm
import glob

if __name__ == "__main__":
    # データ読み込み
    filepath = glob.glob('./data/*')
    print(filepath)
    for path in filepath:
        header = path.split("/")[2].split(".")[0]
        docs = tp.text_splitter(tp.read_txt(path))
        docs = [header+ ">" + d for d in docs]
        
    
        for d in tqdm(docs):
            es.post_data(d, index="anime_doc")  # データを挿入
    