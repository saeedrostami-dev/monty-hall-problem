from unittest.mock import patch

import pytest

from src.main import monty_hall_game, simulate_game


@pytest.mark.parametrize("num_games", [0, -1, -100])
def test_simulate_game_rejects_non_positive_numbers(num_games):
    with pytest.raises(ValueError):
        simulate_game(num_games)


@pytest.mark.parametrize("num_games", ["1000", 1.5, True, None])
def test_simulate_game_rejects_invalid_types(num_games):
    with pytest.raises(TypeError):
        simulate_game(num_games)


def test_simulate_game_when_every_game_is_won():
    with patch("src.main.monty_hall_game", return_value=True) as mock_game:
        stay_rate, switch_rate = simulate_game(10)

    assert stay_rate == 1.0
    assert switch_rate == 1.0
    assert mock_game.call_count == 20


@pytest.mark.parametrize(
    "initial_choice, revealed_door, switch_doors, expected_result",
    [
        (1, 2, True, True),    # Goat -> switch -> car: win
        (0, 1, True, False),   # Car -> switch -> goat: lose
        (0, 1, False, True),   # Car -> stay: win
        (1, 2, False, False),  # Goat -> stay: lose
    ],
)
def test_monty_hall_game(
    initial_choice, revealed_door, switch_doors, expected_result
):
    with (
        patch("src.main.random.shuffle"),
        patch(
            "src.main.random.randrange",
            return_value=initial_choice,
        ),
        patch(
            "src.main.random.choice",
            return_value=revealed_door,
        ),
    ):
        result = monty_hall_game(switch_doors=switch_doors)

    assert result is expected_result
