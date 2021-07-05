#หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
#หาจุดวนซ้ำ
#หาจุดออกจาก function
#ต้องมี parameter
number = int(input('ใส่ค่า Factorial:'))
def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)


print('ค่า factorial =',factorial(number))
a = factorial(number)

#แสดงจำนวนรอบที่เลขจำนวนเต็มหาร 10 ลงตัว
def countzero():
    i = 0
    n = a
    while n % 10 == 0:
      i += 1
      n /= 10
    return i


print('จำนวนเลข 0 ที่ติดกันด้านหลังสุด =',countzero(),'ตัว')

