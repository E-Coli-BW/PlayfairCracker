import buildMatrix 
import numpy as np 

#Build the index dictionary for lookup
def prepareDict(file):
	dictionary={}
	# file="index.txt"
	with open(file) as f:
		for word in f:
			#print(word)
		# word=f.readline()
			if len(word)-1 in dictionary:
				word_list=dictionary.get(len(word)-1)
				word_list.append(word[:len(word)-1])
			else:
				dictionary[len(word)-1] = [word[:len(word)-1]]
	# print(dictionary.keys())
	# print(dictionary[4])

	return dictionary
dictionary=prepareDict("index.txt")

def getPos(letter,matrix):
	for j in range(5):
		for i in range(5):
			if letter==matrix[i][j]:
				return [i,j]

def decrypt(key,msg):
	#given key='key'
	#      msg='lyxaxgda'
	#output should be mesxsage
	key=list(key)
	msg=list(msg)
	# print(msg)
	matrix=buildMatrix.build_matrix(key)

	# print(matrix)
	i=0

	while(i<=len(msg)-2):
		letter1=msg[i]
		letter2=msg[i+1]
		pos1=getPos(letter1,matrix)
		pos2=getPos(letter2,matrix)
		#Same row
		if pos1[0]==pos2[0]:
			letter1=matrix[pos1[0]][pos1[1]-1]
			letter2=matrix[pos2[0]][pos2[1]-1]
		#same col   
		elif pos1[1]==pos2[1]:
			letter1=matrix[pos1[0]-1][pos1[1]]
			letter2=matrix[pos2[0]-1][pos2[1]]
		#diagonal
		else:
			letter1=matrix[pos1[0]][pos2[1]]
			letter2=matrix[pos2[0]][pos1[1]]
		msg[i]=letter1
		msg[i+1]=letter2
		i+=2
	return msg
COUNTER=0
CANDIDATE_KEYS=[]
# print(decrypt("iowrtuefvhz","hddoewtretqfqbqabdiotkqbyndvdkkuqbynkrhfkvyhywkquqkbavhdhqbqqftiiwafbdzeqftgbodqzfhywitghdwpobpthkwitghdfodqtgtfrzutiopwwykdihoviwafbdzeqfewtietqftfwqqukqweovbqtkwtvwouynyfuibmbqywufqfdbfpfqbqkitaywuftntkwixqaknewrfhvobqwudkthutgkhddovqwpwyuohdvovqwpohatvmckuoyhwauogkewtiufqbqawehdfqfahibqwukrhfkvyhxyywcoohbhtwnrufqf"))
all_words=dictionary.values()
big_list_all_words=[]
for word_list in all_words:
	for word in word_list:
		big_list_all_words.append(word)

def filtering(res,i,CANDIDATE_KEYS):
	FOUND_ONE=False
	FOUND_TWO=False
	RES="".join(res)
	# print("Decrypted result is:",RES)

	# print("All words:")
	# print(all_words)
	# print("All words in one single list:")
	# print(big_list_all_words)
	for word in big_list_all_words:
		# print("word is:")
		# print(word)
		# str_word=""
		# for letter in word:
		# 	str_word+=letter
		# print(word)
		# if(len(word)>=4):
		if(len(word)<=2):
			continue
		first_index=RES.find(word)


		if(first_index!=-1):
			# print(word)
			# print(RES)
			# print("first word found is:",word)
			# print(RES)
			# print("at index:",first_index)
			next_starting_index=first_index+len(word)
			# print(RES[first_index:next_starting_index])		
			# temp_res=RES
			RES=RES[next_starting_index:]
			# if(temp_res==word)
			# if(word=="that" and RES[:3]=="for"):
			# 	print(RES)
			FOUND_ONE=True
			# print(i)
			# print(word)
	# print(FOUND_ONE)		
			if(FOUND_ONE):
				for word in big_list_all_words:
					if(len(word)<=2):
						continue
					first_index=RES.find(word)

					if(first_index!=-1):
						next_starting_index=first_index+len(word)
						RES=RES[next_starting_index:]
						FOUND_TWO=True
						print("Second word is:",word)
						if(FOUND_TWO):

							for word in big_list_all_words:
								if(len(word)<=2):
									continue
							# if(FOUND_ONE):
								# if(len(word)>=3):
								if(RES.find(word)!=-1):
									print("third word is:",word)
									CANDIDATE_KEYS.append(i)
									return


	# for dict_key in dict_keys:
	# 	# print(dict_key)
	# 	# print(type(dict_key))
	# 	if(dict_key>=4):
	# 		words=dictionary[dict_key]
	# 		print(words)
	# 		for word in words:
	# 			if(RES.find(word)!=-1):
	# 				found+=1
			# totalWords=len(words)
			# word_find_start=-1
			# while(len(words)!=0 and word_find_start<len(words)-1):
			# 	word_find_start+=1
			# 	print("start finding first word at index:",word_find_start)
			# 	# print(word_find_start)		
			# 	if(RES.find(words[word_find_start])!=-1):
			# 		first_word=words[word_find_start]
			# 		beg=RES.find(words[word_find_start])
			# 		# RES=RES[beg:]
			# 		word_find_start+=1
			# 		print("found at least one word",first_word,"now find second one,starting index is:",word_find_start)	
			# 		if(RES.find(words[word_find_start])!=-1):
			# 			CANDIDATE_KEYS.append(i)
			# 			break

dict_keys=dictionary.keys()
encrypted_file="8_x2.txt"
#Read the file store in a string then keep that 
with open(encrypted_file,'r') as f:
	text=f.readline()
	if not text:
		f.close()

LENGTH_OF_TEXT=20
# print(text)

keys=[]
with open("second_filter.txt",'r') as f:
	lines=f.readlines()
	for line in lines:
		# print(type(line))
		# print(line)
		# print("read as:",line[:len(line)-1])
		keys.append(line[:len(line)-1])
	# print(keys)
		
f.close()

		
print(len(keys))
if("iowrtuefvhz" in keys):
	print("Correct Key exists in second_filter.txt")
for i in keys:
	COUNTER+=1
	#Always use the same string for decryption
	c=text[:LENGTH_OF_TEXT]
	res=decrypt(i,c)
	global RES
	RES=""
	filtering(res,i,CANDIDATE_KEYS)
print(len(CANDIDATE_KEYS))


# msg='hddoewtretqfqbqabdiotkqbyndvdkkuqbynkrhfkvyhywkquqkbavhdhqbqqftiiwafbdzeqftgbodqzfhywitghdwpobpthkwitghdfodqtgtfrzutiopwwykdihoviwafbdzeqfewtietqftfwqqukqweovbqtkwtvwouynyfuibmbqywufqfdbfpfqbqkitaywuftntkwixqaknewrfhvobqwudkthutgkhddovqwpwyuohdvovqwpohatvmckuoyhwauogkewtiufqbqawehdfqfahibqwukrhfkvyhxyywcoohbhtwnrufqf' #movements

# print("Decryption:",decrypt("".join(CANDIDATE_KEYS[0]),msg))
with open("third_filter_back_up.txt",'w') as f:
	for key in CANDIDATE_KEYS:
		key="".join(key)
		f.write(key)
		f.write('\n')
f.close()