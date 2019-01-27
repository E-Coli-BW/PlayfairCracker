# notations 
# PF_E(K,P) => Encrypt plaintetxt P using Playfair with key K
# PF_E(K,[P]) => Encrypt plaintetxt in file [P] using Playfair with key K
# PF_D(K,C) => Decrypt cyiphertext C using Playfair with key K
# PF_D(K,[C]) => Decrypt cyiphertext in file[C] using Playfair with key K

#implement Playfair Cipher

import buildMatrix 
# import keygenerator as keygen
#import testPermuteLib as keygen
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
	print(dictionary.keys())
	print(dictionary[4])

	return dictionary
dictionary=prepareDict("index.txt")

# print(dictionary)

# keys=keygen.return_result()
# matrix=buildMatrix.build_matrix(keys[0])
# print(matrix)

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


# import itertools
# COUNT=0
# RES=list()
def generateKey(num):
	temp=[]
	while(num!=0):
		temp.append(num%10)
		num=num//10
	#print(temp)
	num=temp
	keys=""
	for digit in num:
		keys+=" "
		keys+=(to_english(digit))
	#print(keys)
	keys=set(keys.split())
	# print(keys)
	keys=list(keys)
	#print(keys)
	# res=list()
	# for i in itertools.permutations(keys,11):
	#   res.append(i)
	return keys

def to_english(digit):
	if digit==1:
		return "o n e"
	if digit==2:
		return "t w o"
	if digit==3:
		return "t h r e e"
	if digit==4:
		return "f o u r"
	if digit==5:
		return "f i v e"
	if digit==6:
		return "s i x"
	if digit==7:
		return "s e v e n"
	if digit==8:
		return "e i g h t"
	if digit==9:
		return "n i n e"
	if digit==0:
		return "z e r o"
	else:
		print ("error!")

import itertools
keys=generateKey(54302220)

# msg=decrypt('key','lyxaxgda')
# print(msg)
#print(keys)
#Write a program to find substrings
#Read 10 chars per time, decrypt it using every keys you have
#If the decrypted one matches the dictionary
#Store it as potential key
#After one round
#Read 20 chars per time, decrypt it using every potential keys
#If the decrypted one matches the dictionary
#Store it as new potential key
#Keep doing it until the key sapce is narrow enough!


# msg='krhfkvyhy' #movements
# res=decrypt('abcdzklmngqsxypowrtiefvhu',msg)
# print(res)
# msg='lyxaxgda'
# res=decrypt('key',msg)
# print(res)
# print(res in dictionary[4])
# print(dictionary[9])

COUNTER=0
# global CANDIDATE_KEYS
CANDIDATE_KEYS=[]
# print(type(CANDIDATE_KEYS))
#RES=""
def filtering(res,i,CANDIDATE_KEYS):
	RES="".join(res)
	# for letter in res:
	# 	# print("letter in res is :",letter)
	# 	RES=""
	# 	RES+=letter
		
	for dict_key in dict_keys:
		# print(dict_key)
		# print(type(dict_key))
		if(dict_key>=4):
			words=dictionary[dict_key]
			for word in words:
				# print(word)
				# print(RES)
				
				if(RES.find(word)!=-1):
					# print(i)
					# print(word)
					# global CANDIDATE_KEYS
					# print(type(CANDIDATE_KEYS))
					# print("keys",i)
					# print(i)
					__KEY="".join(i)
					if(__KEY.find("iowrtuefvhz")!=-1):
						
						print(i)

					CANDIDATE_KEYS.append(i)
					return
					# print(CANDIDATE_KEYS)
					# if(COUNTER>100000 and COUNTER%100000==0):
					# 	print(COUNTER/39916800.0*100,"% Searched")
					# 	print(len(CANDIDATE_KEYS))
						#print (CANDIDATE_KEYS)


#I think the problem lies in that I cannot make the 
#file reopened and read from start agian to test other keys
dict_keys=dictionary.keys()
encrypted_file="8_x2.txt"
# with open(encrypted_file,'r') as f:
# 	#for i in range(1,3):
# 	while True:
# 		for i in itertools.permutations(keys,11):
# 			c=f.read(10)
# 			# print(c)
# 			if not c:
# 				f.close()
# 				break			
# 			# print(i)
# 			COUNTER+=1
# 			print(COUNTER)
# 			if(COUNTER>100 and COUNTER%100==0):
# 				progress=(COUNTER/39916800.0)*100
# 				print("{:2.2%} % Searched".format(progress))
# 				print(len(CANDIDATE_KEYS))
# 			res=decrypt(i,c)
# 			global RES
# 			RES=""
# 			filtering(res,i,CANDIDATE_KEYS)
# f.close()

# test writing to file
# with open("first_filter.txt",'w') as f:

# 	key="".join(['1','2','3'])
# 	f.write(key)
# 	f.write('\n')
# f.close()


#Read the file store in a string then keep that 
with open(encrypted_file,'r') as f:
	text=f.readline()
	if not text:
		f.close()

LENGTH_OF_TEXT=10
print(text)
key="iowrtuefvhz"
key=tuple(key)
print(type(key))
print(key)
for item in itertools.permutations(keys,11):
	print(type(item))
	print(item)
	break
if(key in itertools.permutations(keys,11)):
	print("Exist")
else:
	print("Not found")
for i in itertools.permutations(keys,11):
	COUNTER+=1
	#Always use the same string for decryption
	c=text[:LENGTH_OF_TEXT]
	# print("c is:",c)

	# with open(encrypted_file,'r') as f:
	# 	while True:
	# 		c=f.read(10)
	# 		if not c:
	# 			f.close()
	# 			break
	# if(COUNTER>100000 and COUNTER%100000==0):
	# if(COUNTER>100000 and COUNTER%100000==0):
		# progress=(COUNTER/39916800.0)*100
		# progress=(COUNTER/3.0)*100
		# print(progress)
		# print("{:2.2%} % Searched".format(progress))
		# if(len(CANDIDATE_KEYS)>0):
		# if(len(CANDIDATE_KEYS)>0 and len(CANDIDATE_KEYS)%10==0):
			# print(len(CANDIDATE_KEYS))
			# print("COUNTER=",COUNTER)
		# print(len(CANDIDATE_KEYS))
	res=decrypt(i,c)
	global RES
	RES=""
	filtering(res,i,CANDIDATE_KEYS)
print(len(CANDIDATE_KEYS))
with open("first_filter.txt",'w') as f:
	for key in CANDIDATE_KEYS:
		key="".join(key)
		f.write(key)
		f.write('\n')
f.close()




'''
		WORDLENGTH=3
		while(WORDLENGTH<4):
			for i in itertools.permutations(keys,11):
				res=decrypt(i,c)
				#print(res)
				j=0
				
				while(j<len(res)-WORDLENGTH):
					__res=res[j:j+WORDLENGTH]
					if(__res in dictionary[WORDLENGTH]):
						print(i)
						print(__res)
						break
					j+=1
			WORDLENGTH+=1
'''





# res=decrypt(i,msg)
# RES=""
# for letter in res:
#   RES+=letter
# # for subword in RES:
# #     subword=
# if(RES in dictionary[9]):
#   print(i)
#   print(res)

# print(keys)
# msg='hddoew'

# for key in keys:
#   res=decrypt(key,msg)
#   if res in dictionary.values():
#       print(key)
#       print(res)

# #A simple test // should print out message
# msg='lyxaxgda'
# res=decrypt('key',msg)
# print(res)