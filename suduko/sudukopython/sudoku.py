class sudoku:
    innerdimension=3
    def __init__(self,board) -> None:
        self.board=board
        
    def printboard(self):
        for i in range(len(self.board)):
                if i% sudoku.innerdimension==0: print()
                for j in range(len(self.board[0])):
                    if j% sudoku.innerdimension==0: print(end=' ')
                    print(self.board[i][j],end=' ')
                print()
                
    def solve(self,row,col):
        # if  row==len(self.board) and  col==len(self.board):
        #     return True
        # print(row,col)
        if row==len(self.board) :
            col+=1
            if col==len(self.board):
                return True
            else:
                row=0
        if self.board[row][col] != 0:
            return self.solve(row+1,col)
        
        for num in range(1,len(self.board)+1):
            if self.isvalid(num,row,col):
                self.board[row][col] =num
                # print(num)
                if self.solve(row+1,col):
                    return True
                self.board[row][col]=0
    
                    
    def isvalid(self,num,row,col):
        for i in range(len(self.board)):
            if self.board[i][col]==num:
                return False
        for j in range(len(self.board[0])):
            if self.board[row][j]==num:
                return False
            
        startrow=(row//sudoku.innerdimension)*sudoku.innerdimension
        startcol=(col//sudoku.innerdimension)*sudoku.innerdimension
        # print(startrow,startcol)
        for i in range(startrow,startrow+sudoku.innerdimension):
            for j in range(startcol,startcol+sudoku.innerdimension):
                if self.board[i][j]==num:
                    return False
            
        return True