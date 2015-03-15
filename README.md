# Solve_Homophone_Confusion
Error detection and correction: dealing with homophone confusion

##Error detection and correction: dealing with homophone confusion##

####Approach:####

#####In short:######
The homophone confusion can be solved using the surrounding part-of-speech tags and detecting the correct word.
The training file is tagged using nltk-pos tagger. The previous 2 words, their tags, next 2 words and their tags are the features while the current word is the class. 
5 model files will be created for each category of homophone.
The testfile will be again pos-tagged and the class will be detected.

#####Step-by-step explanation:#####

Training data:Brown corpus from NLTK.
The brown corpus directory is first converted into one training file createTrainingfile.py which reads individual file from the directory,chops the tags and creates one file brown_training.txt.
Tagfile.py: This program uses nltk pos tagger to tag a file. We therefore create tagged_training.txt using this program.
Correct_homophones.py: This code takes the tagged training file as input, formats it and calls perceplearn to make 5 model files for each homophone pair.
Correct_homophones_error.py: This code takes the model file as input, testfile to be corrected and gives the corrected test file as output.
#####How to run the code:#####

__To create model file__:
If the training data is already tagged, run :
Command1:
	python3 create_Trainingfile.py inputDir
brown_training.txt will be the output.

Command2:
	python3 tagfile.py inputfile_toTag Output_taggedfile
This will produce the pos-tagged file using nltk pos-tagger

Command3:
	 python3 correct_homophones.py Tagged_Inputfile Output_Modelfile
Will create 5 model files. 

__To correct given testfile__:

Command:
	python3 correct_homophones_error.py Modelfile Testfile Outputfile


Third-party software used: NLTK toolkit

