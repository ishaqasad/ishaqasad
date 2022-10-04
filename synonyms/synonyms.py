'''Semantic Similarity:
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    denom = norm(vec1) * norm(vec2)
    k1 ,k2 = list(vec1.keys()) , list(vec2.keys())
    num = 0
    for i in range(min(len(k1), len(k2) )):
        if(k1[i] in k2):
            num += vec1[k1[i]] * vec2[k1[i]]
    return(num/denom)

def build_semantic_descriptors(sentences):
    semantic_discriptors = dict()
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if(sentences[i][j].lower() in semantic_discriptors.keys()):
                for w in sentences[i] :
                    if(w.lower() in semantic_discriptors[sentences[i][j].lower()]):
                        semantic_discriptors[sentences[i][j].lower()][w.lower()] += 1
                    elif(w.lower() != sentences[i][j].lower()):
                        semantic_discriptors[sentences[i][j].lower()][w.lower()] = 1
            else:
                semantic_discriptors[sentences[i][j].lower()] = create_sen_dict(sentences[i],sentences[i][j].lower())

    return semantic_discriptors

def create_sen_dict(sentence,word):
    d = dict()
    for w in sentence:
        if w.lower() != word.lower():
            d[w.lower()] = 1
    return d

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for s in filenames:
        f = open(s,"r" ,encoding="latin1").read()
        f = f.replace("!" , ".")
        f = f.replace("?" , ".")
        f = f.replace("\n" , " ")
        f = f.split(".")
        for l in f:
            l = l.split()
            sentences.append(l)
    return build_semantic_descriptors(sentences)




def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    sim = dict()
    for w in choices:
        if(w in semantic_descriptors.keys()):
            sim[w] = similarity_fn(semantic_descriptors[word], semantic_descriptors[w])
        else:
            sim[w] = -1
    maxx = [choices[0],sim[choices[0]]]
    for k in choices:
        if(sim[k] > maxx[1]):
            maxx = [k , sim[k]]
    return maxx[0]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename,"r" ,encoding="latin1")
    line = f.readline()
    count = 0
    corr = 0
    while line  != "":
        words = line.split()
        check = most_similar_word(words[0],words[2:], semantic_descriptors, similarity_fn )
        count += 1
        if(check == words[1]):
            corr+= 1
        line = f.readline()

    return (corr / count)*100
"""
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt" , "encyclo_1.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
"""
