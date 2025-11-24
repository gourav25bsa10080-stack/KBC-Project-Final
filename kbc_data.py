# kbc_data.py

# --- 1. Prize Money Structure ---
# List of prizes for each level. The index corresponds to the question number.
# Example: Index 0 is Question 1 (Prize: 1,000)
PRIZE_LADDER = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 
    640000, 1250000, 2500000, 5000000, 10000000
]

# --- 2. Safe Levels ---
# The amount guaranteed if a player gives a wrong answer after reaching this level.
# The index corresponds to the question number (e.g., Q5 and Q10 are safe points).
SAFE_LEVELS = {
    5: 10000,  # After Q5, guaranteed 10,000
    10: 320000 # After Q10, guaranteed 3,20,000
}

# --- 3. Question Bank ---
# List of dictionaries, each containing question details.
QUESTIONS = [
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["A. Lion", "B. Camel", "C. Elephant", "D. Tiger"],
        "answer": "B",
        "level": 1
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C",
        "level": 2
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C",
        "level": 3
    },
    {
        "question": "Which programming language is Python named after?",
        "options": ["A. A snake species", "B. A British comedy group", "C. A Greek philosopher", "D. A type of car"],
        "answer": "B",
        "level": 4
    },
    {
        "question": "In the context of computer science, what does 'CPU' stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Power Utility", "C. Core Program Upgrade", "D. Central Program Unit"],
        "answer": "A",
        "level": 5
    },
    {
        "question": "Which Indian state is known as the 'Land of Five Rivers'?",
        "options": ["A. Gujarat", "B. Punjab", "C. Maharashtra", "D. Kerala"],
        "answer": "B",
        "level": 6
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Ag", "B. Au", "C. Fe", "D. Na"],
        "answer": "B",
        "level": 7
    },
    {
        "question": "Which of these is NOT a functional requirement in a software project?",
        "options": ["A. User Login", "B. Data Reporting", "C. System Performance", "D. Payment Gateway"],
        "answer": "C",
        "level": 8 # Question related to the PDF requirements
    },
    {
        "question": "The primary language of the Bhagavad Gita is?",
        "options": ["A. Hindi", "B. Pali", "C. Sanskrit", "D. Marathi"],
        "answer": "C",
        "level": 9
    },
    {
        "question": "In an operating system, what is a 'Deadlock'?",
        "options": ["A. A security feature", "B. A state where processes wait indefinitely for resources", "C. A type of memory error", "D. A fast booting process"],
        "answer": "B",
        "level": 10
    },
    {
        "question": "Which data structure follows the LIFO (Last-In, First-Out) principle?",
        "options": ["A. Queue", "B. Array", "C. Stack", "D. Linked List"],
        "answer": "C",
        "level": 11
    },
    {
        "question": "Which famous scientist developed the Theory of Relativity?",
        "options": ["A. Isaac Newton", "B. Galileo Galilei", "C. Stephen Hawking", "D. Albert Einstein"],
        "answer": "D",
        "level": 12
    },
    {
        "question": "What is the standard port number for the HTTP protocol?",
        "options": ["A. 21", "B. 23", "C. 80", "D. 443"],
        "answer": "C",
        "level": 13
    },
    {
        "question": "Which country is the origin of the martial art 'Karate'?",
        "options": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
        "answer": "B",
        "level": 14
    },
    {
        "question": "Who is known as the 'Father of the Indian Constitution'?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. B. R. Ambedkar", "D. Sardar Vallabhbhai Patel"],
        "answer": "C",
        "level": 15
    },
]