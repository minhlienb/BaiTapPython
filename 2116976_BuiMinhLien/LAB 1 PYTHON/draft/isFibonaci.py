def is_fibonacci(n):
  """
  Kiểm tra xem một số nguyên n có phải là số Fibonacci hay không.

  Args:
    n: Số nguyên cần kiểm tra.

  Returns:
    True nếu n là số Fibonacci, False nếu n không phải là số Fibonacci.
  """

  # Kiểm tra xem n có phải là số nguyên dương hay không.
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

print(is_fibonacci(8))