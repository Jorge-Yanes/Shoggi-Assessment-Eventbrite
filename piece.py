class Piece:
    def __init__(self, player, piece_symbol, piece_type, crowned):
        self.player = player
        self.piece_symbol = piece_symbol
        self.piece_type = piece_type
        self.crowned = crowned

    # returns the player to whom the piece belongs
    @property
    def player(self):
        return self._player

    # sets the player to whom the piece belongs
    @player.setter
    def player(self, player):
        self._player = player

    # returns the symbol of the piece
    @property
    def piece_symbol(self):
        return self._piece_symbol

    # sets the symbol of the piece
    @piece_symbol.setter
    def piece_symbol(self, piece_symbol):
        self._piece_symbol = piece_symbol

    # returns the type of the piece
    @property
    def piece_type(self):
        return self._piece_type

    # sets the type of the piece
    @piece_type.setter
    def piece_type(self, piece_type):
        self._piece_type = piece_type

    # Crowns a piece
    def crown_piece(self):
        self.crowned = True
