from connectfour.agents.computer_player import RandomAgent
import random
import heapq


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 1


    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append( move )
            vals.append( self.dfMiniMax(next_state, 1) )
        newMove = []
        best = []
        val=0
        for val in range(0, len(vals)):
            if vals[val] == max(vals):
                newMove.append(val);
        if len(newMove)>1:
            bestMove = moves[self.findMiddle(newMove)]
        else:
            bestMove = moves[vals.index( max(vals) )]
        print(vals)
        return bestMove

       

    def findMiddle(self, input_list):
        middle = float(len(input_list))/2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return (input_list[int(middle)])


        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append( move )
            vals.append( self.dfMiniMax(next_state, depth + 1) )

        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)
        
        return bestVal


    def evaluateBoardState(self, board):
        #if the game is finished, check for winner

        #winning move detected and made, prioritising over others


        if(self.id == 2):
            if(board.terminal() == True):
                return 10000;
                sys.exit();

            elif not (isinstance(board.next_state(1,0),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,1),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,2),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,3),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,4),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,5),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(1,6),int)):
                val = self.blockAndEval(board);
                return val;

            else:
                return self.myEval(board)

               

        else:
            if(board.terminal() == True):
                return 1000000;

            elif not (isinstance(board.next_state(2,0),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,1),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,2),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,3),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,4),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,5),int)):
                val = self.blockAndEval(board);
                return val;

            elif not (isinstance(board.next_state(2,6),int)):
                val = self.blockAndEval(board);
                return val;

            else:
                return self.myEval(board)


    def blockAndEval(self,board):

        value = self.blockMove(board,self.id);
        return value;

    def blockMove(self,board,id):

        if (id == 2):
            val = 1;
        else:
            val = 2;

        if not (isinstance(board.next_state(val,3),int)) and (board.next_state(val,3).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,4),int)) and (board.next_state(val,4).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,5),int)) and (board.next_state(val,5).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,6),int)) and (board.next_state(val,6).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,0),int)) and (board.next_state(val,0).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,1),int)) and (board.next_state(val,1).terminal() == True):
            return -10000;

        elif not (isinstance(board.next_state(val,2),int)) and (board.next_state(val,2).terminal() == True):
            return -10000;

        else:
            return self.myEval(board)



    def myEval(self, board):
        val=1
        if self.id==2:
            val==1
        if self.id==1:
            val ==2 
        firstTwos=0
        secondTwos=0
        firstThrees=0
        secondThrees=0
        twos = []
        threes = []
        myEval=0
        firstTwos,secondTwos,firstThrees,secondThrees=self.totalTwosAndThrees(board)
        if self.id==2:
            myEval=(secondThrees *75 + secondTwos*20-firstThrees *75 +firstTwos *20)
        else: 
            myEval=(firstThrees *75 + firstTwos*20 -secondThrees *75 +secondTwos *20)

   



        for row in range (0,6):
            if board.get_cell_value(row,1)==val and board.get_cell_value(row,2)==val and board.get_cell_value(row,0)==0 and board.get_cell_value(row,3)==0:
                myEval= -75
            elif board.get_cell_value(row,2)==val and board.get_cell_value(row,3)==val and board.get_cell_value(row,1)==0 and board.get_cell_value(row,4)==0:
                myEval= -75
            elif board.get_cell_value(row,3)==val and board.get_cell_value(row,4)==val and board.get_cell_value(row,2)==0 and board.get_cell_value(row,5)==0:
                myEval= -75
            elif board.get_cell_value(row,4)==val and board.get_cell_value(row,5)==val and board.get_cell_value(row,3)==0 and board.get_cell_value(row,6)==0:
                myEval= -75
            if board.get_cell_value(row,1)==self.id and board.get_cell_value(row,2)==self.id and board.get_cell_value(row,0)==0 and board.get_cell_value(row,3)==0:
                myEval=  75
            elif board.get_cell_value(row,2)==self.id and board.get_cell_value(row,3)==self.id and board.get_cell_value(row,1)==0 and board.get_cell_value(row,4)==0:
                myEval=  75
            elif board.get_cell_value(row,3)==self.id and board.get_cell_value(row,4)==self.id and board.get_cell_value(row,2)==0 and board.get_cell_value(row,5)==0:
                myEval=  75
            elif board.get_cell_value(row,4)==self.id and board.get_cell_value(row,5)==self.id and board.get_cell_value(row,3)==0 and board.get_cell_value(row,6)==0:
                myEval=  75
            elif board.get_cell_value(row,4)==self.id and board.get_cell_value(row,5)==self.id and board.get_cell_value(row,3)==self.id:
                if board.get_cell_value(row,6)==0  and board.get_cell_value(row,2)==0:
                    myEval=  500
                elif (board.get_cell_value(row,6)!=0  and board.get_cell_value(row,2)==0) or (board.get_cell_value(row,6)==0  and board.get_cell_value(row,2)!=0) : 
                    return 100

            elif board.get_cell_value(row,4)==self.id and board.get_cell_value(row,2)==self.id and board.get_cell_value(row,3)==self.id :
                if board.get_cell_value(row,1)==0 and board.get_cell_value(row,5)==0:
                    myEval=  500
                elif (board.get_cell_value(row,5)!=0  and board.get_cell_value(row,1)==0) or (board.get_cell_value(row,5)==0  and board.get_cell_value(row,1)!=0) : 
                    return 100

            elif board.get_cell_value(row,1)==self.id and board.get_cell_value(row,2)==self.id and board.get_cell_value(row,3)==self.id:
                if board.get_cell_value(row,0)==0 and board.get_cell_value(row,4)==0:
                    myEval=  500
                elif (board.get_cell_value(row,0)!=0  and board.get_cell_value(row,4)==0) or (board.get_cell_value(row,0)==0  and board.get_cell_value(row,4)!=0) : 
                    return 100

            
            

        return myEval
    def rowTwosThrees(self, board):
        threes=[]
        twos=[]
       
        for row in range(0,6):
            same_count =1
            curr = board.get_cell_value(row,0)
            for col in range(1,7):
                if board.get_cell_value(row,col)==curr:
                    same_count += 1
                    if same_count == 3 and curr != 0 and col!=6 :
                        threes.append(curr) 
                    elif same_count == 2 and curr != 0 and col!=5:
                        twos.append(curr) 
                    
        return(twos,threes)
    def colTwosThrees(self, board):
        threes=[]
        twos=[]
        for i in range(0,7):
            same_count = 1
            curr = board.get_cell_value(0,i)
            for j in range(1, 6):
                if board.get_cell_value(j,i) == curr:
                    same_count += 1
                    if same_count == 3 and curr != 0 and j !=5:
                        threes.append(curr)    
                    if same_count == 2 and curr != 0 and j !=4:
                        twos.append(curr)
                   
                else:
                    same_count = 1
                    curr = board.get_cell_value(j,i)
        return(twos,threes)

    def diagTwosThrees(self, board):
        twos=[]
        threes=[]
        for i in range(4):
            for j in range(3):
                same_count = 1
                curr = board.get_cell_value(j,i)
                k, m = j + 1, i + 1
                while k < 6 and m < 7:
                    if board.get_cell_value(k,m) == curr:
                        same_count += 1
                        if same_count is 2 and curr != 0:
                            twos.append(curr)
                        if same_count is 3 and curr != 0:
                            threes.append(curr)    
                    else:
                        same_count = 1
                        curr = board.get_cell_value(k,m)
                    k += 1
                    m += 1
        return(twos,threes)

    def totalTwosAndThrees(self,board):
        twosRow=[]
        threesRow=[]
        twosCol=[]
        threesCol=[]
        twosDiag=[]
        threesDiag=[]
        firstTwos=0
        secondTwos=0
        firstThrees=0
        secondThrees=0
        twosRow, threesRow = self.rowTwosThrees(board)
        twosCol, threesCol, = self.colTwosThrees(board)
        twosDiag,threesDiag =self.diagTwosThrees(board)
    
        for item in twosRow+twosCol+twosDiag:
            if item == 1:
                 firstTwos+=1
            else:
                secondTwos+=1
        for item in threesRow+threesCol+threesDiag:
            if item == 1:
                firstThrees+=1
            else:
                secondThrees+=1
        return (firstTwos,secondTwos,firstThrees,secondThrees)          

        



                

        """
        Your evaluation function should look at the current state and return a score for it.
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
