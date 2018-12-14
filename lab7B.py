# CS2302 Data Structures
# Programmed by Luis Garcia.
# Last modified December 5, 2018.
# Instructor Diego Aguirre.
# Implementation of Edit Distance.
# The implementation of Edit Distance will create a matrix
# and will compare two strings and at the end it will simply return the leftover value
#after analyzing the two strings.
# lab 7

def edit_distance(str1, str2):

    mat = [[0 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)] #Creating new matrix.

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i
            elif str1[i-1] == str2[j-1]:
                mat[i][j] = mat[i-1][j-1]
            # If characters at actual position are the same,
            # Assign the actual position to the min value, previously computed
            else:
                mat[i][j] = 1 + min(mat[i][j-1], mat[i-1][j], mat[i-1][j-1])
    return mat[len(str1)][len(str2)] #  Return  value in the last row, and last column last column.

print(edit_distance("door", "moon")) # words to test
