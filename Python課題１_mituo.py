#★1問----------------------------
print("1問")
print("Hello,World！")


#★2問----------------------------
print("2問")
num = float(input("n="))
if 100 < num:
        print("対象")
elif 1 <= num% 2 == 1:
        print("規格外,対象外")
elif 2 <= num <= 5:
        print("規格内,対象外")  
elif 6 <= num <= 20:
        print("規格外,対象外")
elif 20 < num <= 100:
        print("規格内,対象外")


        

#★3問 ----------------------------
print("3問")
A = float(input("a="))
B = float(input("b="))
X = A + B
Y = A - B
Z = A * B
print(X)
print(Y)
print(Z)


#★4問 ----------------------------
print("4問")
import math
C = float(input("a="))
D = float(input("b="))
math.ceil(C / D)
E = math.ceil(C / D)
F = float(C)/ float(D)
print(E)
print(F)

#★5問----------------------------
print("5問")
n = int(input("n="))
for i in range(n):
    print(i**2)

#★問題6　うるう年----------------------------
print("6問")
#指定された年がうる年かどうかを判定し、True/Falseをコンソールに表示してください。
year_str = input("西暦4桁を入力")
year = int(year_str)

if year % 100 == 0 and year % 400 != 0:
    print("False")
elif year % 4 == 0:
    print("True")
else:
    print("False")  
#★問題7 Print関数----------------------------
print("7問")
n = int(input("入力値="))
mylist = list(range(n))
print(*mylist, sep='')

    
#★問題8 抽出----------------------------
#入力値1: 総数を表す数字(n) 入力値2: 対象値がスペース区切りされたもの(A[] of n)
print("8問")
#出力値: 2番目に大きい数字
n = int(input("総数="))
list = input("対象値=")       
T = sorted(set(list))[-2]
print(T)


#★9問----------------------------
print("9問")
import random
Y = str(input("姓="))
Z = str(input("名="))
list = []
list.append(Y)
list.append(Z)
random.shuffle(list)
print(*list)



