import sys
import copy


def detector(cands, fraud):
    for fraud1 in cands:
        rest = copy.deepcopy(cands)
        rest.remove(fraud1)    
        for fraud2 in rest:
            if fraud1 + fraud2 == fraud:
                cands.remove(fraud1)
                cands.remove(fraud2)
                return cands

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

sum_fraud = sum(dwarfs) - 100

dwarfs = detector(dwarfs, sum_fraud)

dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)