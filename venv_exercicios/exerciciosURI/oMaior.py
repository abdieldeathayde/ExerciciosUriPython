a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a + b + abs(a-b)) // 2
MaiorAB=(c+MaiorAB+abs(MaiorAB-c)) // 2;
print(f"{MaiorAB} eh o maior")