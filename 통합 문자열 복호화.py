def decryption():

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
        
        
        
def string_arrange():
    
    boolean=1
    blockN=2
    l=''
    string=''
    
    ftable=open('table.txt','r')           #알파벳 대응표 불러오기(table.txt)
    dic=str(ftable.readline())
    ftable.close()

    # dic={'~':28,' ':27,'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,
    #      'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
    #      'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    #dic='abcdefghijklmnopqrstuvwxyz ~!1234567890ㄱㄴㄷㄹㅁㅍㅅㅇㅈㅊㅋㅌㅍㅎ'                  #알파벳 대응표

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
                    
        l=l.replace('~','')
        string+=l
    print('최종 복호문: '+string)
    
decryption()
string_arrange()

                