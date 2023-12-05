#암호화 알고리즘(저장한 키 불러오기 추가, 파일로 암호문 쓰기)
boolean=1

f1=open('key.txt','r')             
d=int(f1.readline())
N=int(f1.readline())
e=int(f1.readline())
n=0                             #n은 함수반복 횟수

f1.close()

print('공개키 e:',e)
print('공개키 N:',N)

fblock=open('blocked_str.txt','r')

while boolean:
    a=fblock.readline()         #a는 blocked_str 파일을 한줄씩 입력받음
    
    if str(a)=='':              #블록화 문자열을 모두 함수에 대입한 후, ''를 만나면 boolean으로 while문 탈출, if문 탈출
        boolean=0
        break
    
    if int(a) <= N:          #평서문의 크기가 N보다 작은지 확인
        x=0
            
        while True:       #암호화 과정
            x+=1
            if x%N == (int(a)**e)%N:
                break
        
        if n==0:                            #처음 파일 작성시 w모드로 기존 파일 초기화
            fEn=open('enc.txt','w')           #enc.txt 파일에 암호문 저장
            fEn.write(str(x)+'\n')
            fEn.close()
            
        else:                               #2번째 작성부터는 a모드로 기존 파일에 추가
            fEn=open('enc.txt','a')           #enc.txt 파일에 암호문 저장
            fEn.write(str(x)+'\n')
            fEn.close()
        n+=1


    else:
        print('암호문의 크기가 N보다 큽니다')