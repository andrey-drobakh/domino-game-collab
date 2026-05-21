import cl_interface as cli
import backend as be


def run_game() :
    md = be.MoveData()

    if cli.read_and_handle_player_names( md ) :
        return

    be.init_game( md )
    while not be.is_game_over( md ) :
        be.init_move( md )

        cli.display_hands( md )

        cli.display_prompt( md )
        cli.read_player_input( md )

        be.handle_player_input( md )

        cli.display_table_bones( md )
        cli.display_move_message( md )
    cli.display_game_results( md )


if __name__ == '__main__' :
    run_game()