Project Statement: KBC Simulation

📝 Problem Statement

The goal is to create a functional, terminal-based simulation of the popular game show, Kaun Banega Crorepati (KBC). This project will test the player's general knowledge through a series of multiple-choice questions with increasing prize money. The core challenge is to implement the game's complex financial logic, specifically the safe levels and walk-away option, using modular Python code.

🎯 Objectives

To apply Python programming concepts like data structures (lists, dictionaries) and functions.

To implement modular design principles by separating data, logic, and control flow into distinct files.

To ensure robust input handling to make the simulation reliable.

To accurately reflect the KBC game's prize money structure and safe-level rules.

⚙️ Scope of the Project

The current scope covers a fully functional single-player KBC simulation run entirely within the terminal. It includes:

A question bank with 15 questions.

A prize ladder up to ₹1 Crore.

Implementation of the two designated safe levels (Q5 and Q10).

Option for the user to quit and take their current winnings.

🧑‍💻 Target Users

The primary target users are:

Students/Peers: To showcase understanding of modular Python programming and algorithmic logic.

General Users: Anyone who wants to test their general knowledge in a KBC format.

⭐ High-Level Features

Modular Architecture: Separate files for Data, Logic, and Execution (kbc_data.py, game_logic.py, main.py).

Safe Levels: Guaranteed winnings at specified question milestones.

Input Validation: Handling of invalid user choices (non A/B/C/D inputs).

Session Persistence: The current winnings are tracked throughout the game session.
