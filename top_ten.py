import sys
import json
import ast
import operator

def main():
    dic = {}
    count = 1

    tweet_file = open(sys.argv[1])

    for line in tweet_file:
        data = json.loads(ast.literal_eval(line))
        sum = 0
        if "entities" in data:
            entities = data["entities"]
            hash_tag = entities["hashtags"]
    
            for data in hash_tag:
                hash_tag2 = data["text"] 
                if hash_tag2 in dic:
                    dic[hash_tag2]+= 1
                else:
                    dic.update({hash_tag2:count}) 
    sorts = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    i = 0
    for k in sorts:
        i = i+1
        if i <= 10:
            print(k[0]+"\t"+str(k[1]))

if __name__ == '__main__':
    main()
