import os
from openai import OpenAI

def get_explanation_texts(openai_client, target_file_path):
    """
    指定されたファイルのgpt-4o-miniによる自然言語説明を取得します。
    """
    with open(target_file_path, "r", encoding="utf-8") as f:
        trial_file = f.read()
        # 3. ファイルの自然言語説明を取得
        prompt_prefix = "これから提供するファイルについて日本語で簡潔に解説してください。 \
                            クラスやメソッドなど主要な要素について漏れなく記述してください。 \n "
        prompt = prompt_prefix + trial_file
        chat_completion = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o-mini",
        )
    return chat_completion.choices[0].message.content

def recreate_folder_structure(src_dir, dest_dir):
    """
    指定されたフォルダの構造を別のフォルダに再現します。
    
    :param src_dir: 元のフォルダのパス
    :param dest_dir: フォルダ構造を再現する先のパス
    """
    for root, dirs, files in os.walk(src_dir):
        # 相対パスを計算して、新しいフォルダに適用
        relative_path = os.path.relpath(root, src_dir)
        target_path = os.path.join(dest_dir, relative_path)
        
        # フォルダを作成
        os.makedirs(target_path, exist_ok=True)


def main():
    # openaiのapiを用いてあるフォルダ以下の全てのファイルを自然言語で説明したテキストファイルを出力する
    # 1. APIキーを環境変数から取得
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )
    # 2. フォルダの読み込み
    base_target_dir = r"target-repository-src"
    output_dir = r"output"
    # 3. フォルダ階層をoutputフォルダ内に構築
    recreate_folder_structure(base_target_dir, output_dir)

    # 4. 自然言語説明を取得しファイルに保存
    # フォルダ内の全てのファイルを取得
    for root, dirs, files in os.walk(base_target_dir):
        for file in files:
            target_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, base_target_dir)
            output_file_dir = os.path.join(output_dir, relative_path)
            # ファイル末尾の拡張子部分のみ_description.txtに置き換える
            basename_without_ext = os.path.splitext(os.path.basename(target_path))[0]
            output_file_name = basename_without_ext +  "_description.txt"
            output_file_path = os.path.join(output_file_dir, output_file_name)

            chat_completion_content = get_explanation_texts(client, target_path)
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(chat_completion_content)


if __name__ == "__main__":
    main()
