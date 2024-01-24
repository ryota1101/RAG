import requests
from embedding import get_embedding
import uuid

# データ挿入
def post_data(text, index="document_vectors"):
    new_uuid = str(uuid.uuid4())
    data = {
        "document_id": new_uuid,
        "text": text,
        "vector": get_embedding(text)
    }

    # print(data)
    response = requests.post(f"http://localhost:9200/{index}/_doc/{new_uuid}", json=data)
    
    if response.status_code == 201:
        return None
    else:
        print(f"データ挿入に失敗しました。エラーコード: {response.status_code}")
        print(response.json())
        return None

# データ検索
def search_data(target_vector, top_k=10, index="document_vectors"):
    data = {
        "size": top_k,  # 返される検索結果の数
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'vector') + 1.0",
                    "params": {
                        "query_vector": target_vector
                    }
                }
            }
        }
    }

    response = requests.post(f"http://localhost:9200/{index}/_search", json=data)
    
    if response.status_code == 200:
        search_results = response.json()
        return search_results
    else:
        print(f"ベクトル検索に失敗しました。エラーコード: {response.status_code}")
        print(response.json())
        return None
    
# 全てのデータ削除
def delete_all_documents(index="document_vectors"):
    data = {
        "query": {
            "match_all": {}  # 全てのドキュメントに該当
        }
    }

    # Delete by Queryを使って全ドキュメントを削除
    response = requests.post(f"http://localhost:9200/{index}/_delete_by_query", json=data)
    response_data = response.json()
    print(response_data)

    return response    

if __name__ == "__main__":
    # #テキスト検索
    # text_to_search = "RAGの勉強"
    # target_vector_to_search = get_embedding(text_to_search)
    # search_result = search_data(target_vector_to_search, 3)
    
    # if search_result:
    #     # print("ベクトル検索結果:")
    #     for hit in search_result["hits"]["hits"]:
    #         # print(f"ID: {hit['_id']}, スコア: {hit['_score']}, テキスト: {hit['_source']['text']}")
    #         print(hit['_source']['text'])

    # #データ挿入
    # text_to_post = "こんばんは。ジョンです。"
    # post_data(text_to_post)  # データを投稿
    
    # データ削除
    delete_all_documents()
    