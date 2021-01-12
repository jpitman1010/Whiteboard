# import test
# import unittest

def done_or_not(board): #board[i][j]
  # your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'
    """
    >>> done_or_not([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7],[8, 5, 9, 7, 6, 1, 4, 2, 3],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 6, 1, 5, 3, 7, 2, 8, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 4, 5, 2, 8, 6, 1, 7, 9]])
    'Finished!'
                       
    >>> done_or_not([[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 0, 3, 4, 9],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
    'Try again!'

    
    >>> done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 5, 3]])
    'Finished!'

                   
    >>> done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 3, 5]])                 
    'Try again!'

    >>> done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 0, 3, 7, 5],[7, 0, 6, 3, 8, 0, 2, 1, 9],[6, 4, 3, 1, 5, 0, 7, 9, 2],[5, 2, 1, 7, 9, 0, 8, 4, 6],[9, 8, 0, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 0, 8, 1, 7, 9, 2, 4],[8, 7, 0, 6, 4, 2, 1, 3, 5]])
    'Try again!'
                  
    >>> done_or_not([[1, 2, 3, 4, 5, 6, 7, 8, 9],[2, 3, 4, 5, 6, 7, 8, 9, 1],[3, 4, 5, 6, 7, 8, 9, 1, 2],[4, 5, 6, 7, 8, 9, 1, 2, 3],[5, 6, 7, 8, 9, 1, 2, 3, 4],[6, 7, 8, 9, 1, 2, 3, 4, 5],[7, 8, 9, 1, 2, 3, 4, 5, 6],[8, 9, 1, 2, 3, 4, 5, 6, 7],[9, 1, 2, 3, 4, 5, 6, 7, 8]])         
    'Try again!'
    """


    compare_list = [1,2,3,4,5,6,7,8,9]
    columns = {0:[], 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    squares =  {0: [], 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}

        
    for row in range(len(board)):
        # print('row',row,'   =',sorted(board[row]))
        if sorted(board[row]) != compare_list:
            # print('failed row = ', sorted(board[row]))
            # print("Try again!")
            return "Try again!"
        for column in range(len(board)):
            columns[column].append(board[row][column])
        
    
    square = 0
    while square < 9:
        squares[square].extend(board[square][0:3])
        squares[square].extend(board[square + 1][0:3])
        squares[square].extend(board[square + 2][0:3])
        squares[square+1].extend(board[square][3:6])
        squares[square+1].extend(board[square + 1][3:6])
        squares[square+1].extend(board[square + 2][3:6])
        squares[square+2].extend(board[square][6:9])
        squares[square+2].extend(board[square + 1][6:9])
        squares[square+2].extend(board[square + 2][6:9])
        # print(squares)

        square += 3

    # print('columns = ', columns)
    # print('squares = ', squares)
    
    for column in columns.keys():
        # print('column',column,'=', sorted(columns[column]))
        if sorted(columns[column]) != compare_list:
            # print('column =', column, 'failed sorted column =', sorted(columns[column]))
            # print("Try again!")
            return "Try again!"
    for square in squares.keys():
        # print('square',square,'=',sorted(squares[square]))
        if sorted(squares[square]) != compare_list:
            # print('square = ',square,'failed sorted square =', sorted(squares[square]))
            # print("Try again!")
            return "Try again!"
    
    # print("Finished!")
    return "Finished!"


if __name__ == "__main__":
    from doctest import testmod
    doctest.testmod()
    if testmod().failed == 0:
        # All 6 Tests Passed!!!
        app.run(debug=True)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
#     $python example.py -v

#     Trying:
#         done_or_not([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
#                           [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                          [3, 4, 5, 2, 8, 6, 1, 7, 9]])
#     Expecting:


    # Trying: 7, 1, 3, 9, 2, 4, 8, 5, 6],
#                          [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                          [3, 0, 0, 4, 8, 1, 1, 7, 9]])
#     Expecting:
#         Traceback (most recent call last):
#             'Try again!'

#     ok

#     Trying:
#         done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

#     Expecting:
#         Traceback (most recent call last):
#             'Finished!'

#     ok
#     Trying:                    
#         done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])
                        
#     Expecting:
#         Traceback (most recent call last):
#             'Try again!'
#     ok
#     Trying:
#         done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 0, 3, 7, 5]
#                         ,[7, 0, 6, 3, 8, 0, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 0, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 0, 8, 4, 6]
#                         ,[9, 8, 0, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 0, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 0, 6, 4, 2, 1, 3, 5]])

#     Expecting:
#         Traceback (most recent call last):
#             'Try again!'

#     ok

#     Trying:                   
#         done_or_not([[1, 2, 3, 4, 5, 6, 7, 8, 9]
#                          ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
#                          ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
#                          ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
#                          ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
#                          ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
#                          ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
#                          ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
#                          ,[9, 1, 2, 3, 4, 5, 6, 7, 8]])

#     Expecting:
#         Traceback (most recent call last):
#             'Try again!'
#     ok

# 2 items passed all tests:
#    1 tests in __main__
#    6 tests in __main__.done_or_not
# 6 tests in 2 items.
# 6 passed and 0 failed.
# Test passed.
# $