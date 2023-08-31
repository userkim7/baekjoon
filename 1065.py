#1065

#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

##첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
##첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N=int(input())
List=[n for n in range(1,100)] #1|2자리 한수 리스트
for n in range(-8,9): #세자리 한수 리스트에 추가
    for i in range(1,10):
        if not(i+2*n<0 or i+2*n>9):
            List.append(i*100+(i+n)*10+i+2*n)
List.sort() #리스트 정렬
end=144 #N==999|1000
for index,num in enumerate(List): #N이하의 한수의 계수 구하기
    if num>N: #N보다 큰 한수의 인덱스(=한수개수-N보다 큰 한수1개)
        end=index
        break
print(end)

###등차수열,집합
