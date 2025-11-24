# game_logic.py
import random
from kbc_data import PRIZE_LADDER, SAFE_LEVELS

# --- Functional Module 1: Input/Output and Display ---

def display_question(q_data, question_num):
    """Prints the question, options, and current prize details."""
    prize = PRIZE_LADDER[question_num - 1]
    
    # Format the prize money with commas for readability
    print("-" * 50)
    print(f"💰 Question {question_num} for ₹{prize:,}")
    print("-" * 50)
    print(f"❓ {q_data['question']}")
    
    # Display the four options
    for option in q_data['options']:
        print(f"   {option}")

def get_user_answer():
    """Gets and validates the user's input."""
    valid_answers = ["A", "B", "C", "D"]
    
    while True:
        try:
            # Error Handling Strategy: Use a loop and try/except for robust input
            answer = input("\nYour answer (Enter A, B, C, or D to lock): ").upper()
            if answer == "QUIT":
                return "QUIT"
            if answer in valid_answers:
                return answer
            else:
                print("❌ Invalid entry. Please enter A, B, C, D, or QUIT.")
        except Exception:
            print("An unexpected input error occurred. Please try again.")

# --- Functional Module 2: Game State and Calculation ---

def calculate_winnings(current_level, is_correct):
    """
    Calculates the final prize money based on the game rules (safe levels).
    """
    
    # Check if the player won the current question
    if is_correct:
        # If correct, they win the prize for the current question
        return PRIZE_LADDER[current_level - 1]
    
    # If incorrect, calculate the safe prize money
    else:
        print("\n\t[Game Over] Wrong Answer!")
        
        # Check safe levels in reverse order (highest safe level reached)
        safe_amount = 0
        for level, prize in sorted(SAFE_LEVELS.items(), reverse=True):
            if current_level > level:
                safe_amount = prize
                break # Found the highest safe level
                
        if safe_amount > 0:
            print(f"You missed the question, but your guaranteed safe prize is ₹{safe_amount:,}.")
        else:
            print("You leave the game with ₹0, as you did not cross a safe zone.")
            
        return safe_amount # Returns the safe amount (or 0)