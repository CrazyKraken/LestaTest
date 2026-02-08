def test_import_controller():
    from src.controller import GameController

    assert GameController is not None
    assert GameController.__name__ == "GameController"
