#암호화 알고리즘(저장한 키 불러오기 추가, 파일로 암호문 쓰기)
f1=open('key.txt','r')             
d=int(f1.readline())
N=int(f1.readline())
e=int(f1.readline())
f1.close()

print('공개키 e:',e)
print('공개키 N:',N)

a=int(input('평서문:'))       #평서문 입력(이때 a<N이어야 함)
if a <= N:          #평서문의 크기가 N보다 작은지 확인

  finput=open('input.txt','w')            #input.txt 파일에 평서문 저장
  finput.write(str(a))
  finput.close

  x=0
  while True:       #암호화 과정
    x+=1
    if x%N == (a**e)%N:
      break
  print('암호문:',x)

  fEn=open('enc.txt','w')           #enc.txt 파일에 암호문 저장
  fEn.write(str(x))
  fEn.close()

else:
  print('암호문의 크기가 N보다 큽니다')

