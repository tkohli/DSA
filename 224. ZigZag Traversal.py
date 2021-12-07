def zigzagTraverse(array):
    # row+1, col -1 or reverse 
    height = len(array)-1
    width = len(array[0])-1
    row,col = 0,0
    result= []
    isGoingDown = True
    while not outOfBounds(row,col,height,width):
        result.append(array[row][col])
        if isGoingDown:
            if col==0 or row == height:
                isGoingDown = False
                if row==height:
                    col+=1
                else:
                    row+=1
            else:
                col-=1
                row+=1
        else:
            if row==0 or col == width:
                isGoingDown = True
                if col == width:
                    row+=1
                else:
                    col+=1
            else:
                col+=1
                row-=1
    return result

def outOfBounds(row,col,height,width):
    return 0>row or row>height or 0>col or col >width


print(zigzagTraverse([
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]))