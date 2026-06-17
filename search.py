<<<<<<< HEAD
from collections import deque
from csp import can_extend, compute_budget_used

def get_activities_per_day(total_activities, num_days, preferred=3):
    """Auto-calculate activities per day so we never exceed available pool."""
    max_possible = total_activities // num_days
    return max(1, min(preferred, max_possible))

def heuristic(activity, user_interests, remaining_budget):
    if user_interests:
        matching = sum(1 for tag in activity["interest"] if tag in user_interests)
        relevance = matching / len(activity["interest"])
    else:
        relevance = 0.5
    cost_ratio = activity["cost"] / (remaining_budget + 1)
    return (1 - relevance) + cost_ratio

def _combinations(lst, r):
    if r == 0:
        yield ()
        return
    for i in range(len(lst) - r + 1):
        for rest in _combinations(lst[i+1:], r - 1):
            yield (lst[i],) + rest

def bfs_search(activities, num_days, total_budget, accommodation_per_day,
               user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    queue = deque([([], initial_budget)])
    visited_count = 0
    while queue and visited_count < 2000:
        completed_days, remaining_budget = queue.popleft()
        visited_count += 1
        if len(completed_days) == num_days:
            return [[activities[i] for i in day] for day in completed_days]
        used_so_far = {i for day in completed_days for i in day}
        available = [i for i in range(n) if i not in used_so_far]
        cur_apd = min(apd, len(available))
        if cur_apd == 0:
            continue
        for combo in _combinations(available, cur_apd):
            day_cost = sum(activities[i]["cost"] for i in combo)
            if day_cost <= remaining_budget:
                queue.append((completed_days + [list(combo)], remaining_budget - day_cost))
                break
    return None

def dfs_search(activities, num_days, total_budget, accommodation_per_day,
               user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    stack = [([], initial_budget)]
    while stack:
        completed_days, remaining_budget = stack.pop()
        if len(completed_days) == num_days:
            return [[activities[i] for i in day] for day in completed_days]
        used_so_far = {i for day in completed_days for i in day}
        available = [i for i in range(n) if i not in used_so_far]
        cur_apd = min(apd, len(available))
        if cur_apd == 0:
            continue
        for combo in _combinations(available, cur_apd):
            day_cost = sum(activities[i]["cost"] for i in combo)
            if day_cost <= remaining_budget:
                stack.append((completed_days + [list(combo)], remaining_budget - day_cost))
                break
    return None

def greedy_best_first_search(activities, num_days, total_budget, accommodation_per_day,
                              user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    itinerary = []
    used_indices = set()
    remaining_budget = initial_budget

    for day_num in range(num_days):
        available = [(i, activities[i]) for i in range(n) if i not in used_indices]

        # If pool exhausted, allow reuse of all activities
        if len(available) < apd:
            all_acts = [(i, activities[i]) for i in range(n)]
            extra = [(i, a) for i, a in all_acts if (i, a) not in available]
            available = available + extra

        if not available:
            return None

        ranked = sorted(available, key=lambda x: heuristic(x[1], user_interests, remaining_budget))

        day_indices = []
        day_cost = 0
        for idx, activity in ranked:
            if len(day_indices) >= apd:
                break
            if day_cost + activity["cost"] <= remaining_budget:
                day_indices.append(idx)
                day_cost += activity["cost"]

        # Fallback: pick cheapest if nothing fits
        if not day_indices:
            cheapest = sorted(available, key=lambda x: x[1]["cost"])
            for idx, activity in cheapest[:apd]:
                day_indices.append(idx)
                day_cost += activity["cost"]

        if not day_indices:
            return None

        remaining_budget -= day_cost
        used_indices.update(day_indices)
        itinerary.append([activities[i] for i in day_indices])

    return itinerary if len(itinerary) == num_days else None

def summarize_itinerary(itinerary, accommodation_per_day):
    total_activity_cost = sum(a["cost"] for day in itinerary for a in day)
    total_accommodation = accommodation_per_day * len(itinerary)
    return {
        "days": len(itinerary),
        "total_activity_cost": total_activity_cost,
        "total_accommodation_cost": total_accommodation,
        "total_cost": total_activity_cost + total_accommodation,
        "activities_per_day": [len(day) for day in itinerary],
=======
from collections import deque
from csp import can_extend, compute_budget_used

def get_activities_per_day(total_activities, num_days, preferred=3):
    """Auto-calculate activities per day so we never exceed available pool."""
    max_possible = total_activities // num_days
    return max(1, min(preferred, max_possible))

def heuristic(activity, user_interests, remaining_budget):
    if user_interests:
        matching = sum(1 for tag in activity["interest"] if tag in user_interests)
        relevance = matching / len(activity["interest"])
    else:
        relevance = 0.5
    cost_ratio = activity["cost"] / (remaining_budget + 1)
    return (1 - relevance) + cost_ratio

def _combinations(lst, r):
    if r == 0:
        yield ()
        return
    for i in range(len(lst) - r + 1):
        for rest in _combinations(lst[i+1:], r - 1):
            yield (lst[i],) + rest

def bfs_search(activities, num_days, total_budget, accommodation_per_day,
               user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    queue = deque([([], initial_budget)])
    visited_count = 0
    while queue and visited_count < 2000:
        completed_days, remaining_budget = queue.popleft()
        visited_count += 1
        if len(completed_days) == num_days:
            return [[activities[i] for i in day] for day in completed_days]
        used_so_far = {i for day in completed_days for i in day}
        available = [i for i in range(n) if i not in used_so_far]
        cur_apd = min(apd, len(available))
        if cur_apd == 0:
            continue
        for combo in _combinations(available, cur_apd):
            day_cost = sum(activities[i]["cost"] for i in combo)
            if day_cost <= remaining_budget:
                queue.append((completed_days + [list(combo)], remaining_budget - day_cost))
                break
    return None

def dfs_search(activities, num_days, total_budget, accommodation_per_day,
               user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    stack = [([], initial_budget)]
    while stack:
        completed_days, remaining_budget = stack.pop()
        if len(completed_days) == num_days:
            return [[activities[i] for i in day] for day in completed_days]
        used_so_far = {i for day in completed_days for i in day}
        available = [i for i in range(n) if i not in used_so_far]
        cur_apd = min(apd, len(available))
        if cur_apd == 0:
            continue
        for combo in _combinations(available, cur_apd):
            day_cost = sum(activities[i]["cost"] for i in combo)
            if day_cost <= remaining_budget:
                stack.append((completed_days + [list(combo)], remaining_budget - day_cost))
                break
    return None

def greedy_best_first_search(activities, num_days, total_budget, accommodation_per_day,
                              user_interests, activities_per_day=3):
    initial_budget = total_budget - (accommodation_per_day * num_days)
    if initial_budget < 0:
        return None
    n = len(activities)
    apd = get_activities_per_day(n, num_days, activities_per_day)
    itinerary = []
    used_indices = set()
    remaining_budget = initial_budget

    for day_num in range(num_days):
        available = [(i, activities[i]) for i in range(n) if i not in used_indices]

        # If pool exhausted, allow reuse of all activities
        if len(available) < apd:
            all_acts = [(i, activities[i]) for i in range(n)]
            extra = [(i, a) for i, a in all_acts if (i, a) not in available]
            available = available + extra

        if not available:
            return None

        ranked = sorted(available, key=lambda x: heuristic(x[1], user_interests, remaining_budget))

        day_indices = []
        day_cost = 0
        for idx, activity in ranked:
            if len(day_indices) >= apd:
                break
            if day_cost + activity["cost"] <= remaining_budget:
                day_indices.append(idx)
                day_cost += activity["cost"]

        # Fallback: pick cheapest if nothing fits
        if not day_indices:
            cheapest = sorted(available, key=lambda x: x[1]["cost"])
            for idx, activity in cheapest[:apd]:
                day_indices.append(idx)
                day_cost += activity["cost"]

        if not day_indices:
            return None

        remaining_budget -= day_cost
        used_indices.update(day_indices)
        itinerary.append([activities[i] for i in day_indices])

    return itinerary if len(itinerary) == num_days else None

def summarize_itinerary(itinerary, accommodation_per_day):
    total_activity_cost = sum(a["cost"] for day in itinerary for a in day)
    total_accommodation = accommodation_per_day * len(itinerary)
    return {
        "days": len(itinerary),
        "total_activity_cost": total_activity_cost,
        "total_accommodation_cost": total_accommodation,
        "total_cost": total_activity_cost + total_accommodation,
        "activities_per_day": [len(day) for day in itinerary],
>>>>>>> 8589fb43ed2959927bc961d281d88a84f4bd1a8f
    }