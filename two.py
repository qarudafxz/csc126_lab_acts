def alphabet_position_getter(character):
    low = character.lower().split(" ")[1][0]
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in alphabet:
        if i in low:
           return alphabet.index(i) + 1
    return None

def operate(x, y, op):
 match(op):
  case "-":
   return x - y
  case "*":
   return x * y
  case "/":
   return x / y
  case "//":
   return x // y
  case '%':
   return x % y
  case '**':
   return x ** y
  
   
def index_calc(input, val):
 half = val / 2
 sum = input + val
 op = ['+', '-', '*', '/', '//', '%', '**']

 print(str(input) + " " + op[0] + " " + str(val) + " = " + str(sum) + " id: " + str(id(sum)))
 for op_type in op[1:]:
    ans = operate(sum, half, op_type)
    print(str(sum) + " " + op_type + " " + str(half) + " = " + str(ans) + " id: " + str(id(ans)))
    sum = ans
    
   
def main():
    index = alphabet_position_getter("Francis Tin-ao")
    num = int(input("Enter a number: "))
    index_calc(num, index)

if(__name__ == "__main__"):
    main() 
  
  