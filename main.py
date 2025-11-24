# main.py

import random
from kbc_data import QUESTIONS, PRIZE_LADDER, SAFE_LEVELS
from game_logic import display_question, get_user_answer, calculate_winnings

def main():
    """The main function to orchestrate the KBC game flow."""
    
    # Start the game state
    current_winnings = 0
    game_running = True
    
    print("*" * 60)
    print("        💰 KBC (Kaun Banega Crorepati) Python Simulation 💰")
    print("*" * 60)
    print("Welcome! You must answer all questions correctly to win the top prize.")
    print(f"Total questions: {len(QUESTIONS)}. Safe levels at Q{list(SAFE_LEVELS.keys())[0]} and Q{list(SAFE_LEVELS.keys())[1]}.\n")
    
    # Shuffle the questions to ensure replayability
    random.shuffle(QUESTIONS) 
    
    # Start the main game loop
    for question_index, q_data in enumerate(QUESTIONS):
        if not game_running:
            break

        question_num = question_index + 1
        
        # 1. Display the current state and question
        display_question(q_data, question_num)
        
        # Display current safe amount for context
        # (This is a non-functional requirement related to usability)
        safe_amount = SAFE_LEVELS.get(question_index, 0) # Use index for previous safe level
        if safe_amount > 0:
            print(f"🎁 Note: The previous safe prize you secured is ₹{safe_amount:,}.")
        else:
            print(f"🎁 Note: Your current winnings are ₹{current_winnings:,}.")


        # 2. Get user input
        user_choice = get_user_answer()
        
        if user_choice == "QUIT":
            print(f"\nPlayer chose to walk away. Final Winnings: ₹{current_winnings:,}")
            game_running = False
            continue

        # 3. Check answer and update state
        if user_choice == q_data['answer']:
            # Answer is correct
            current_winnings = PRIZE_LADDER[question_index]
            print(f"\n✅ Correct! You have won ₹{current_winnings:,}!")
            
            if question_num < len(QUESTIONS):
                 print("Moving to the next question...")
            
        else:
            # Answer is wrong (trigger game over logic)
            final_prize = calculate_winnings(question_num, False)
            current_winnings = final_prize
            game_running = False
            
    # Final results after the loop finishes
    print("\n" + "=" * 60)
    if game_running:
        print(f"✨ GRAND WINNER! You have successfully answered all {len(QUESTIONS)} questions.")
        print(f"🏆 Final Prize Money: ₹{current_winnings:,} (₹1 Crore)")
    else:
        print(f"👋 Thank you for playing. Your final takeaway is ₹{current_winnings:,}")
    print("=" * 60)

if __name__ == "__main__":
    main()