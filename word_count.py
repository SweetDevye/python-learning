import sys

def word_count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"文件 {filename} 未找到")
        return

    words = text.split()
    freq = {}
    for word in words:
        word = word.lower().strip('.,!?";:')
        freq[word] = freq.get(word, 0) + 1

    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python word_count.py <文件名>")
    else:
        word_count(sys.argv[1])
