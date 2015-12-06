## Author: Jessy Li (ljunyi@seas.upenn.edu)

from nltk.tokenize import sent_tokenize, word_tokenize
import speciteller

def multisent_specificity(sentlst):
    '''Specificity of more than one sentence is:
    first each word has specificity of its sentence
    then take the average word specificity
    '''
    tkns = 0.0
    spec = 0.0
    preds = speciteller.run("sents", sentlst)
    for (s, p) in zip(sentlst, preds):
        ntkn = float(len(s.split()))
        spec += p*ntkn
        tkns += ntkn
    return spec/tkns

def run_text(inputfile, do_sent_tokenization, do_word_tokenization):
    '''an interface for running an article
    '''
    prep = []
    with open(inputfile) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                if do_sent_tokenization:
                    prep.extend(sent_tokenize(line))
                else:
                    prep.append(line)
    sents = []
    for prepsent in prep:
        if len(prepsent) > 0:
            if do_word_tokenization:
                sents.append(" ".join(word_tokenize(prepsent)))
            else:
                sents.append(prepsent)
    return multisent_specificity(sents)

if __name__ == "__main__":
    print run_text("/nlp/users/louis-nenkova/corpus-v2/BST-goodAvgBad-research/1999_01_03_1074147.txt", True, True)
