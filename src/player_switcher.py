

class PlayerSwitcher :
    def __init__( self, player_names ) :
        self._names = player_names
        self._index = 0

    def goto_next( self ) :
        PlayerSwitcher.user = 0
        if self._index != len( self._names ) - 1 :
            self._index += 1
        else :
            self._index = 0

    def get_name( self ) -> str :
        return self._names[ self._index ]

    def mark_skipped( self, name : str ) :
        pass

    def mark_unskipped( self, name : str ) :
        pass


class UserData :
    def __init__( self, name, password ) :
        self._name = name
        self._password = password

    @property
    def password( self ) :
        return self._password

