# Module 1: quiz_data.py
# Purpose: Holds the immutable data for the game. This separation ensures
# high Maintainability (NFR) and fulfills the Data Initialization (FR1).
# The prize money ladder. Index 2 (Q2) and Index 7 (Q7) are Safe Havens.

MONEY_LADDER = [
    0, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000
]

# The list of all questions.
QUESTIONS = [
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Jupiter", "Mars", "Venus", "Saturn"],
        "answer_index": 2, # Answer is the 2nd option: Mars
        "5050_removal": [1, 4] # Indices of incorrect options to remove
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"],
        "answer_index": 3,
        "5050_removal": [1, 2]
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["Kyoto", "Osaka", "Seoul", "Tokyo"],
        "answer_index": 4,
        "5050_removal": [1, 2]
    },
    {
        "question": "The chemical symbol 'H2O' represents what?",
        "options": ["Hydrogen", "Oxygen", "Water", "Carbon Dioxide"],
        "answer_index": 3,
        "5050_removal": [2, 4]
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer_index": 4,
        "5050_removal": [2, 3]
    },
    {
        "question": "How many players are on a soccer (football) team?",
        "options": ["9", "10", "11", "12"],
        "answer_index": 3,
        "5050_removal": [1, 4]
    },
    {
        "question": "What is the freezing point of water in Celsius?",
        "options": ["0°C", "10°C", "-10°C", "100°C"],
        "answer_index": 1,
        "5050_removal": [2, 4]
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["Hyper Text Transfer Protocol", "High Technology Test Program", "Hyperlink Technical Transfer", "High Traffic Terminal Process"],
        "answer_index": 1,
        "5050_removal": [3, 4]
    },
    {
        "question": "Which animal is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Great White Shark"],
        "answer_index": 3,
        "5050_removal": [1, 2]
    }
]