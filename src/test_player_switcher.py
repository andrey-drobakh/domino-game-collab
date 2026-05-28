from src.player_switcher import PlayerSwitcher, UserData


# Test Driven Development (TDD)

def test_1() :
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


def test_2() :
    names = list( 'abcdefg' )
    ps = PlayerSwitcher( names )

    ps.mark_skipped( 'c' )
    ps.mark_skipped( 'f' )
    ps.mark_skipped( 'g' ) # добавил проверку


    ps.goto_next()
    ps.goto_next()

    assert ps.get_name() == 'd'

    ps.goto_next()
    ps.goto_next()
    ps.goto_next() # добавил пропуск

    assert ps.get_name() == 'b' # 'g' добавил проверку на предполагаемую 'b'


def test_3() :
    names = list( 'abcd' )
    ps = PlayerSwitcher( names )

    assert ps.get_name() == 'a'

    ps.goto_next()
    assert ps.get_name() == 'b'

    ps.goto_next()
    assert ps.get_name() == 'c'

    ps.goto_next()
    assert ps.get_name() == 'd'

    ps.mark_skipped( 'b' )
    # Остались игроки 'acd'

    ps.goto_next()
    assert ps.get_name() == 'a'


def test_4() :
    names = list( 'abcd' )
    ps = PlayerSwitcher( names )

    ps.goto_next()
    ps.goto_next()

    assert ps.get_name() == 'c'

    ps.mark_skipped( 'b' )

    ps.goto_next()

    assert ps.get_name() == 'd'
