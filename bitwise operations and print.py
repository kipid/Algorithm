print(0<<1) # 0
# print(0<<<2)
print(1<<0) # 1
print(1<<1) # 2
print(1<<2) # 4
print(1<<3) # 8
print(1<<31) # 2147483648
print()

print(f"{bin(1<<0) = }") # '0b1'
print(f"{bin(1<<1) = }") # '0b10'
print(f"{bin(1<<2) = }") # '0b100'
print(f"{bin(1<<3) = }") # '0b1000'
print()

print(f"{hex(1<<0) = }") # '0x1'
print(f"{hex(1<<1) = }") # '0x2'
print(f"{hex(1<<2) = }") # '0x4'
print(f"{hex(1<<3) = }") # '0x8'
print()

print(f"{1<<0:b}") # 1
print(f"{1<<1:b}") # 10
print(f"{1<<2:b}") # 100
print(f"{1<<3:b}") # 1000
print()

print(f"{1<<0:16b}") #                1
print(f"{1<<1:16b}") #               10
print(f"{1<<2:16b}") #              100
print(f"{1<<3:16b}") #             1000
print(f"{1<<31:16b}") # 10000000000000000000000000000000
print()

print(f"{1<<0:016b}") # 0000000000000001
print(f"{1<<1:016b}") # 0000000000000010
print(f"{1<<2:016b}") # 0000000000000100
print(f"{1<<3:016b}") # 0000000000001000
print(f"{1<<31:016b}") # 10000000000000000000000000000000
print()

print(f"{1<<0:032b}") # 00000000000000000000000000000001
print(f"{1<<1:032b}") # 00000000000000000000000000000010
print(f"{1<<2:032b}") # 00000000000000000000000000000100
print(f"{1<<3:032b}") # 00000000000000000000000000001000
print(f"{1<<31:032b}") # 10000000000000000000000000000000
print(f"{1<<32:032b}") # 100000000000000000000000000000000
print(f"{1<<100:032b}") # 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(f"{len("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") = }") # 101
print()

# 진법 초기화
a = 10
print(type(a), a) # <class 'int'> 10
a = 0b10
print(type(a), a) # <class 'int'> 2
a = 0o10
print(type(a), a) # <class 'int'> 8
a = 0x10
print(type(a), a) # <class 'int'> 16
print()

a = 0B10
print(type(a), a) # <class 'int'> 2
a = 0O10
print(type(a), a) # <class 'int'> 8
a = 0X10
print(type(a), a) # <class 'int'> 16
print("-"*20)

# 출력
i = 0x100
print("i =", i) # i = 256
print("i =", bin(i)) # i = 0b100000000
print("i =", int(i)) # i = 256
print("i =", oct(i)) # i = 0o400
print("i =", hex(i)) # i = 0x100
print("-"*20)

# 문자열을 형변환
i = "100"
print("i =", int(i)) # i = 100
print("i =", int(i, 2)) # i = 4
print("i =", int(i, 8)) # i = 64
print("i =", int(i, 16)) # i = 256
print("i =", int(i, 5)) # i = 25
print("-"*20)

# 비트 연산자(Bitwise Operators)
a = 0b1100
b = 0b1010

print('a =',  a, ":", bin(a)) # a = 12 : 0b1100
print('b =',  b, ":", bin(b)) # b = 10 : 0b1010
print('a & b =',  a & b, ":", bin(a & b)) # a & b = 8 : 0b1000
print('a | b =',  a | b, ":", bin(a | b)) # a | b = 14 : 0b1110
print('a ^ b =',  a ^ b, ":", bin(a ^ b)) # a ^ b = 6 : 0b110
print('~a =',  ~a, ":", bin(~a)) # ~a = -13 : -0b1101
print(f'{~a = :032b}') # -0000000000000000000000000001101
print(f"{((1 << 32) - 1) & ~a = :032b}") # 11111111111111111111111111110011

a = 0b1
print('a =', a) # a = 1
a = a << 1    # * 2
print('a =', a) # a = 2
a = a << 1    # * 2
print('a =', a) # a = 4
a = a << 3    # * 2**3
print('a =', a) # a = 32

a = a >> 1    # // 2
print('a =', a) # a = 16
a = a >> 1    # // 2
print('a =', a) # a = 8
a = a >> 2    # // 2**2
print('a =', a) # a = 2
a = a >> 1    # // 2
print('a =', a) # a = 1
a = a >> 1    # // 2
print('a =', a) # a = 0

a = 10
b = 100
# print(f"{a = , b =}") # SyntaxError: f-string: expecting '!', or ':', or '}'
a = -10
print(f"{a >> 1 = }")
print(f"{a >> 2 = }")
print(f"{a >> 3 = }")
print(f"{a >> 4 = }")
print(f"{a >> 5 = }")
print()
# print(f"{a >>> 1 = }") # SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
int32_1 = (1<<32)-1
def rRRShift(a: int, shift: int) -> int: # mimic (a >>> shift)
	return (int32_1 & a) >> shift
