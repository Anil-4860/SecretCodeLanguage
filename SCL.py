#write a python program to translate a message into secret code language.Use therules
#below to translate normal English into secrete code language.
#cooding:
#if the word containing at least 3 charaacter,remove the first letter and append it
#at the end.
#now append three random character at the starting and the end
#else:
#  simply reverse the string

#Decoding
#if the word contains less than 3 character,reverse it
#else:
#  remove the three characters from start and end. Now remove the last letter and append
# it to the begning

#Your program should ask whether you want to code or decode
#coding
smessage=input("enter your string:")
words=smessage.split()
for word in words:
   if len(word)>=3:
     word=word[1:]+word[0]
     x="wxz"
     y="xzv"
     word=x+word[0:]+y
     #print(word,end=" ")
   else:
     if len(word)==2:
       word=word[1]+word[0]
     else:
       word=word[0]
   print(word,end=" ")
print()

#decoding
message=input("enter your message for coding:")
words=message.split()
for word in words:

 if len(word)<=2:
   if len(word)==2:
     word=word[1]+word[0]
   else:
     word=word[0]
 else:
    word=word[3:-3]
    word=word[-1]+word[0:-1]
 print(word,end=" ")

st=input("enter your mesage:")
words=st.split()
coding=input("1 for coding 0 for decoding:")
coding=True if (coding=="1") else False
print(coding)
if (coding):
  nwords=[]
  for word in words:
    if len(word)>=3:
      r1=input("enter your first random string:")
      r2=input("enter your second random string:")
      stnew=r1+word[1:]+word[0]+r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
else:
  nwords=[]
  for word in words:
    if len(word)>=3:
      stnew=word[-4]+word[3:-4]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))