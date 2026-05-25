from src.player_switcher import PlayerSwitcher, UserData


# Test Driven Development (TDD)

def test_player_switcher_1() :
    names = list( 'abcd' )
    ps = PlayerSwitcher( names )

    assert ps.get_name() == 'a'
    # return self._names[ self._index ]

    ps.goto_next()
    assert ps.get_name() == 'b'

    ps.goto_next()
    assert ps.get_name() == 'c'

    ps.goto_next()
    assert ps.get_name() == 'd'

    ps.goto_next()
    assert ps.get_name() == 'a'


def test_player_switcher_2() :
    names = list( 'abcd' )
    ps = PlayerSwitcher( names )

    ps.mark_skipped( 'c' )

    ps.goto_next()
    ps.goto_next()

    assert ps.get_name() == 'd'




