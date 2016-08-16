import re

def countWords():
    val="350 Downing Street dunno who is going to the Downing Street 250 again "
    wordre=re.compile('\w+')
    list={}

    for word in wordre.findall(val):
        if word in list:
            list[word]+=1
        else:
            list[word]=1

    print "Count of Words :",list

def testStr():
    st=['edefdfd','ddd','a','bb','zzzz','fdfdfdf']
    print sorted(st,key=len)

testStr()
