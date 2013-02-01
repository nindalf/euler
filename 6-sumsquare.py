limit = 100

squares = [i*i for i in range(1, limit+1)]
sumsquares = sum(squares)

sequence = [i for i in range(1, limit+1)]
sumseq = sum(sequence)

print(sumsquares - sumseq*sumseq)
