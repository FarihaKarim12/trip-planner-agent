from flask import Flask, request, jsonify, send_from_directory
import os

from agent import TravelAgent
from api import generate_travel_plan

app = Flask(__name__, static_folder="frontend", static_url_path="")

# Initialize the travel agent (goal-based intelligent agent)
agent = TravelAgent()


@app.route("/")
def index():
    """Serve the main frontend page."""
    return send_from_directory("frontend", "index.html")


@app.route("/destinations", methods=["GET"])
def get_destinations():
    """Return all available travel destinations."""
    return jsonify({"destinations": agent.destinations})


@app.route("/plan", methods=["POST"])
def generate_plan():
    """
    Main route: receive user inputs and return a complete travel itinerary.

    Expected JSON body:
        {
            "destination": "Paris",
            "num_days": 3,
            "budget": 500,
            "interests": ["art", "food"]
        }

    Returns:
        {
            "success": true,
            "travel_plan": "...",           ← AI-generated text
            "structured": {...},             ← raw itinerary data
            "summary": {...},               ← cost breakdown
            "search_info": {...}            ← which algorithm was used
        }
    """
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), 400

    destination = data.get("destination", "").strip()
    num_days    = data.get("num_days", 3)
    budget      = data.get("budget", 500)
    interests   = data.get("interests", [])

    # Validate types
    try:
        num_days = int(num_days)
        budget   = float(budget)
    except (ValueError, TypeError):
        return jsonify({"success": False, "error": "Invalid num_days or budget"}), 400

    try:
        # Step 1: Run the agent to produce a structured itinerary
        plan_result = agent.plan(destination, num_days, budget, interests)

        # Step 2: Format itinerary for OpenAI prompt
        structured_text = agent.format_for_prompt(plan_result)

        # Step 3: Generate human-readable plan via OpenAI API
        travel_plan = generate_travel_plan(structured_text, destination, num_days, budget)

        # Step 4: Build response
        # Convert activity dicts to JSON-serializable format
        serialized_itinerary = [
            [
                {
                    "name":     activity["name"],
                    "cost":     activity["cost"],
                    "duration": activity["duration"],
                    "interest": activity["interest"],
                }
                for activity in day
            ]
            for day in plan_result["itinerary"]
        ]

        return jsonify({
            "success":     True,
            "travel_plan": travel_plan,
            "summary":     plan_result["summary"],
            "search_info": {
                "algorithm_used": plan_result["search_used"],
                "bfs_found_plan": plan_result["bfs_found"],
            },
            "itinerary":   serialized_itinerary,
        })

    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": f"Internal error: {str(e)}"}), 500


if __name__ == "__main__":
    print("🌍 AI Travel Planner Agent starting...")
    print("   Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)