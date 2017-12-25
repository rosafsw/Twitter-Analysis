import sys
import json
import ast

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # initialize an empty dictionary
    scores = {}
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score  = line.split("\t") 
        # Convert the score to an integer.
        scores[term] = int(score)
    for line in tweet_file:
        data = json.loads(ast.literal_eval(line))
        sum = 0
        if "text" in data:
            content = data["text"]
            term = content.split(" ")
            for word in term:
                if word in scores:
                    sum=sum+scores.get(word)
            for word in term:
                if word not in scores:
                	print(word+" "+str(sum))

if __name__ == '__main__':
    main()
