
def isvalidchessboard(board):
    pieces = ["pawn","knight","bishop","rook","king","queen"]
    white_pieces = 0
    black_pieces = 0
    white_king = 0
    black_king = 0
    white_pawns = 0
    black_pawns = 0

    for square, piece in board.items():
        if square[0] not in "abcdefgh" or square[1] not in "12345678":
            return False
        if piece[0] not in "wb" or piece[1:] not in pieces:
            return False
        
        if piece[0] == "w":
            white_pieces +=1
            if piece[1:] == "king":
                white_king += 1
            if piece[1:] == "pawn":
                white_pawns += 1
        else:
            black_pieces += 1

            if piece[1:] == "king":
                black_king += 1
            if piece[1:] == "pawn":
                black_pawns += 1

        

    return (
        white_king == 1 and black_king == 1
    and white_pieces <= 16 and black_pieces <= 16
    and white_pawns <= 8 and black_pawns <= 8)


chess_board = {
    "h1" : "bking",
    "c6": "wqueen",
    "g2" : "bbishop",
    "h5" : "bqueen",
    "e3" : "wking"
    }


print(isvalidchessboard(chess_board))
