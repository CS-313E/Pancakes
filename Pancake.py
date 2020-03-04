#  File: Pancake.py

#  Description: Create an algorithm to sort the stack of pancakes.

#  Student's Name: Jadesola Jaiyesimi

#  Student's UT EID: jaj3847

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: February 19th, 2020

#  Date Last Modified: February 21, 2020

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula 
#          this is a list of lists
#          the last item in this list is the sorted stack
def sort_pancakes ( pancakes ):
  every_flip = []
  index = 0
  count = len(pancakes)-1 
  maximum = pancakes.index(max(pancakes))
  if count < 0 :
    every_flip = pancakes
  else:
    while (count != 0 ):
      if maximum == 0:  # end of list
        x = flip(pancakes,count)
        every_flip.append(x[:])
      elif count == pancakes.index(max(pancakes)):# in correct place
        pancakes = pancakes
      else:     # middle of list
        x = flip(pancakes,maximum)  #flip 1
        every_flip.append(x[:])
        x = flip(pancakes,count)  #flip 2
        every_flip.append(x[:])
        
      count  -= 1
      maximum = pancakes.index(max(pancakes[:count+1]))

  return every_flip    # return a list of flipped pancake stacks

def flip (pancakes, index):
  pancakes[:index+1] =reversed( pancakes[:index+1])
  return pancakes

def main():
  # open the file pancakes.txt for reading
  in_file = open ("./pancakes.txt", "r")

  line = in_file.readline()
  line = line.strip()
  line = line.split()
  print (line)
  pancakes = []
  for item in line:
    pancakes.append (int(item))

  # print content of list before flipping
  print ("Initial Order of Pancakes = ", pancakes)

  # call the function to sort the pancakes
  every_flip = sort_pancakes ( pancakes )

  # print the contents of the pancake stack after
  # every flip
  for i in range (len(every_flip)):
    print (every_flip[i])


  # print content of list after all the flipping
  print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
  main()