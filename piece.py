class Piece():

    def __init__(self, player, piece_symbol, crowned=False):
        self._player = player
        self._piece_symbol = piece_symbol
        self._crowned = crowned

    def get_crowned(self):
        return self._crowned

    # returns the player to whom the piece belongs
    def get_player(self):
        return self._player

    # sets the player to whom the piece belongs
    def set_player(self, player):
        self._player = player

    # returns the symbol of the piece
    def get_piece_symbol(self):
        return self._piece_symbol

    # sets the symbol of the piece
    def set_piece_symbol(self, piece_symbol):
        self._piece_symbol = piece_symbol

    # Crowns a piece
    @classmethod
    def crown_piece(cls):
        self._crowned = True

    player = property(get_player, set_player)
    piece_symbol = property(get_piece_symbol, set_piece_symbol)
    crowned = property(get_crowned)
