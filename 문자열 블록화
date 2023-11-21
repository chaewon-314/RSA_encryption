a=str(input())                               #블록화할 문자열 입력
n=0                                         #인덱싱용 상수
blockN=2                                 #blockN은 한 block당 문자 수
b=[]                                        #블록화한 문자열 저장 리스트
l=''                                        #블록-숫자 변환 매개변수

#dic={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35}
dic={'~':27,' ':26,'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,
     'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
     'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
#dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

# Sbox={}

# n=1
# for x1 in range(97,123):
#     for x2 in range(97,123):
#         for x3 in range(97,123):
#             for x4 in range(97,123):
#                 k=str(str(chr(x1)))+str(chr(x2))+str(chr(x3))+str(chr(x4))
#                 Sbox[n]=k
#                 n+=1
# print(Sbox)
                
#문자열을 블록화
n=0
while True:
    b.append(a[n:n+blockN])
    n+=blockN
    if n>=len(a):
        break

print(b)

#b의 마지막 항이 blockN보다 짧을때 항 앞에 ~추가하여 길이 조절
lastB=b[len(b)-1]
lastB='~'*(blockN-len(lastB))+lastB
b[len(b)-1]=lastB




#블록을 숫자로 변환
for x in range(len(b)):
    k=b[x]
    l=0
    for y in range(blockN):
        l+=dic[k[y]]*(len(dic)**(blockN-(y+1)))
    b[x]=l
    
print(b)

#블록화한 문자열 값을 blocked_str.txt파일에 저장
f=open('blocked_str.txt','w')
for x in range(len(b)):
    f.write(str(b[x])+'\n')
f.close()



# try:
#     for x in range(len(b)):
#         k=b[x]
#         k=dic[k[0]]*(len(dic)**3)+dic[k[1]]*(len(dic)**2)+dic[k[2]]*(len(dic)**1)+dic[k[3]]     #26진법 사용
#         b[x]=k
# except:
#     if len(b[len(b)-1])==1:
#         b[len(b)-1]=('~'*(blockN-1)+b[len(b)-1])
#         k=b[len(b)-1]
#         k=dic[k[0]]*(len(dic)**3)+dic[k[1]]*(len(dic)**2)+dic[k[2]]*(len(dic)**1)+dic[k[3]]
#         b[len(b)-1]=k
        
#     elif len(b[len(b)-1])==2:
#         b[len(b)-1]=('~'*(blockN-2)+b[len(b)-1])
#         k=b[len(b)-1]
#         k=dic[k[0]]*(len(dic)**3)+dic[k[1]]*(len(dic)**2)+dic[k[2]]*(len(dic)**1)+dic[k[3]]
#         b[len(b)-1]=k
        
#     elif len(b[len(b)-1])==3:
#         b[len(b)-1]=('~'*(blockN-3)+b[len(b)-1])
#         k=b[len(b)-1]
#         k=dic[k[0]]*(len(dic)**3)+dic[k[1]]*(len(dic)**2)+dic[k[2]]*(len(dic)**1)+dic[k[3]]
#         b[len(b)-1]=k
# print(b)

# f=open('blocked_str.txt','w')       #블록화한 문자열 값을 blocked_str.txt파일에 저장
# for x in range(len(b)):
#     f.write(str(b[x])+'\n')
# f.close()
