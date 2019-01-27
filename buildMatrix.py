import numpy as np
# import keygenerator as keygen
# import testPermuteLib as keygen

#convert the input(a key of type string)
def str2list(str_key):
	list_key=[]
	for i in range(len(str_key)):

		list_key.append(str_key[i])
	return list_key

#build the original 5*5 alphabet matrix
def original_matrix():
	original=[i for i in range(97,123)]
	alphebet=[chr(i) for i in original]
	alphebet.remove('j')
	#print(len(alphebet))
	w, h = 5, 5;
	matrix = [[0 for x in range(w)] for y in range(h)] 
	pos=0
	for i in range(int(len(alphebet)/5)):
		for j in range(int(len(alphebet)/5)):

			matrix[i][j]=alphebet[pos]
			pos+=1
	return matrix

#build the matrix of encryption table
def build_matrix(key):
	key=str2list(key)
	original=[i for i in range(97,123)]
	alphebet=[chr(i) for i in original]
	alphebet.remove('j')
	pos=0
	matrix=original_matrix()
	# print(matrix)
	for i in range(5):
		for j in range(5):
			if(pos==len(key)):
				break
			# print(i,j,pos)
			matrix[i][j]=key[pos]
			pos+=1

		if(pos==len(key)):
			break
	#matrix[1][1]=key[-1]

	# print(key)
	# print(key[-1])
	# print("-------")
	# print(matrix)

	
	# original=[i for i in range(97,123)]
	# alphebet=[chr(i) for i in original]
	# alphebet.remove('j')
	alphebet_pos=0
	# print("--------")
	# print("pos=",pos)
	while(pos<25):
		if(alphebet[alphebet_pos] not in key):
			matrix[(pos)//5][(pos)%5]=alphebet[alphebet_pos]
		else:
			pos-=1
		pos+=1
		alphebet_pos+=1

	# print("-----")
	# print(matrix)
	return matrix
#test build_matrix function
#build_matrix("helloworld")

#playfair encryption
#TODO
# keys=keygen.return_result()
# # print(keys[0])
# build_matrix(keys[0])


#END TODO

#playfair decryption
#TODO


#END TODO


