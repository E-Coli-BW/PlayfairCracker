COUNT=0
RES=list()
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
	print(keys)
	keys=list(keys)
	permute(keys,0,len(keys))


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

def permute(keys,start,end):
	global COUNT
	global RES
	if(start>=end):
		temp=""
		for digit in keys:
			temp+=digit
		RES.append(temp)
		#completion=(COUNT+1)/3628800*100
		#percent=str(completion)+"%"
		#print(percent)
		#print(temp)
		#with open('keys.txt', 'a') as f:
		#	print(temp,file=f)
		COUNT+=1
	else:
		i=start
		for num in range(start,end):
			keys[num],keys[i] = keys[i], keys[num]
		
			permute(keys,start+1,end)
			keys[num],keys[i]=keys[i],keys[num]

def return_result():
	return RES
num=54302220
generateKey(num)
# print(COUNT)
# print(RES[0])
#res=return_result()
