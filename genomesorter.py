import csv

def prep(genome):
    genome = genome.split(':')[0]
    if "_" in genome:
        s = "_"
    else:
        s = "-"
    
    gs = genome.split("s")
    if gs[-1].isdigit():
        genome = genome[:-1*(len(gs[-1])+1)]
    return genome

with open('g2fgenome.txt') as tsv:
    lines = [line.strip().split('\t') for line in tsv]
    
    names = {}
    genes = {}

    for line in lines[1:]:
        name = prep(line[0])
        ns = []
        for i in range(1, len(line)):
            ns.append(1 if line[i] == 'N' else 0)
        ns = sum(ns)
        try:
            acc = ((len(line)-1)-ns)/((len(line)-1))
        except ZeroDivisionError:
            acc = 0.0
        

        if name in names.keys():
            if names[name] > acc:
                genes[name] = line[1:]
                names[name] = acc
                
        else: 
            names[name] = acc
            genes[name] = line[1:]

with open ('converted.txt', 'w') as f:
    f.truncate()
    # '\t'.join(genes[name])
    f.write('\t'.join(lines[0]))
    for k in genes.keys():
        f.write(k+'\t'+'\t'.join(genes[k]))