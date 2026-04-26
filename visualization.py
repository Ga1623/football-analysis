# ============================================
# VISUALIZATIONS
# ============================================

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('International Football Analysis (1872-2024)', fontsize=16, fontweight='bold')

# 1. Histogram of goals per match
axes[0,0].hist(df['total_goals'], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0,0].set_xlabel('Total Goals per Match')
axes[0,0].set_ylabel('Number of Matches')
axes[0,0].set_title('Distribution of Goals Per Match')
axes[0,0].axvline(avg_goals, color='red', linestyle='--', linewidth=2, label=f'Mean: {avg_goals:.2f}')
axes[0,0].axvline(most_common_goals, color='green', linestyle='--', linewidth=2, label=f'Mode: {most_common_goals}')
axes[0,0].legend()
axes[0,0].set_xlim(0, 15)

# 2. Bar chart of match outcomes
outcome_colors = ['#2ecc71', '#f39c12', '#e74c3c']
axes[0,1].bar(result_counts.index, result_counts.values, color=outcome_colors, edgecolor='black')
axes[0,1].set_xlabel('Match Outcome')
axes[0,1].set_ylabel('Number of Matches')
axes[0,1].set_title('Match Outcomes Distribution')
for i, (outcome, count) in enumerate(result_counts.items()):
    axes[0,1].text(i, count + 500, f'{count:,}\n({count/num_matches*100:.1f}%)', 
                   ha='center', fontsize=10)

# 3. Top 10 teams by total wins (bar chart)
top_10_wins = wins_by_team.head(10)
colors = plt.cm.viridis(np.linspace(0, 0.8, 10))
axes[1,0].barh(range(len(top_10_wins)), top_10_wins.values, color=colors, edgecolor='black')
axes[1,0].set_yticks(range(len(top_10_wins)))
axes[1,0].set_yticklabels(top_10_wins.index)
axes[1,0].set_xlabel('Number of Wins')
axes[1,0].set_title('Top 10 Teams by Total Wins')
axes[1,0].invert_yaxis()
for i, (team, wins) in enumerate(top_10_wins.items()):
    axes[1,0].text(wins + 10, i, str(wins), va='center')

# 4. Goals over time (average goals per year)
df['year'] = df['date'].dt.year
yearly_avg_goals = df.groupby('year')['total_goals'].mean()
axes[1,1].plot(yearly_avg_goals.index, yearly_avg_goals.values, 'b-', linewidth=1, alpha=0.7)
axes[1,1].scatter(yearly_avg_goals.index, yearly_avg_goals.values, s=10, c='red', alpha=0.5)
axes[1,1].set_xlabel('Year')
axes[1,1].set_ylabel('Average Goals per Match')
axes[1,1].set_title('Evolution of Goals Per Match Over Time')
axes[1,1].axhline(avg_goals, color='gray', linestyle='--', alpha=0.5, label=f'Overall Avg: {avg_goals:.2f}')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Additional Visualization: Top 10 teams by home win percentage
print("\n" + "=" * 60)
print("ADDITIONAL INSIGHTS")
print("=" * 60)

# Calculate home win percentage for teams with at least 100 home matches
home_win_pct_by_team = []
for team in all_teams:
    home_matches = df[df['home_team'] == team]
    if len(home_matches) >= 100:
        home_wins = len(home_matches[home_matches['result'] == 'Home Win'])
        home_win_pct_by_team.append((team, home_wins/len(home_matches)*100, len(home_matches)))

home_win_pct_sorted = sorted(home_win_pct_by_team, key=lambda x: x[1], reverse=True)

print("\nTop 10 Teams by Home Win Percentage (minimum 100 home matches):")
for i, (team, pct, matches) in enumerate(home_win_pct_sorted[:10], 1):
    print(f"   {i:2d}. {team:20s}: {pct:.1f}% ({matches} home matches)")