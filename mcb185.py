
def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#gc content
def gc(dna):
	g = dna.count('G')
	c = dna.count('C')
	return (g + c)/len(dna)
	

	
def n50(length)
	length.sort()
	running_sum = 0
	total = sum(length)
	for value in length :
		running_sum += value
		if running-sum > total/2 :
			return value
			break