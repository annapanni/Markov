from random import randint
markov= {}
n=1

with open("hp.txt") as f:
    for sor in f:
        for betu in range(len(sor)-n):
            try:
                markov[sor[betu:betu+n]].append(sor[betu+n])
            except:
                markov[sor[betu:betu+n]]=[sor[betu+n]]
                
print(markov)
                   

def új_név(markov):
    név="_"*n
    while név[-1]!=".":
        betuk=név[-n:]
        vals=markov[betuk]
        név+=vals[randint(0,len(vals)-1)]
    új=név[n:-1]
    if len(új)<3:
        új=új_név(markov)
    return új

for i in range(10):
    print (új_név(markov))