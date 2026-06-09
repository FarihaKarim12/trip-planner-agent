# api.py — OpenAI API Integration
# Sends the structured itinerary to OpenAI and returns a natural-language travel plan.
# Uses carefully engineered prompts for best output quality.

import os
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

SYSTEM_PROMPT = """You are an expert travel guide and trip planner with encyclopedic knowledge 
of destinations worldwide. Your role is to transform a structured travel itinerary into a 
beautifully written, practical, and engaging day-by-day travel guide.

Guidelines:
- Write in a warm, enthusiastic, and informative tone
- For each day, provide a cohesive narrative (not just a list)
- Add practical tips: best time to visit, what to wear, must-try foods nearby
- Include estimated timing for each activity
- End with a brief overview of estimated total costs
- Use clear Day headings (Day 1:, Day 2:, etc.)
- Keep it friendly and exciting — make the reader look forward to the trip!
"""

def generate_travel_plan(structured_itinerary_text: str, destination: str, num_days: int, budget: float) -> str:
    """
    Send a structured itinerary to OpenAI and receive a human-readable travel plan.

    Args:
        structured_itinerary_text : plain-text representation of the itinerary
        destination               : city name (used to enrich the prompt)
        num_days                  : trip length
        budget                    : user's total budget

    Returns:
        str — AI-generated travel plan, or an error message
    """
    if not OPENAI_API_KEY:
        # Return a nicely formatted mock response if no API key is set
        return _mock_travel_plan(structured_itinerary_text, destination, num_days, budget)

    user_prompt = f"""
Please create a detailed, engaging day-by-day travel itinerary for the following trip:

{structured_itinerary_text}

Total Budget: ${budget}
Trip Duration: {num_days} days in {destination}

Transform this into a beautifully written travel guide with:
1. A brief exciting introduction to the destination
2. Detailed day-by-day plans with timing suggestions
3. Practical tips for each activity
4. Local food recommendations
5. A brief budget breakdown at the end

Make it feel like advice from a well-traveled friend!
"""

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": user_prompt},
                ],
                "max_tokens": 1500,
                "temperature": 0.7,
            },
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "OpenAI request timed out. Showing structured plan instead.\n\n" + structured_itinerary_text
    except requests.exceptions.HTTPError as e:
        return f"OpenAI API error: {e}\n\nStructured Plan:\n{structured_itinerary_text}"
    except Exception as e:
        return f"Unexpected error: {e}\n\nStructured Plan:\n{structured_itinerary_text}"


def _mock_travel_plan(structured_text: str, destination: str, num_days: int, budget: float) -> str:
    """
    Returns a formatted mock travel plan when no OpenAI key is provided.
    Parses the structured itinerary and formats it nicely.
    """
    lines = structured_text.strip().split("\n")
    
    output = []
    output.append(f"YOUR {num_days}-DAY {destination.upper()} ADVENTURE")
    output.append(f"Welcome to {destination}! Get ready for an unforgettable journey.")
    output.append(f"Your budget: ${budget:.0f} | Duration: {num_days} days")
    
    current_day = None
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Day ") and stripped.endswith(":"):
            current_day = stripped
            output.append(f"{stripped}")
        elif stripped.startswith("- ") and current_day:
            # Parse activity line
            activity_text = stripped[2:]
            name = activity_text.split(" (")[0]
            output.append(f"{name}")
            if "Cost:" in activity_text:
                cost_part = activity_text.split("Cost: $")[1].split(",")[0]
                duration_part = activity_text.split("Duration: ")[1].split("h")[0] if "Duration:" in activity_text else "2"
                output.append(f"Cost: ${cost_part}  -{duration_part} hours")
        elif stripped.startswith("Total Budget Used:"):
            output.append("")
            output.append("BUDGET SUMMARY")
            output.append(f"{stripped}")
    
    return "\n".join(output)