from request import search_data
from openai import OpenAI
from embedding import get_embedding

# apikeyを読み込む
with open('secret.txt', 'r') as file:
    mykey = file.read()

client = OpenAI(
  api_key=mykey
)

# 参考情報取得
def get_ref(query, index="document_vectors"):
    target_vector_to_search = get_embedding(query)
    search_result = search_data(target_vector_to_search, 10, index=index)
    ref = ""
    if search_result:
        for hit in search_result["hits"]["hits"]:
            ref += hit['_source']['text'] + "\n"
    return ref


#chat
def chat(query, info=1):
    # 参考情報取得
    ref = get_ref(query, index="anime_doc")
    if info==1:
        print(ref)
    # chat作成
    response = client.chat.completions.create(
        # model="gpt-4",
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "参考情報をもとに質問に回答してください。わからない場合はわからないと答えてください。"},
            {"role": "user", "content": "#参考情報"},
            {"role": "user", "content": ref},
            {"role": "user", "content": "#質問"},
            {"role": "user", "content": query},
        ],
        temperature=0.7,
        # top_p=0.5,
        # frequency_penalty=0,
        # presence_penalty=0,
        # max_tokens=100, # 最大出力トークン
        # n = 3,
        stop=None,
    )
    print(response.choices[0].message.content)
    
if __name__ == "__main__":
    chat("鬼滅とは何ですか？いつから連載されていますか？")

