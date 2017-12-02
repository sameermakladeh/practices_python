# find cuss words
import urllib

def read_text():
    quotes = open(r"C:\Users\Sameer\Desktop\movie quotes.txt")
    content = quotes.read()
    #print (content)
    quotes.close()
    return content

def check_prof(txt_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+txt_check)
    output = connection.read()
    #print (output)
    if  "true" in output:
        print "woah there buddy!"
    elif  "false" in output:
        print "Cool man"
    else:
        print "oops, nothing to fetch"
    connection.close()
txt=read_text()
check_prof(txt)