# print(1 << 30)
#
# print(0x7fffffff)
#
# print(0x6fffffff)
#
# print(0x5fffffff)
#
# print(0x4fffffff)
#
# print(0x3fffffff)
#
# print(0x2fffffff)
#
# print(0x1fffffff)
#
import time
i = 1 << 25
j = 0;
c = time.time();
while i != j:
    j += 1;
    print(j)

d = time.time();
print(c)
print(d)
print((d-c))