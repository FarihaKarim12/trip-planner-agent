<<<<<<< HEAD
from data import get_activities, get_accommodation_cost, get_destinations
from search import bfs_search, greedy_best_first_search, summarize_itinerary
from csp import check_constraints

class TravelAgent:
    """
    Goal-based agent that plans travel itineraries.

    Workflow:
        1. Perceive user inputs
        2. Load environment (activity dataset)
        3. Run BFS to verify a valid solution exists (uninformed search)
        4. Run Greedy Best-First Search for the optimized solution (informed search)
        5. Validate final itinerary against CSP constraints
        6. Return structured itinerary for OpenAI formatting
    """

    def __init__(self):
        self.destinations = get_destinations()

    def perceive(self, destination, num_days, budget, interests):
        """
        Percept function: validate and store environment inputs.

        Returns:
            dict of validated inputs, or raises ValueError
        """
        if destination not in self.destinations:
            raise ValueError(f"Unknown destination '{destination}'. "
                             f"Choose from: {self.destinations}")
        if num_days < 1 or num_days > 14:
            raise ValueError("Number of days must be between 1 and 14.")
        if budget < 1:
            raise ValueError("Budget must be a positive number.")

        return {
            "destination": destination,
            "num_days": num_days,
            "budget": budget,
            "interests": interests or [],
        }

    def plan(self, destination, num_days, budget, interests):
        """
        Main agent action: produce an optimized travel itinerary.

        Args:
            destination : str  — city name
            num_days    : int  — trip length
            budget      : float — total USD budget
            interests   : list of str — e.g. ["food", "history"]

        Returns:
            dict with keys:
                'itinerary'   : list of days (each day = list of activity dicts)
                'summary'     : cost/duration breakdown
                'search_used' : which algorithm produced the final plan
                'bfs_found'   : whether BFS found any valid plan
        """
        # Step 1: Perceive
        percepts = self.perceive(destination, num_days, budget, interests)

        # Step 2: Load environment
        activities = get_activities(destination)
        accommodation = get_accommodation_cost(destination)

        # Step 3: Uninformed Search — BFS to check feasibility
        bfs_result = bfs_search(
            activities, num_days, budget, accommodation, interests
        )
        bfs_found = bfs_result is not None

        # Step 4: Informed Search — Greedy Best-First for optimized plan
        greedy_result = greedy_best_first_search(
            activities, num_days, budget, accommodation, interests
        )

        # Step 5: Select best result
        if greedy_result:
            final_itinerary = greedy_result
            search_used = "Greedy Best-First Search"
        elif bfs_result:
            final_itinerary = bfs_result
            search_used = "BFS (fallback)"
        else:
            raise ValueError(
                "No valid itinerary found within your budget and duration constraints. "
                "Try increasing your budget or reducing the number of days."
            )

        # Step 6: CSP validation
        valid, reason = check_constraints(final_itinerary, num_days, budget, accommodation)
        if not valid:
            raise ValueError(f"CSP constraint violated: {reason}")

        # Step 7: Build summary
        summary = summarize_itinerary(final_itinerary, accommodation)

        return {
            "destination": destination,
            "interests": interests,
            "itinerary": final_itinerary,
            "summary": summary,
            "search_used": search_used,
            "bfs_found": bfs_found,
        }

    def format_for_prompt(self, plan_result):
        """
        Convert structured itinerary into a text block for OpenAI prompt.

        Returns a clean, structured string describing the day-wise plan.
        """
        dest = plan_result["destination"]
        interests = ", ".join(plan_result["interests"]) if plan_result["interests"] else "general"
        summary = plan_result["summary"]
        itinerary = plan_result["itinerary"]

        lines = [
            f"Destination: {dest}",
            f"Duration: {summary['days']} days",
            f"Total Budget Used: ${summary['total_cost']} "
            f"(Activities: ${summary['total_activity_cost']}, "
            f"Accommodation: ${summary['total_accommodation_cost']})",
            f"User Interests: {interests}",
            f"Algorithm: {plan_result['search_used']}",
            "",
            "Planned Activities:",
        ]

        for i, day in enumerate(itinerary, 1):
            lines.append(f"\n  Day {i}:")
            for activity in day:
                tags = ", ".join(activity["interest"])
                lines.append(
                    f"    - {activity['name']} "
                    f"(Cost: ${activity['cost']}, Duration: {activity['duration']}h, "
                    f"Tags: {tags})"
                )

