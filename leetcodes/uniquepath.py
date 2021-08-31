# brutal force:
# make the m by n array start with all 1 initialize 
# start interate the inner side start border at 1->m and 1-> n
# add up the top and left to found the current index value
# until the end of array
# return the last index of array at [m-1][n-1]
# improve algorithm:
# only run a haft bottom of the array
# the diagonal will be the sum of the index [i-1][j-1] + [i][j-1] +[i][j-2]
# the max number of m and n will be the row
# the their is the column number must be equal row then calculate until diagonal 
# there is a problem to do in this way is out of bound 