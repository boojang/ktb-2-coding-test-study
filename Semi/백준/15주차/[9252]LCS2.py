'''
Author    : semi
Date      : 2025.08.18(Mon)
Runtime   : 440ms
Memory    : 57628KB
Algorithm : DP
'''

seq1 = input().strip()
seq2 = input().strip()

# 배열의 크기는 (seq1의 길이 + 1) x (seq2의 길이 + 1)로 만들어주면 더 편리할 거예요
# row : seq1 column seq2
P = [[0]*(len(seq2)+1) for _ in range(len(seq1)+1)]

for i in range(1,len(seq1)+1):
    for j in range(1,len(seq2)+1):
        if seq1[i-1]== seq2[j-1]: # ACK AEK 같을경우
            P[i][j] = P[i-1][j-1] +1
        else:
            P[i][j] = max(P[i][j-1],P[i-1][j])


# LCS 길이 출력 -> 역으로 이동

lcs_length = P[len(seq1)][len(seq2)]

if lcs_length ==0:
    print(lcs_length)
else:
    print(lcs_length)

    # lcs 추적
    lcs_string = ""

    i = len(seq1)
    j = len(seq2)

    # 경로 탐색
    while i >0 and j>0 :
        if seq1[i-1] == seq2[j-1]: # 만약 두 글자가 같음
            lcs_string += seq1[i-1] # 글자 추가
            i -=1;j -=1 #대각선으로 이동

        elif P[i-1][j]> P[i][j-1]:
            i -=1
        else:
            j -=1

    print(lcs_string[::-1]) #거꾸로 출력 seq[start:stop:step]