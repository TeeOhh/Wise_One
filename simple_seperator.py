## A simple argument mapper
## Searches for common words found in premises and conlusions

premise = ['for', 'since', 'as', 'because', 'after all']
conclusion = ['thus', 'therefore', 'so', 'hence', 'consequently', 
'it follows that', 'proves that', 'implies that', 'for this reason']

def main():
	argument = input("Argument: ")
	sentences = argument.split(". ")
	concl_candidates = list(sentences[0]).append(sentences[-1])
	conclusions = get_conclusions(sentences)
	## Assumption that premises are all sentences but the conclusion(s)...
	premises = (list (set(sentences) - set(conclusions)))
	print("---Premises---")
	print(premises)
	print("---Conclusion(s)---")
	print(conclusions)

def get_conclusions(sentences):
	conclusions = []
	for sentence in sentences:
		sentence2 = sentence.lower()
		for word in conclusion:
			if word in sentence2:
				conclusions.append(sentence)
	return conclusions

main()