=======
from data import get_activities, get_accommodation_cost, get_destinations
from search import bfs_search, greedy_best_first_search, summarize_itinerary
from csp import check_constraints

class TravelAgent:
    """
    Goal-based agent that plans travel itineraries.

    Workflow:
        1. Perceive user inputs
        2. Load environment (activity dataset)
        3. Run BFS to verify a valid solution exists (uninformed search)
        4. Run Greedy Best-First Search for the optimized solution (informed search)
        5. Validate final itinerary against CSP constraints
        6. Return structured itinerary for OpenAI formatting
    """

    def __init__(self):
        self.destinations = get_destinations()

    def perceive(self, destination, num_days, budget, interests):
        """
        Percept function: validate and store environment inputs.

        Returns:
            dict of validated inputs, or raises ValueError
        """
        if destination not in self.destinations:
            raise ValueError(f"Unknown destination '{destination}'. "
                             f"Choose from: {self.destinations}")
        if num_days < 1 or num_days > 14:
            raise ValueError("Number of days must be between 1 and 14.")
        if budget < 1:
            raise ValueError("Budget must be a positive number.")

        return {
            "destination": destination,
            "num_days": num_days,
            "budget": budget,
            "interests": interests or [],
        }

    def plan(self, destination, num_days, budget, interests):
        """
        Main agent action: produce an optimized travel itinerary.

        Args:
            destination : str  — city name
            num_days    : int  — trip length
            budget      : float — total USD budget
            interests   : list of str — e.g. ["food", "history"]

        Returns:
            dict with keys:
                'itinerary'   : list of days (each day = list of activity dicts)
                'summary'     : cost/duration breakdown
                'search_used' : which algorithm produced the final plan
                'bfs_found'   : whether BFS found any valid plan
        """
        # Step 1: Perceive
        percepts = self.perceive(destination, num_days, budget, interests)

        # Step 2: Load environment
        activities = get_activities(destination)
        accommodation = get_accommodation_cost(destination)

        # Step 3: Uninformed Search — BFS to check feasibility
        bfs_result = bfs_search(
            activities, num_days, budget, accommodation, interests
        )
        bfs_found = bfs_result is not None

        # Step 4: Informed Search — Greedy Best-First for optimized plan
        greedy_result = greedy_best_first_search(
            activities, num_days, budget, accommodation, interests
        )

        # Step 5: Select best result
        if greedy_result:
            final_itinerary = greedy_result
            search_used = "Greedy Best-First Search"
        elif bfs_result:
            final_itinerary = bfs_result
            search_used = "BFS (fallback)"
        else:
            raise ValueError(
                "No valid itinerary found within your budget and duration constraints. "
                "Try increasing your budget or reducing the number of days."
            )

        # Step 6: CSP validation
        valid, reason = check_constraints(final_itinerary, num_days, budget, accommodation)
        if not valid:
            raise ValueError(f"CSP constraint violated: {reason}")

        # Step 7: Build summary
        summary = summarize_itinerary(final_itinerary, accommodation)

        return {
            "destination": destination,
            "interests": interests,
            "itinerary": final_itinerary,
            "summary": summary,
            "search_used": search_used,
            "bfs_found": bfs_found,
        }

    def format_for_prompt(self, plan_result):
        """
        Convert structured itinerary into a text block for OpenAI prompt.

        Returns a clean, structured string describing the day-wise plan.
        """
        dest = plan_result["destination"]
        interests = ", ".join(plan_result["interests"]) if plan_result["interests"] else "general"
        summary = plan_result["summary"]
        itinerary = plan_result["itinerary"]

        lines = [
            f"Destination: {dest}",
            f"Duration: {summary['days']} days",
            f"Total Budget Used: ${summary['total_cost']} "
            f"(Activities: ${summary['total_activity_cost']}, "
            f"Accommodation: ${summary['total_accommodation_cost']})",
            f"User Interests: {interests}",
            f"Algorithm: {plan_result['search_used']}",
            "",
            "Planned Activities:",
        ]

        for i, day in enumerate(itinerary, 1):
            lines.append(f"\n  Day {i}:")
            for activity in day:
                tags = ", ".join(activity["interest"])
                lines.append(
                    f"    - {activity['name']} "
                    f"(Cost: ${activity['cost']}, Duration: {activity['duration']}h, "
                    f"Tags: {tags})"
                )

>>>>>>> 8589fb43ed2959927bc961d281d88a84f4bd1a8f
        return "\n".join(lines)