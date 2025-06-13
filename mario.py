def main():
  print_square(4)
  
def print_square(size):
  size=int(input("Enter the side length "))
  #For each row in square
  
  for i in range (size):
    #For each brick in row
    
      for j in range (size):
        #Print brick 
        
        print("#", end="")
      print()
main()