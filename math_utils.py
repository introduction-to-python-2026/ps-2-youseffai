def find_max_number(num1, num2, num3):
  if num1>num2 and num1>num3:
    return num1
  if num2>num3 and num2>num3:
    return num2
  if num1>=num2>=num3 or num1>=num3>=num2:
    return num1
  if num2>=num1>=num3 or num2>=num3>=num1:
    return num2
  else:
    return num3

def find_mean(num1, num2, num3):
    total=num1+num2+num3
    n=3
    mean=total/3
    return mean

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    variance = ((num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2) / 3
    std_dev = math.sqrt(variance)
    return mean, std_dev

