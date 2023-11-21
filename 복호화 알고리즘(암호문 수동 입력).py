#복호화 알고리즘(암호문 수동 입력)
f=open('key.txt','r')         
d=int(f.readline())
N=int(f.readline())
e=int(f.readline())
f.close()

print('개인키:',d)
print('공개키 N:',N)


x=int(input('암호문:'))     #암호문 입력

b=0
while True:                        #복호화 과정
  b+=1
  if (b%N) == (x**d)%N:
    break
print('복호문:',b)

fDe=open('dec.txt','w')
fDe.write(str(b))
fDe.close()