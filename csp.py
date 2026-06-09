def check_constraints(itinerary, num_days, total_budget, accommodation_cost_per_day):
    """
    Validate a complete or partial itinerary against hard constraints.

    Constraints:
      1. Total cost (activities + accommodation) must not exceed budget.
      2. Number of days in itinerary must equal num_days.
      3. Each day must have at least 1 activity.

    Returns:
        (bool, str) — (is_valid, reason_if_invalid)
    """
    # Constraint 1: Duration
    if len(itinerary) != num_days:
        return False, f"Duration mismatch: expected {num_days} days, got {len(itinerary)}"

    # Constraint 2: Each day must have activities
    for i, day_activities in enumerate(itinerary):
        if not day_activities:
            return False, f"Day {i+1} has no activities"

    # Constraint 3: Total budget
    total_activity_cost = sum(
        activity["cost"]
        for day in itinerary
        for activity in day
    )
    total_accommodation = accommodation_cost_per_day * num_days
    total_cost = total_activity_cost + total_accommodation

    if total_cost > total_budget:
        return False, f"Exceeds budget: ${total_cost} > ${total_budget}"

    return True, "Valid"


def can_extend(current_itinerary, candidate_activity, remaining_budget,
               remaining_days, accommodation_cost_per_day):
    """
    Pruning function: checks if adding an activity is feasible.
    Called during BFS/Greedy traversal to prune impossible branches early.

    Args:
        current_itinerary: list of days built so far
        candidate_activity: activity dict being considered
        remaining_budget: budget left after accommodation and current activities
        remaining_days: days not yet planned
        accommodation_cost_per_day: fixed daily hotel cost

    Returns:
        bool — True if adding this activity is still feasible
    """
    activity_cost = candidate_activity["cost"]

    # After adding this activity, check if remaining budget covers
    # accommodation for remaining days (minimum viable continuation)
    min_future_cost = accommodation_cost_per_day * remaining_days
    projected_spend = activity_cost + min_future_cost

    return projected_spend <= remaining_budget


def compute_budget_used(itinerary, accommodation_cost_per_day):
    """Calculate total money spent in a given itinerary."""
    activity_cost = sum(a["cost"] for day in itinerary for a in day)
    accommodation = accommodation_cost_per_day * len(itinerary)
    return activity_cost + accommodation