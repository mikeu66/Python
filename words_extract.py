import re
from collections import defaultdict

f = open("moby.txt",encoding = "utf-8")
x = f.read().lower()
all_words = open("allwords.txt", "w")
unique = open("uniquewords.txt", "w")
freq = open("wordfrequency.txt", "w")
y = re.findall('[a-z]+',x)



def create_all_words(lst):
	for i in lst:
		all_words.write(i+'\n')
	all_words.close()


def create_freq(lst):
	d = defaultdict(int)
	for i in lst:
		d[i] += 1
	sort = sorted(d.items(), key=lambda x:x[1])
	for key in sort:
		p = (key[0],"  :  ", key[1])
		freq.write(key[0]+" : "+str(key[1])+'\n')
		#print(key, " :: ", d[key])


def get_unique(lst):
	d = defaultdict(int)
	for i in lst:
		d[i] += 1
	sort = sorted(d.items(), key=lambda x:x[1])
	for j in sort:
		if int(j[1]) == 1:
			#unique.write(j[0]+"  :  "+ str(j[1])+"\n")
			unique.write(j[0]+'\n')



create_all_words(y)
create_freq(y)
get_unique(y)