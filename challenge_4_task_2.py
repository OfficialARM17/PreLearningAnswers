def boredom_assessment(staff):
    # Department boredom scores
    boredom_scores = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    
    # Calculate the total boredom score for the staff
    total_boredom = sum(boredom_scores[staff[person]] for person in staff)
    
    # Return the appropriate message based on the total score
    if total_boredom <= 80:
        return 'kill me now'
    elif total_boredom < 100:
        return 'i can handle this'
    else:
        return 'party time!!'

# Example Usage
staff = {
    'John': 'accounts',
    'Jane': 'canteen',
    'Jim': 'pissing about',
    'Jack': 'trading'
}

print(boredom_assessment(staff))
