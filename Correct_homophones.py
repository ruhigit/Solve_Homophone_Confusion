
import sys
import re
import pickle
#sys.path.insert(0, "..")
from perceplearn import perceptron

def format_file(words):
	## The list of word-tag pairs are words
	op=[[],[],[],[],[]]
	predefined_list=['it\'s','its','you\'re','your','they\'re','their','loose','lose','to','too']
	
	for index,word in enumerate(words):
			
		curr=words[index][0]
		##If we find a word amongst the 10 predefined words,we build a sentence
		curr=curr.lower()
		if curr in predefined_list:
			list_index=predefined_list.index(curr)	
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
			tag=curr
			sentence=tag+" "+sentence
			pos=int(list_index/2)
			op[pos].append(sentence)
			##print(sentence)
	
	return op
			
def main():
	
	if len(sys.argv) != 3:
		print ('usage: python3 correct_homophones.py Tagged_Inputfile Output_Modelfile')
		sys.exit(1)
	
	##The 1st argument contains the list of words along with its tag
	taggedfile=open(sys.argv[1],"rb")
	tagged_words=pickle.load(taggedfile)
	taggedfile.close()
	
	trainingset=format_file(tagged_words)
	##print(trainingset)
	i=0
	while i<5:
		##print(trainingset[i])
		perceptron(trainingset[i],sys.argv[2]+"_"+str(i))
		i+=1
	return
	
if __name__=="__main__":
	main()
