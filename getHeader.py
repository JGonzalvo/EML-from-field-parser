from email import message_from_file
import os
import base64

root=os.path.dirname(os.path.abspath(__file__))
dst = root + '\\Mails\\'

fo = open("output.txt","w+")

def extract (msgfile, key):
    m = message_from_file(msgfile)
    tempHeader = caption(m)

    return tempHeader

def caption (origin):
    tempHeader = ""
    if origin.has_key("From"): 
		tempHeader = origin["From"].strip()
    return tempHeader
	
def convert (tempHeader):
	tempHeader=tempHeader.split("<")[-1]
	#tempHeader = base64.b64decode(tempHeader)
	tempHeader=tempHeader[:-1]
	return tempHeader
	
def temp(x):
	
	
	return temp
	
for i in os.listdir(dst):
	if i.endswith(".eml"):
		dstMails = root + '\\Mails\\' + i
		f = open(dstMails, "rb")
		header = extract(f, f.name)
		header = convert(header)
		print header
		fo.write(header + '\n')
		f.close()

fo.close()
	

