def DNA_strand(dnas):
    AT, CG = set('AT'), set('CG')
    dnaReturn =[]
    for dna in dnas:
        if dna in AT:
            dnaReturn += list(AT - set(dna))
        elif dna in CG:
            dnaReturn += list(CG - set(dna))
    breakpoint()
    return ''.join(dnaReturn)

print(DNA_strand("AAAA"))
