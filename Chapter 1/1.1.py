print("*** Converting hh.mm.ss to seconds ***")
print("Enter hh mm ss :", end = " ")
t = list(map(int, input().split(' ')))
output=t[0]*3600+t[1]*60+t[2]
for i in range(len(t)):
	if t[i] >= 60 or t[i]<0:
		print("mm("+"{:02d}".format(t[i])+") is invalid!")
		exit()
print("{:02d}".format(t[0])+":"+"{:02d}".format(t[1])+":"+"{:02d}".format(t[2])+" =","{:,}".format(output),"seconds")
