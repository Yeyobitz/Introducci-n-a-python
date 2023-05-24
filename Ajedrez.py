# Definición de las constantes
EMPTY = "-"
ROOK = "♜"
KNIGHT = "♞"
BISHOP = "♝"
QUEEN = "♛"
KING = "♚"
PAWN = "♟"

# Colores de texto
BLACK = "\033[1;30m"  # Negro
WHITE = "\033[1;37m"  # Blanco
RESET = "\033[0m"  # Restaurar color predeterminado

# Crear el tablero de ajedrez vacío
board = [[EMPTY for i in range(8)] for j in range(8)]

# Colocar las piezas blancas
board[0] = [WHITE + ROOK, WHITE + KNIGHT, WHITE + BISHOP, WHITE + QUEEN, WHITE + KING, WHITE + BISHOP, WHITE + KNIGHT, WHITE + ROOK]
board[1] = [WHITE + PAWN] * 8

# Colocar las piezas negras
board[7] = [BLACK + ROOK, BLACK + KNIGHT, BLACK + BISHOP, BLACK + QUEEN, BLACK + KING, BLACK + BISHOP, BLACK + KNIGHT, BLACK + ROOK]
board[6] = [BLACK + PAWN] * 8

# Imprimir el tablero
print("   A B C D E F G H")
for i, row in enumerate(board):
    print(f"{8 - i} ", end="")
    for square in row:
        print(square + RESET, end=" ")
    print()
print()

# Reglas de movimiento para la torre (rook)
def valid_rook_move(start_row, start_col, end_row, end_col):
    return start_row == end_row or start_col == end_col

# Reglas de movimiento para el caballo (knight)
def valid_knight_move(start_row, start_col, end_row, end_col):
    row_diff = abs(start_row - end_row)
    col_diff = abs(start_col - end_col)
    return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

# Reglas de movimiento para el alfil (bishop)
def valid_bishop_move(start_row, start_col, end_row, end_col):
    row_diff = abs(start_row - end_row)
    col_diff = abs(start_col - end_col)
    return row_diff == col_diff

# Reglas de movimiento para la reina (queen)
def valid_queen_move(start_row, start_col, end_row, end_col):
    return valid_rook_move(start_row, start_col, end_row, end_col) or valid_bishop_move(start_row, start_col, end_row, end_col)

# Reglas de movimiento para el rey (king)
def valid_king_move(start_row, start_col, end_row, end_col):
    row_diff = abs(start_row - end_row)
    col_diff = abs(start_col - end_col)
    return row_diff <= 1 and col_diff <= 1

# Reglas de movimiento para el peón (pawn)
def valid_pawn_move(start_row, start_col, end_row, end_col, color):
    if color == "white":
        return end_row - start_row == 1 and start_col == end_col
    elif color == "black":
        return start_row - end_row == 1 and start_col == end_col
    return False

# Ejemplo
def main():
    # Solicitar entrada de los jugadores
    player1 = input("Nombre del jugador 1: ")
    player2 = input("Nombre del jugador 2: ")

    # Variable para alternar entre jugadores
    current_player = player1

    while True:
        # Imprimir el tablero
        print("   A B C D E F G H")
        for i, row in enumerate(board):
            print(f"{8 - i} ", end="")
            for square in row:
                print(square + RESET, end=" ")
            print()
        print()

        # Solicitar movimiento al jugador actual
        print(f"Turno de {current_player}")
        start_pos = input("Ingrese la posición de inicio (por ejemplo, A2): ")
        end_pos = input("Ingrese la posición de destino (por ejemplo, A4): ")

        # Convertir las coordenadas a índices de matriz
        start_col = ord(start_pos[0]) - ord('A')
        start_row = 8 - int(start_pos[1])
        end_col = ord(end_pos[0]) - ord('A')
        end_row = 8 - int(end_pos[1])
        
        # Verificar si las coordenadas están dentro del rango válido
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print("Coordenadas fuera de rango. Inténtalo de nuevo.")
            continue

        # Obtener la pieza en la posición de inicio
        piece = board[start_row][start_col]

        # Verificar si el movimiento es válido según las reglas de la pieza
        valid_move = False

        if piece == ROOK:
            valid_move = valid_rook_move(start_row, start_col, end_row, end_col)
        elif piece == KNIGHT:
            valid_move = valid_knight_move(start_row, start_col, end_row, end_col)
        elif piece == BISHOP:
            valid_move = valid_bishop_move(start_row, start_col, end_row, end_col)
        elif piece == QUEEN:
            valid_move = valid_queen_move(start_row, start_col, end_row, end_col)
        elif piece == KING:
            valid_move = valid_king_move(start_row, start_col, end_row, end_col)
        elif piece == PAWN:
            color = "white" if current_player == player1 else "black"
            valid_move = valid_pawn_move(start_row, start_col, end_row, end_col, color)

        # Realizar el movimiento si es válido
        if valid_move:
            board[end_row][end_col] = piece
            board[start_row][start_col] = EMPTY
            print("Movimiento válido. ¡Pieza movida!")
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

        # Cambiar al siguiente jugador
        current_player = player2 if current_player == player1 else player1

        # Separador de turno
        print("\n---------------------\n")

if __name__ == "__main__":
    main()
