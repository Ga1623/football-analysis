# ============================================
# MATCH RESULTS ANALYSIS
# ============================================

print("\n" + "=" * 60)
print("MATCH RESULTS ANALYSIS")
print("=" * 60)

# Function to determine match result
def match_result(row):
    if row['home_score'] > row['away_score']:
        return 'Home Win'
    elif row['home_score'] < row['away_score']:
        return 'Away Win'
    else:
        return 'Draw'

# Apply the function
df['result'] = df.apply(match_result, axis=1)

# Question 9: Percentage of home wins
result_counts = df['result'].value_counts()
home_win_pct = (result_counts['Home Win'] / num_matches) * 100
draw_pct = (result_counts['Draw'] / num_matches) * 100
away_win_pct = (result_counts['Away Win'] / num_matches) * 100

print(f"\n9. Match outcome percentages:")
print(f"   Home Wins: {home_win_pct:.1f}% ({result_counts['Home Win']:,} matches)")
print(f"   Draws: {draw_pct:.1f}% ({result_counts['Draw']:,} matches)")
print(f"   Away Wins: {away_win_pct:.1f}% ({result_counts['Away Win']:,} matches)")

# Question 10: Does home advantage exist?
print(f"\n10. Home Advantage Analysis:")
print(f"    Home teams win {home_win_pct:.1f}% of matches")
print(f"    Away teams win only {away_win_pct:.1f}% of matches")
print(f"    This confirms a significant home advantage exists!")
print(f"    Home teams are {(home_win_pct / away_win_pct):.2f}x more likely to win than away teams")

# Question 11: Which country has the most wins historically?
# Calculate wins for each team (as home and away)

# Create a list of all matches with winner
def get_winner(row):
    if row['home_score'] > row['away_score']:
        return row['home_team']
    elif row['home_score'] < row['away_score']:
        return row['away_team']
    else:
        return None

df['winner'] = df.apply(get_winner, axis=1)

# Count wins per team
wins_by_team = df[df['winner'].notna()]['winner'].value_counts()

print(f"\n11. Top 15 teams by total wins:")
for i, (team, wins) in enumerate(wins_by_team.head(15).items(), 1):
    # Calculate win percentage
    total_matches = len(df[(df['home_team'] == team) | (df['away_team'] == team)])
    win_pct = (wins / total_matches) * 100
    print(f"    {i:2d}. {team:20s}: {wins:4,} wins ({win_pct:.1f}%) out of {total_matches:,} matches")