print(f"{(int32_1 & a) = :032b}") # 11111111111111111111111111110110
print(f"{(int32_1 & a) >> 1 = :032b}") # 01111111111111111111111111111011
print(f"{(int32_1 & a) >> 2 = :032b}") # 00111111111111111111111111111101
print(f"{(int32_1 & a) >> 3 = :032b}") # 00011111111111111111111111111110
print(f"{(int32_1 & a) >> 4 = :032b}") # 00001111111111111111111111111111
print(f"{(int32_1 & a) >> 5 = :032b}") # 00000111111111111111111111111111
print(f"{(int32_1 & a) >> 6 = :032b}") # 00000011111111111111111111111111
print(f"{(int32_1 & a) >> 7 = :032b}") # 00000001111111111111111111111111
print(f"{(int32_1 & a) >> 31 = :032b}") # 00000000000000000000000000000001
print(f"{rRRShift(a, 1) = :032b}") # 01111111111111111111111111111011
print(f"{rRRShift(a, 31) = :032b}") # 00000000000000000000000000000001
print()

# 비트 연산자(Bitwise Operators)
# 2의 누승 출력하기
a = 1
for i in range(0, 11):
    print('{0:6,}'.format(a << i), end=' ')
    #      1      2      4      8     16     32     64    128    256    512  1,024
print()

a = 2
for i in range(0, 11):
    print('{0:6,}'.format(a ** i), end=' ')
    #      1      2      4      8     16     32     64    128    256    512  1,024
print()

a = 1024
for i in range(0, 11):
    print('{0:6,}'.format(a >> i), end=' ')
    #  1,024    512    256    128     64     32     16      8      4      2      1
print()

a = 2
for i in range(10, -1, -1):
    print('{0:6,}'.format(a ** i), end=' ')
    #  1,024    512    256    128     64     32     16      8      4      2      1
print()

# 2의 보수를 이용한 뺄셈
# ~(1의보수) + 1 = 2의 보수
a = 10
b = 3
c = a - b
d = a + (~b + 1)
print('a - b =', c) # a - b =  7
print('a + (~b + 1) =', d) # a + (~b + 1) = 7

# 두개의 숫자를 교환하기
a = 100
b = 200
print('a={0}, b={1}'.format(a,b)) # a=100, b=200

# 임시 변수를 사용하는 방법
temp = a
a = b
b = temp
print('a={0}, b={1}'.format(a,b)) # a=200, b=100

# Python의 tuple을 이용하는 방법
a, b = b, a
print('a={0}, b={1}'.format(a,b)) # a=100, b=200

# ^(xor)연산자를 이용하는 방법
a = a ^ b # (a ^ b)
b = a ^ b # (a ^ b) ^ b => a
a = a ^ b # (a ^ b) ^ a => b
print('a={0}, b={1}'.format(a,b)) # a=200, b=100

# 색상 값은 어떻게 나타낼까?
# 대부분 4Byte로 Alpha, Red, Green, Blue를 이용하여 나타낸다.
# 색상값이 AABBCCDD일때 각각 1바이트씩 분리하고 다시 결합해 보자
# 2진수 4자리는 16진수 1자리이다. 1Byte는 8Bit이므로 16진수 2자리로 표현 가능하다.
# and 연산은 값을 지울 때 사용합니다.
# 0으로 &연산하면 0이고 1로 &연산하면 통과입니다.
# or 연산은 값을 설정할 때 사용합니다.
# 0으로 |연산하면 통과이고 1로 |연산하면 1입니다.

# 색상분리
color = 0xAABBCCDD
alpha = color >> 24 & 0xFF
red = color >> 16 & 0xFF
green = color >> 8 & 0xFF
blue = color & 0xFF

print(color, hex(color)) # 2864434397 0xaabbccdd
print(alpha, hex(alpha)) # 170 0xaa
print(red, hex(red)) # 187 0xbb
print(green, hex(green)) # 204 0xcc
print(blue, hex(blue)) # 221 0xdd

# 색상 결합
color2 = 0
print(color2, hex(color2)) # 0 0x0
color2 = color2 | alpha << 24
print(color2, hex(color2)) # 2852126720 0xaa000000
color2 = color2 | red << 16
print(color2, hex(color2)) # 2864381952 0xaabb0000
color2 = color2 | green << 8
print(color2, hex(color2)) # 2864434176 0xaabbcc00
color2 = color2 | blue
print(color2, hex(color2)) # 2864434397 0xaabbccdd

# red값 만 삭제
color2 = color2 & 0xFF00FFFF
print(color2, hex(color2)) # 2852179165 0xaa00ccdd

# red값을 56으로 설정
color2 = color2 | 0x00560000
print(color2, hex(color2)) # 2857815261 0xaa56ccdd

# 테트리스 벽돌을 출력해보자
brick = (0x0660, 0x0F00, 0x2222, 0x6220, 0x4460, 0x4640, 0x7200, 0x6300,0x4620)
print(f"{len('1000000000000000') = }")
for i in brick:
    mask = 0b1000000000000000
    for j in range(0,16):
        print('■' if (mask & i) == mask else '□', end='')
        if (j+1)%4==0:
            print()
        mask >>= 1
    print()

