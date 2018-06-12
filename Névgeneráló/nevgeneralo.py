from random import randint
markov= {}

with open("elf-names.txt") as f:
    for sor in f:
        sor="__"+sor.strip().lower()+"."
        betu=0
        for i in range(len(sor)-2):
            try:
                markov[sor[betu]+sor[betu+1]].append(sor[betu+2])
            except:
                markov[sor[betu]+sor[betu+1]]=[sor[betu+2]]
            betu+=1

def új_név(markov):
    név="__"
    while név[-1]!=".":
        betuk=név[-2]+név[-1]
        vals=markov[betuk]
        név+=vals[randint(0,len(vals)-1)]
    új=név[2:-1]
    if len(új)<3:
        új=új_név(markov)
    return új

for i in range(10):
    print (új_név(markov))