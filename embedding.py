from openai import OpenAI

# apikeyを読み込む
with open('secret.txt', 'r') as file:
    mykey = file.read()

client = OpenAI(
  api_key=mykey
)

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


if __name__ == "__main__":
    print(get_embedding("RAGお試し"))