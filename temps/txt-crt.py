import os

def main():
    src_file = ""   # 源文件
    target_dir = ""   # 输出文件夹

    # 创建目标文件夹
    os.makedirs(target_dir, exist_ok=True)

    # 读取源文件
    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 按空白字符分割 为数组
    tokens = content.split()   # ["zz", "xx", "cc"]

    # 为每个字符串创建 对应名称的txt
    for token in tokens:
        filename = f"{token}.txt"
        path = os.path.join(target_dir, filename)

        # 创建空文件
        with open(path, "w", encoding="utf-8") as f:
            pass

        print(f"Created: {path}")

if __name__ == "__main__":
    main()