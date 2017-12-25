import sys
import json
import ast

def main():
    tweet_file = open(sys.argv[1])

    total_count = 0
    sums = {}
    for line in tweet_file:
        data = json.loads(ast.literal_eval(line))
        count = 1
        if "text" in data:
            content = data["text"]
            term = content.split(" ")
            for word in term:
                total_count += 1
                if word in sums:
                    sums[word] += 1
                else:
                    sums.update({word:count})
    for word, count in sums.items():
        frequecy = float(count) / total_count
        result = str(word) + " " + str(frequecy)
        print(result)

if __name__ == '__main__':
    main()
