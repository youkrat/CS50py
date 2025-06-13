def main():
  size=int(input("Enter size "))
  print_square(size)
  
def print_square(size):

  
  for i in range (size):
    #For each brick in row
    
      for j in range (size):
        #Print brick 
        
        print("#", end="")
      print()
main()