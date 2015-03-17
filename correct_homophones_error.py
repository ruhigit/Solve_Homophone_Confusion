import nltk
import sys
import re
import pickle
#sys.path.insert(0, "..")
from perceplearn import perceptron
##The feature_vector is the model that will be used to calculate the classes
##Testset is a list of sentnces that have to be tagged with the right class.

predefined_list=['it\'s','its','you\'re','your','they\'re','their','loose','lose','to','too']

def classify(feature_vector,sentence):
	##print(sentence)
	
	weight_class1=0
	weight_class2=0
	words=sentence.split()
	tag=int(words[0])
	class1=predefined_list[tag*2]
	class2=predefined_list[(tag*2)+1]
	##print(class1)
	##print(class2)
	for word in words:
		if word in feature_vector[class1]:
			##if the word has a non-zero value add it
			weight_class1+=feature_vector[class1][word]
		elif word in feature_vector[class2]:
			##if the word has a non-zero value add it
			weight_class2+=feature_vector[class2][word]

		if(weight_class1>weight_class2):
			predicted_class=class1	
		else:
			predicted_class=class2
			
	return predicted_class
def format_file(words,index):
	##print(index)
	##print(words)
	## The list of word-tag pairs are words
	curr=words[index][0]
	curr=curr.lower()
	##print(curr)
		##If we find a word amongst the 10 predefined words,we build a sentence
	if curr in predefined_list:
		index_found=predefined_list.index(curr)	
		##Boundary condition begining of sentence
		if index==0 or words[index-1]=="B":
			##if first word then previous word is BOS and prev-1 is BOS_1
			prev="BOS"
			prev_1="BOS_1"
			prevtag="BTAG"                         
			prev_1_tag="BTAG1"
	
		elif words[index-2]=="B":
			##for second word prev-1 is BOS_1
			prev=words[index-1][0]
			prev_1="BOS_1"
			prevtag=words[index-1][1]
			prev_1_tag="BTAG1"
					
		##All other words
		else:
			prev=words[index-1][0]
			prev_1=words[index-2][0]
			prevtag=words[index-1][1]
			prev_1_tag=words[index-2][1]
					
		##Boundary condition end of sentence
		if words[index+1]=="E":
			##if last word then next word is EOS and next+1 word is EOF_1
			next="EOF"
			next_1="EOF_1"
			nexttag="ETAG"
			next_1_tag="ETAG1"
	
		elif words[index+2]=="E":
			##if second last word then next+1 word is EOF_1
			next=words[index+1][0]
			next_1="EOF_1"
			nexttag=words[index+1][1]
			next_1_tag="ETAG1"
					
	
		##All other words
		else:
			next=words[index+1][0]
			next_1=words[index+2][0]
			nexttag=words[index+1][1]
			next_1_tag=words[index+2][1]
				
				
		sentence="prev:%s prevtag:%s prev_1:%s prev_1_tag:%s next:%s nexttag:%s next_1:%s next_1_tag:%s" %(prev,prevtag,prev_1,prev_1_tag,next,nexttag,next_1,next_1_tag)
		tag=int(index_found/2)
		sentence=str(tag)+" "+sentence	
	
	return sentence
			
def main():
	tagged_words=list()
	if len(sys.argv) != 4:
		print ('usage: python3 correct_homophones_error.py Modelfile Testfile Outputfile')
		sys.exit(1)
	op=open(sys.argv[3],"w")
	##The 2nd argument contains the list of words along with its tag
	i=0
	while i<5:
		##print(trainingset[i])
		modelfile=open(sys.argv[1]+"_"+str(i),"rb")
		tagged_words.append(pickle.load(modelfile))
		modelfile.close()
		i+=1
	##print(len(tagged_words))
	testfile=open(sys.argv[2],"r")
	for line in testfile:
		words=line.split()
		for index,word in enumerate(words):
			curr=word.lower()
			if curr in predefined_list:
				tagged=list()
				##print(word)
				tag_index=int(predefined_list.index(curr)/2)
				##print(index)
				tagged.append("B")
				tagged+=nltk.pos_tag(words)
				tagged.append("E")
				##print(tagged)
				testsentence=format_file(tagged,index+1)
				##print(testsentence)
				curr=classify(tagged_words[tag_index],testsentence)
				##print(curr)
				if word.isupper():
					word=curr.upper()
				elif word[0].isupper():
					##print(word)
					word=curr.capitalize()
					##print(word)
				else:
				 	word=curr
			op.write(word)
			op.write(" ")
		op.write("\n")
	op.close()
	return
	
if __name__=="__main__":
	main()
