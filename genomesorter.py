import csv
import re

def prep(genome):
    split_genome = genome.replace(":"," ").replace("-"," ").replace("_"," ").split()
    genome = []
    
    
    potential_name = []
    for chunk in split_genome:
        if re.search('[a-zA-Z]', chunk):
            potential_name.append(chunk)
            genome = genome+potential_name
            potential_name = []
        else:
            potential_name.append(chunk)

    genome = '_'.join(genome)
    return genome

with open('genome.txt') as tsv:
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
    #This is generally fine, contains header data
    f.write('\t'.join(lines[0]))
    for k in genes.keys():
        if k == "":
            pass
        else:
            f.write('\n'+k+'\t'+'\t'.join(genes[k]))
