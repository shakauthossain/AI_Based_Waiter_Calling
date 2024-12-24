def map_hand_to_employee(hand_x, hand_y, zones, employee_names):
    for i, (top_left, bottom_right) in enumerate(zones):
        if top_left[0] <= hand_x <= bottom_right[0] and top_left[1] <= hand_y <= bottom_right[1]:
            return employee_names[i]
    return None