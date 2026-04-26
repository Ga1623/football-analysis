
print("\n" + "=" * 60)
print("GOALS ANALYSIS RESULTS")
print("=" * 60)

# Create total goals column
df['total_goals'] = df['home_score'] + df['away_score']

# Question 5: Average number of goals per match
avg_goals = df['total_goals'].mean()
print(f"\n5. Average goals per match: {avg_goals:.2f}")

# Question 6: Highest scoring match
max_goals = df['total_goals'].max()
highest_scoring = df[df['total_goals'] == max_goals]
print(f"\n6. Highest scoring match(es) with {max_goals} total goals:")
for _, match in highest_scoring.iterrows():
    print(f"   {match['home_team']} {match['home_score']} - {match['away_score']} {match['away_team']} ({match['date'].date()})")

# Question 7: Are more goals scored at home or away?
total_home_goals = df['home_score'].sum()
total_away_goals = df['away_score'].sum()
print(f"\n7. Goals comparison:")
print(f"   Total home goals: {total_home_goals:,}")
print(f"   Total away goals: {total_away_goals:,}")
print(f"   Difference: {total_home_goals - total_away_goals:,} more goals at home")
print(f"   Home goals represent: {(total_home_goals/(total_home_goals+total_away_goals)*100):.1f}% of all goals")

# Question 8: Most common total goals value
most_common_goals = df['total_goals'].mode()[0]
goals_distribution = df['total_goals'].value_counts().sort_index()
print(f"\n8. Most common total goals value: {most_common_goals} goals")
print(f"\n   Goals distribution (top 10):")
for goals, count in goals_distribution.head(10).items():
    percentage = (count / num_matches) * 100
    print(f"   {goals} goal(s): {count:,} matches ({percentage:.1f}%)")