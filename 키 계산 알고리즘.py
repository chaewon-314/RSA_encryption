#키 계산 알고리즘
import random
e=3                               #e는 편의상 3으로 고정(e값은 p,q와 서로소인 어떤 수든지 가능함.)
a=2                               #페르마 소정리용 상수
N=0                               #개인키 N 0으로 초기화
minPQ=80                         #p,q의 최솟값, mimPQ>1
maxPQ=600                        #p,q의 최댓값, maxPQ>1
maxKeyLength=50000                    #최대 키 길이, keylength>1
minKeyLength=30000                          #최소 키 길이

while N>maxKeyLength or N<minKeyLength:               #N이 maxkeylength이하, minKeyLength이상 일때까지 반복
  while True:                       #(p-1)이 e의 배수가 아닌 p 찾기
    p=random.randrange(minPQ,maxPQ)
    if p%2==1:
      if (a**(p-1))%p == 1:         #페르마 소정리
        if (p-1)%e != 0:
          break
        else:
          continue

  while True:                       #(q-1)이 e의 배수가 아닌 q 찾기
    q=random.randrange(minPQ,maxPQ)
    if q%2==1:
      if (a**(q-1))%q == 1:     #페르마 소정리
        if (q-1)%e != 0:
          break
        else:
          continue


                   #e는 (p-1), (q-1)과 서로소인 정수(변경 가능)


  d=0
  while True:             #d(개인키) 찾기
    d+=1
    if (e*d)%((p-1)*(q-1))==1:    #d(개인키)는 (p-1)*(q-1)로 나눈 나머지가 1이 되도록 하는 수
      break
  N=p*q
  
print('개인키:',d)
print('공개키 N:',N)
print('공개키 e:',e)


f=open('key.txt','w')       #키 값을 key.txt파일에 저장
f.write(str(d)+'\n')
f.write(str(N)+'\n')
f.write(str(e)+'\n')
f.close()