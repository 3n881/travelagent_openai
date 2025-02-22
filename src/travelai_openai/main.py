#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from travelai_openai.crew import TravelaiOpenai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'source_location': 'pune',
        'destination_location': 'jaipur',
        # 'travel_date': '2025-03-15',
        # 'travel_duration': '5 days',
        # 'number_of_travelers': '2',
        # 'travel_companions_type': 'Couple',
        # 'budget_per_person': '15000',
        # 'preferred_travel_mode': 'Flight',
        # 'accommodation_type': 'Hotel',
        # 'meal_preferences': 'Non-Veg',
        # 'interests': 'Nature',
        # 'accessibility_needs': 'Wheelchair accessible',
        # 'dietary_restrictions': 'Gluten-free',
        # 'special_requests': 'Early check-in and city view room',
        # 'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }
    
    try:
        TravelaiOpenai().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TravelaiOpenai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelaiOpenai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TravelaiOpenai().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
