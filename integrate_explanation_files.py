import os
# from openai import OpenAI

def main():
    # outputフォルダの中身を一つのファイルにまとめる
    output_dir = r"output"
    output_file = r"all_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                target_path = os.path.join(root, file)
                with open(target_path, "r", encoding="utf-8") as f2:
                    # フォルダ階層を名前として書きこむ
                    f.write(target_path)
                    f.write(f2.read())
                    f.write("\n")

if __name__ == '__main__':
    main()
    