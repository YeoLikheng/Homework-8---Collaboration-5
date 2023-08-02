def replace_last(numbers):
   if numbers:
      numbers.insert(0,numbers.pop())
      return numbers
   else:
      return numbers
   

