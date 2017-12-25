import sys
import json
import ast
import operator

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # initialize an empty dictionary
    scores = {}
    datamap = {}
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score  = line.split("\t") 
        # Convert the score to an integer.
        scores[term] = int(score)
    for line in tweet_file:
        data = json.loads(ast.literal_eval(line))
        sum = 0
        if "place" in data:
            if sum == 0:
                content = data["place"]
                if content != None:
                    country_code = content["country_code"]
                    if (country_code == "US"):
                            full_name=content["full_name"]
                            terms=full_name.split(", ")
                            t=terms[1]
                            if "text" in data:
                                content2 = data["text"]
                                term2 = content2.split(" ")
                                for word in term2:
                                    if word in scores:
                                        sum=sum+scores.get(word)
                            if t in datamap:
                                datamap[t]=(float(datamap[t])+sum)/2
                            else:
                                datamap.update({t:sum})
    print(max(datamap.items(), key=operator.itemgetter(1))[0])  

if __name__ == '__main__':
    main()
