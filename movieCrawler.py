# -*- coding: utf-8 -*-
import sys, codecs
import urllib2


output = open('data.txt', 'a')

cache = ""
num = 10000
while num < 100000 :
	

	try:
		page=urllib2.urlopen('http://movie.mtime.com/'+str(num)).readline()
		endpos = page.find("</title>")
		cache += str(num)+"   "+page[184:endpos]+"\n"
		#output.writelines(str(num)+"   "+page[184:endpos]+"\n")
		num = num+1
	except:
		num = num+1


	if(num%100==0):
		output.writelines(cache)
		cache = ""
		

if cache != "":
	output.writelines(cache)


output.close()

#print page
