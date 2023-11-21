#복호화 알고리즘(파일로 암호문 받기)
f=open('key.txt','r')         
d=int(f.readline())
N=int(f.readline())
e=int(f.readline())
f.close()

f2=open('enc.txt','r')           #enc.txt 파일에서 암호문 불러오기
x=int(f2.readline())
f2.close()

print('개인키:',d)
print('공개키 N:',N)
print('암호문:',x)

b=0
while True:                        #복호화 과정
  b+=1
  if (b%N) == (x**d)%N:
    break
print('복호문:',b)

fDe=open('dec.txt','w')           #dec.txt 파일에 복호문 저장
fDe.write(str(b))
fDe.close()