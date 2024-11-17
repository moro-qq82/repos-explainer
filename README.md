# repository explainer
- openaiのapiを用いて何らかのリポジトリの中身のファイルをすべて自然言語で説明させ、それをテキストファイルに保存します
- 得られたテキストをNotebookLM等に突っ込んでコーディングのお供にすることを想定しています
<br>
<br>
(English)

- Use OpenAI's API to generate natural language explanations for all files within a given repository and save them in a text file.
- The resulting text is intended to be used as a coding aid by inputting it into tools like NotebookLM.


### How to use
- 動作はpython3.12.1で確認しています
- ` pip install openai`
- 環境変数"OPENAI_API_KEY"にAPIKEYを設定してください
- target-repository-srcに説明させたいリポジトリのソースコードを丸ごとコピーしてください
- get_explanation_texts.pyでリポジトリのフォルダ構造に沿って説明テキストを書きだします
- integrate_explanation_files.pyで全テキストを一つのファイルにします
- !! CAUTION !!
  - 2024年11月17日現在gpt-4o-miniを使用していますが、リポジトリ全体を読み込んで説明テキストを書きだすので相当量のトークンを消費します
  - api使用料と実行時間がかかりますのでご注意ください

<br>
<br>
(English)  

- The operation has been tested with Python 3.12.1.
- `pip install openai`
- set your API key in the environmental variable "OPENAI_API_KEY".
- Copy the source code of the repository you want to describe entirely into target-repository-src.
- get_explanation_texts.py outputs explanation texts according to the repository’s folder structure.
- integrate_explanation_files.py combines all texts into a single file.
- !! CAUTION !!
  - As of November 17, 2024, GPT-4 Turbo (gpt-4-turbo) is being used. Reading through the entire repository to generate explanation texts consumes a significant amount of tokens.
  - Be mindful of API usage fees and execution time.