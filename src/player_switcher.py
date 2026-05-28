

class PlayerSwitcher :
    def __init__( self, player_names ) :
        self._names = player_names
        self._names_to_status = { x : True for x in player_names }
        self._index = 0

    def goto_next( self ) :
        self._names = [ k for k, v in self._names_to_status.items() if v ]
        self._shift_index()

    def get_name( self ) -> str :
        return self._names[ self._index ]

    def mark_skipped( self, name : str ) :
        skipped_element_index = self._names.index( name )
        self._names_to_status[ name ] = False
        if skipped_element_index < self._index :
            self._index -= 1

    def mark_unskipped( self, name : str ) :
        pass

    def _shift_index( self ) :
        if self._index < len( self._names ) - 1 :
            self._index += 1
        else :
            self._index = 0


class UserData :
    def __init__( self, name, password ) :
        self._name = name
        self._password = password

    @property
    def password( self ) :
        return self._password

