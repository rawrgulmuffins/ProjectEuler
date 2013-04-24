#!/usr/bin/env python3.2
#populates a N by 4 matrix and finds the max product of 4 consecutive  diagnal, up, down, left, right, numbers.
import sys

def main():
   if(len(sys.argv) < 2):
      print("No file name to open. USAGE: ./" + argv[0] + " \"file_name\"")
      exit(1);

   try:
      data_file = open(sys.argv[1])
   except IOError:
      print("Could not open file! Closing Question11.py")

   with data_file:
      matrix = []
      for line in data_file:
         matrix.append( [int(n) for n in line.split() ] )
      print(FindLargest(matrix))



# this answer was used in this function
# http://stackoverflow.com/questions/6429638/how-to-split-a-string-into-two-integers-in-python
# This is a brute force algorithm and can be accomplished in linear time. Currently n^3.
def FindLargest(matrix):
   # TODO -- refactor code
   matrix_max = 0
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         sums = [1, 1, 1, 1]
         for k in range(4):
            #check right
            if( j + k < len(matrix[0])):
               sums[0] *= matrix[i][j + k]
            #check down
            if( i + k < len(matrix)):
               sums[1] *= matrix[i + k][j]
            if( i + k < len(matrix)):
               #check diag right
               if( j + k < len(matrix[0])):
                  sums[2] *= matrix[i+k][j+k]
               #check diag left
               if( j - k > 0): #left bound of matrix is 0
                  sums[3] *= matrix[i + k][j - k]
         for num in sums:
            if (num > matrix_max):
               matrix_max = num
   return matrix_max


def MulitiplyList(numbers):
    product = 1
    for ix in range(len(numbers)):
        product *= numbers[ix]
    return product

main()
