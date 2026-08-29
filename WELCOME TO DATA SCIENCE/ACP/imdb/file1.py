
# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 2. Import the dataset using Pandas
# ============================================================

df = pd.read_csv("IMDB Dataset.csv")


# ============================================================
# 3. Print the first three and last three rows of the dataset
# ============================================================

print("First 3 rows:")
print(df.head(3))

print("\nLast 3 rows:")
print(df.tail(3))


# ============================================================
# 4. Check the detailed information of the dataset
# ============================================================

print("\nDataset Information:")
df.info()


# ============================================================
# 5. Check if any null values are present in the dataset
# ============================================================

print("\nNull Values:")
print(df.isnull().sum())


# ============================================================
# 6. Create a subset with row numbers between 41 to 75
# ============================================================

# iloc uses Python indexing, so row 41 to 75 becomes 40:75
subset_df = df.iloc[40:75]

print("\nSubset from row 41 to row 75:")
print(subset_df)


# ============================================================
# 7. Check details of the movie with the highest number of votes
# ============================================================

highest_votes_movie = df.loc[df["No_of_Votes"].idxmax()]

print("\nMovie with the Highest Number of Votes:")
print(highest_votes_movie)


# ============================================================
# 8. Create boxplots for IMDB_Rating and Runtime
# ============================================================

plt.figure(figsize=(12, 5))

# Boxplot for IMDB_Rating
plt.subplot(1, 2, 1)
sns.boxplot(y=df["IMDB_Rating"])
plt.title("Boxplot of IMDB Rating")

# Boxplot for Runtime
plt.subplot(1, 2, 2)
sns.boxplot(y=df["Runtime"])
plt.title("Boxplot of Runtime")

plt.tight_layout()
plt.show()


# ============================================================
# 9. Check relationship between IMDB_Rating and Runtime
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(df["Runtime"], df["IMDB_Rating"])

plt.title("Relationship between Runtime and IMDB Rating")
plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")

plt.show()


# ============================================================
# 10. Check distribution of IMDB_Rating and Runtime
# ============================================================

plt.figure(figsize=(12, 5))

# Distribution of IMDB_Rating
plt.subplot(1, 2, 1)

sns.histplot(df["IMDB_Rating"], kde=True)

plt.title("Distribution of IMDB Rating")
plt.xlabel("IMDB Rating")


# Distribution of Runtime
plt.subplot(1, 2, 2)

sns.histplot(df["Runtime"], kde=True)

plt.title("Distribution of Runtime")
plt.xlabel("Runtime")

plt.tight_layout()
plt.show()


# ============================================================
# 11. Create a count plot of Rating
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Rating",
    order=df["Rating"].value_counts().index
)

plt.title("Number of Movies with Each Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()