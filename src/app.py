import time

import pandas as pd
import streamlit as st

from main import monty_hall_game


st.set_page_config(
    page_title="Monty Hall Simulator",
    page_icon="🚪",
    layout="centered",
)

st.title("🚪 Monty Hall Simulator")

st.write(
    "Explore the Monty Hall problem and discover "
    "why switching doors can improve your chances of winning."
)

st.divider()

st.subheader("Simulation Settings")

num_games = st.number_input(
    "Number of games to simulate",
    min_value=1,
    max_value=10_000,
    value=1000,
    step=50,
)

delay = st.slider(
    "Animation delay (seconds)",
    min_value=0.0,
    max_value=0.2,
    value=0.05,
    step=0.01,
    help="Controls the pause between chart updates.",
)

if st.button("Run Simulation", type="primary"):
    stay_history = []
    switch_history = []

    stay_wins = 0
    switch_wins = 0

    st.divider()
    st.subheader("Live Simulation")

    progress = st.progress(0, text="Preparing simulation...")

    col1, col2 = st.columns(2)

    with col1:
        stay_metric = st.empty()
        stay_metric.metric(
            label="Win Rate Without Switching",
            value="0.00%",
        )

    with col2:
        switch_metric = st.empty()
        switch_metric.metric(
            label="Win Rate With Switching",
            value="0.00%",
        )

    st.subheader("Without Switching")
    stay_chart_placeholder = st.empty()

    st.subheader("With Switching")
    switch_chart_placeholder = st.empty()

    batch_size = 50

    for game_number in range(1, int(num_games) + 1):
        if monty_hall_game(switch_doors=False):
            stay_wins += 1

        if monty_hall_game(switch_doors=True):
            switch_wins += 1

        stay_history.append(stay_wins / game_number)
        switch_history.append(switch_wins / game_number)

        # Update the interface after each batch of games.
        if game_number % batch_size == 0 or game_number == num_games:
            stay_rate = stay_history[-1]
            switch_rate = switch_history[-1]

            stay_metric.metric(
                label="Win Rate Without Switching",
                value=f"{stay_rate:.2%}",
            )

            switch_metric.metric(
                label="Win Rate With Switching",
                value=f"{switch_rate:.2%}",
            )

            stay_chart = pd.DataFrame(
                {
                    "Game": range(1, game_number + 1),
                    "Cumulative Win Rate": stay_history,
                }
            )

            switch_chart = pd.DataFrame(
                {
                    "Game": range(1, game_number + 1),
                    "Cumulative Win Rate": switch_history,
                }
            )

            stay_chart_placeholder.line_chart(
                stay_chart,
                x="Game",
                y="Cumulative Win Rate",
                x_label="Game Number",
                y_label="Cumulative Win Rate",
                height=350,
            )

            switch_chart_placeholder.line_chart(
                switch_chart,
                x="Game",
                y="Cumulative Win Rate",
                x_label="Game Number",
                y_label="Cumulative Win Rate",
                height=350,
            )

            progress.progress(
                game_number / int(num_games),
                text=f"Simulating game {game_number:,} of {int(num_games):,}",
            )

            time.sleep(delay)

    progress.progress(1.0, text="Simulation completed!")

    st.success("Simulation completed successfully!")

    st.caption(
        f"Completed {int(num_games):,} games. "
        "Results vary because the simulation is random."
    )

st.divider()

st.caption(
    "The player chooses one of three doors. The host then "
    "reveals a goat behind another door."
)
