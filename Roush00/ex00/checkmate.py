PIECES = "KPBRQ"

SLIDING_DIRECTIONS = {
    "B": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    "R": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "Q": [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
}


def find_pieces(rows, size):
    king_pos = None
    pieces = []

    for r in range(size):
        for c in range(size):
            cell = rows[r][c]
            if cell == "K":
                if king_pos is not None:
                    return None, None
                king_pos = (r, c)
            elif cell in PIECES:
                pieces.append((cell, r, c))

    return king_pos, pieces


def pawn_attacks(r, c, king_pos):
    kr, kc = king_pos
    return r - 1 == kr and (c - 1 == kc or c + 1 == kc)


def sliding_attacks(piece, r, c, rows, size, king_pos):
    for dr, dc in SLIDING_DIRECTIONS[piece]:
        nr, nc = r + dr, c + dc

        while 0 <= nr < size and 0 <= nc < size:
            cell = rows[nr][nc]

            if (nr, nc) == king_pos:
                return True
            if cell in PIECES:
                break

            nr += dr
            nc += dc

    return False


def checkmate(board):
    try:
        if not isinstance(board, str) or board == "":
            return

        rows = board.split("\n")
        size = len(rows)

        for row in rows:
            if len(row) != size:
                return

        king_pos, pieces = find_pieces(rows, size)
        if king_pos is None:
            return

        for piece, r, c in pieces:
            if piece == "P":
                attacks = pawn_attacks(r, c, king_pos)
            else:
                attacks = sliding_attacks(piece, r, c, rows, size, king_pos)

            if attacks:
                print("Success")
                return

        print("Fail")
    except Exception:
        return
