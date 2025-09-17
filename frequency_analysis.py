import sys
from collections import Counter
import matplotlib.pyplot as plt

def frequency_analysis(text: str):
    letters = [character.lower() for character in text if character.isalpha()]
    counter = Counter(letters)
    total = sum(counter.values())
    return {key: counter[key] / total for key in counter}

def plot_frequencies(freqs: dict, sort_by_freq: bool = False):
    items = list(freqs.items())
    if sort_by_freq:
        items.sort(key=lambda x: x[1], reverse=True)
    else:
        items.sort(key=lambda x: x[0])
    letters, values = zip(*items)
    plt.figure(figsize=(10, 5))
    plt.bar(letters, values)
    plt.xlabel("Letters")
    plt.ylabel("Relative Frequency")
    plt.title("Letter Frequency Analysis")
    plt.tight_layout()
    plt.show()

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python frequency_analysis.py <file | text> [--sort]")
            sys.exit(1)

        arg = sys.argv[1]
        sort_flag = "--sort" in sys.argv
    except Exception as the_error:
        print(f"Error: {the_error}")
        sys.exit(1)

    try:
        with open(arg, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = arg

    freqs = frequency_analysis(content)
    for k, v in sorted(freqs.items(), key=lambda x: x[1], reverse=True if sort_flag else False):
        print(f"{k}: {v:.2%}")
    plot_frequencies(freqs, sort_by_freq=sort_flag)

if __name__ == "__main__":
    main()
