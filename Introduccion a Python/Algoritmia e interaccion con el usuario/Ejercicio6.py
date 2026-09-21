"NUMEROS PRIMOS EN UN RANGO"
def is_cousin (number):
        return (number%2 or number%3 or number%5 or number%7) != 0

print("Ingrese dos números: ", end = "")
first_number, second_number = list(map(int, input().split()))

for number in range(first_number, second_number):
  if is_cousin(number) : print(number) 
        