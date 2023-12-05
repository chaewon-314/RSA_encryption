boolean=1
blockN=2
l=''
string=''


# dic={'~':28,' ':27,'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,
#      'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
#      'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
dic='abcdefghijklmnopqrstuvwxyz ~'                  #알파벳 대응표

f=open('dec.txt','r')


while boolean:
    a=f.readline()         #a는 dec.txt 파일을 한줄씩 입력받음
    
    if str(a)=='':              #블록화 복호문을 모두 함수에 대입한 후, ''를 만나면 boolean으로 while문 탈출, if문 탈출
        boolean=0
        break
    l=''
    k=int(a)
    #블록화한 복호문을 문자열로 재구성
    for x in range(1,blockN+1):
        for y in range(1,len(dic)+1):
            if k >= (len(dic)**(blockN-x))*(len(dic)-y):
                l+=str(dic[len(dic)-y])
                k-=(len(dic)**(blockN-x))*(len(dic)-y)
                break
                

    string+=l
print(string)
            
              


    
    













# n=0
# while True:
#     b.append(a[n:n+blockN])
#     n+=blockN
#     if n>=len(a):
#         break

# print(b)

# #b의 마지막 항이 blockN보다 짧을때 항 앞에 ~추가하여 길이 조절
# lastB=b[len(b)-1]
# lastB='~'*(blockN-len(lastB))+lastB
# b[len(b)-1]=lastB




# #블록을 숫자로 변환
# for x in range(len(b)):
#     k=b[x]
#     l=0
#     for y in range(blockN):
#         l+=dic[k[y]]*(len(dic)**(blockN-(y+1)))
#     b[x]=l
    
# print(b)

