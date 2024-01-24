# RAGの環境構築
- langchain、llamaindexを基本使用しないRAG
- ローカルのElasticsearchを使用
- カスタマイズ性能を向上させたい

## 環境構築の方法
- memo/memo.txtを参照

## 各ファイルの説明
- chat.py
    - ユーザークエリーから参考情報取得
    - 参考情報を基にした回答生成
- database.py
    - dataディレクトリ内のデータをデータベースに挿入
    - txtファイルのファイル名をヘッダーとする
- embedding.py
    - テキストをembeddingする関数
- request.py
    - データベースへのデータ挿入関数
    - データ検索関数
    - データ削除関数
- text_processing.py
    - txtファイル読み込み
    - テキストのチャンク分割