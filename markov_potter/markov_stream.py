from random import randint

def create_markov(filename,order):
    markov= {}
    with open(filename) as f:
        key = ''
        while True: 
            char = f.read(1)
            if char == '' : break
            try:
                markov[key].append(char)
            except:
                markov[key] = [char]
            key += char
            key = key[-order:] # keep n character for key
    return markov
                
def new_text(markov, order, db=300):
    char = ''
    par = char

    for _ in range(db):
        key = par[-order:]
        vals = markov[key]
        char = vals[randint(0, len(vals)-1)]
        par += char

    return par


#for _ in range(3): # 3 new paragraph.

n=3
m = create_markov("hp.txt",n)
print(new_text(m, n, 2000))
