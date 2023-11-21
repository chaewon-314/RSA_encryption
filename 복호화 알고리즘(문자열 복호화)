#복호화 알고리즘(암호문 수동 입력)

#키값 불러오기
f=open('key.txt','r')         
d=int(f.readline())
N=int(f.readline())
e=int(f.readline())
f.close()

print('개인키:',d)
print('공개키 N:',N)


boolean=1
n=0


fenc=open('enc.txt','r')

while boolean:
    x=fenc.readline()         #a는 blocked_str 파일을 한줄씩 입력받음
    
    if str(x)=='':              #블록화 문자열을 모두 함수에 대입한 후, ''를 만나면 boolean으로 while문 탈출, if문 탈출
        boolean=0
        break
            
    b=0
    while True:                        #복호화 과정
        if (b%N) == (int(x)**d)%N:
            break
        b+=1
    print('복호문:',b)
        
    if n==0:                            #처음 파일 작성시 w모드로 기존 파일 초기화
        fde=open('dec.txt','w')           #dec.txt 파일에 암호문 저장
        fde.write(str(b)+'\n')
        fde.close()
            
    else:                               #2번째 작성부터는 a모드로 기존 파일에 추가
        fde=open('dec.txt','a')           #dec.txt 파일에 암호문 저장
        fde.write(str(b)+'\n')
        fde.close()
    n+=1
        