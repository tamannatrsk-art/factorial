import sys, copy


STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
    'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ',
    'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR',
    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'
}



BOARD_TEMPLATE = """
  
  a    b     c   d    e    f    g    h
  ___ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
     ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  |    ||||||    ||||||    ||||||    ||||||
4 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||


"""

WHITE_SQUARE = "||"
BLACK_SQUARE = "  "

def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in "87654321":
        for x in "abcdefgh" :
          if x + y in board.keys():
            squares.append(board[x + y])
          else:
                if is_white_square:
                  squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)
        is_white_square = not is_white_square
        

    print(BOARD_TEMPLATE.format(*squares))
print_chessboard(STARTING_PIECES)
print("Interactive Chessboard")
print("by Al Sweigart al@inentwithpython.com")
print()
print("Pieces : ")
print("  w - white, b - Black")
print("  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - king")
print("Commands : ")
print("  move e2 e4 - Moves the piece at e2 to e4")
print("  remove e2 - Removes the piece at e2")
print("  set e2 wP - Sets square e2 to a white pawn")
print("  reset - Resets pieces back to their starting squares")
print("  clear - Clears the entire board")
print("  fill wP - Files entire board with white pawns.")
print("  quit - Quits the program")


main_board = copy.copy(STARTING_PIECES)
while True :
  print_chessboard(main_board)
  


  
  print("1. move e2 e4 - Move a piece ")
  print("2. remove e2 - Remove a piece ")
  print("3. set e2 wp - set a piece ")
  print("4. reset - Reset the board")
  print("5. cleat - cleat the board")
  print("6. quit - Exit the program")
  response = input("> Enter a command : ").split()

  if response[0] == "move":
    main_board[response[2]] = main_board[response[1]]
    del main_board[response[1]]
  elif response[0] == "remove":
    del main_board[response[1]]
  elif response[0] == "set":
    main_board[response[1]] = response[2]
  elif response[0] == "rest":
    main_board = copy.copy(STARTING_PIECES)
  elif response[0] == "clear":
    main_board = {}
  elif response[0] == "fill":
    for y in "87654321":
      for x in "abcdefgh":
        main_board[x + y] = response[1]
  elif response[0] == "quit":
    sys.exit()


