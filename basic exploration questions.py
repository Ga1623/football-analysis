
print("\n" + "=" * 60)
print("BASIC EXPLORATION RESULTS")
print("=" * 60)

# Question 1: How many matches are in the dataset?
num_matches = df.shape[0]
print(f"\n1. Total number of matches in the dataset: {num_matches:,}")

# Question 2: What is the earliest and latest year in the data?
df['date'] = pd.to_datetime(df['date'])
earliest_date = df['date'].min()
latest_date = df['date'].max()
print(f"\n2. Earliest match date: {earliest_date.date()}")
print(f"   Latest match date: {latest_date.date()}")
print(f"   Date range spans: {latest_date.year - earliest_date.year} years")

# Question 3: How many unique countries are there?
# We need to consider both home and away teams
home_teams = set(df['home_team'].unique())
away_teams = set(df['away_team'].unique())
all_teams = home_teams.union(away_teams)
unique_countries = len(all_teams)
print(f"\n3. Number of unique countries/teams: {unique_countries}")

# Question 4: Which team appears most frequently as home team?
most_frequent_home = df['home_team'].value_counts().head(10)
print(f"\n4. Top 10 teams by appearances as home team:")
for i, (team, count) in enumerate(most_frequent_home.items(), 1):
    print(f"   {i}. {team}: {count:,} matches")