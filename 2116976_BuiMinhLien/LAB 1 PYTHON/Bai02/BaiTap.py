import math

def Cau01(a, b):
    sum = a + b
    div = a/b   
    mul = a**b
    print("a + b = " + str(sum))
    print("a/b = " + str(div))
    print("a b = " + str(sum))


def Cau02(a, b):
    return a*b*2


def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def Cau03(start, end):
   for i in range (start, end):
      if is_prime == True: print(i)
      else: 
         continue



def is_fibonacci(n):
  if not isinstance(n, int) or n < 0:
    return False

  # Khởi tạo hai số Fibonacci đầu tiên.
  a, b = 0, 1

  # Lặp qua dãy số Fibonacci cho đến khi gặp n.
  while b <= n:
    a, b = b, a + b

  # Nếu n bằng một trong hai số Fibonacci đầu tiên, thì nó là số Fibonacci.
  if n == a or n == b:
    return True

  return False
    
def tinh_Tong_Can_Bac_Hai(n):
  sum = 0
  for i in range(1, n):
    sum += math.sqrt(i)
  return sum

def giai_phuong_trinh_bac_2(a,b,c):
  delta = b**2 - 4*a*c
  if delta < 0:
    return "Phương trình vô nghiệm"
  elif delta == 0:
    return f"Phương trình có nghiệm kép = {-(b / (2 * a))}"
  else:
    x1 = (-(b) + math.sqrt(delta))/(2*a)
    x2 = (-(b) - math.sqrt(delta))/(2*a)
    return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    
def Cau09_Tinh_N_GT(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

def draw_custom_triangle(height):
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print('* ' * i)
        else:
            print('*  ' + ' ' * (2 * (i - 2)) + '*')

def giay_qua_gio(seconds):
   return f"{seconds // 3600}:{seconds %3600 // 60}:{seconds %3600 % 60}"

def so_le_khong_chia_het_cho_5(list):
  out = []
  for item in list:
    if not(item % 5 == 0) and item % 2 != 0:
      out.append(item)
  return out

def so_le_khong_chia_het_cho_5(list):
   for item in list:
    if not(item % 5 == 0) and item % 2 != 0:
      print(item)

def Xuat_fib(list):
  out = []
  for item in list:
    if is_fibonacci(item):
      out.append(item)
  return out

def find_max_prime(list):
  out = []
  for item in list:
    if is_prime(item):
      out.append(item)
  return max(out) #nếu không có số nguyên tố thì sao

def find_max_prime_2(list):
  out = filter(is_prime, list) 
  return max(out) #nếu không có số nguyên tố thì sao




''''''''
def find_min_fib(list):
  out = []
  for item in list:
    if is_fibonacci(item):
      out.append(item)
  return min(out)


def find_min_fib_2(list):
  out = filter(is_fibonacci, list)
  return min(out)

''''''''
def tinh_trung_binh_so_le(list):
  out = []
  for item in list:
    if item % 2 == 1:
      out.append(item)
  return sum(out) / len(out)


def tinh_tich_so_le_khong_chia_het_cho_3(list):
  out = []
  for item in list:
    if (item % 2 == 1) and not(item % 3 == 3):
      out.append(item)
  result = 1
  for x in out:
    result *= x
  return result 

def doi_cho_x_y(list, pos1, pos2):
  x = list.pop(pos1)  
  y = list.pop(pos2-1)
  list.insert(pos1, y)
  list.insert(pos2 , x)
  return list

def dao_mang(list):
  list.reverse() 

def xuat_cac_so_lon_thu_nhi(list):
  sortedList = list
  sortedList.sort()
  return sortedList[-2]

def dem_so_lan_xuat_hien(list, n):
  out = []
  for x in list:
    if x == n:
      out.append(x)
  return len(out)



def tinhTong(list):
  return sum(list)
  