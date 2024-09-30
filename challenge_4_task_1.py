def assess_happiness(meet, boss):
    # Total number of people in the room
    num_people = len(meet)
    
    # Calculate total score, boss's score is doubled
    total_score = sum(meet[name] * 2 if name == boss else meet[name] for name in meet)
    
    # Calculate the average happiness rating
    average_rating = total_score / num_people
    
    # Assess the happiness
    if average_rating <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'

# Example Usage
meet = {
    'Alice': 6,
    'Bob': 4,
    'Charlie': 7,
    'David': 5
}
boss = 'Charlie'

print(assess_happiness(meet, boss))
