import os
import pandas as pd
import matplotlib.pyplot as plt

#project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)

in_path = "data/processed/spotify_clean.csv"
fig_dir = "figures"
os.makedirs(fig_dir, exist_ok=True)

df = pd.read_csv(in_path)

print("Loaded:", in_path)
print("Rows, cols:", df.shape)

#duration distribution
plt.figure()
df["duration_seconds"].hist(bins=30)
plt.title("Song Duration Distribution (seconds)")
plt.xlabel("Duration (seconds)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "duration_distribution.png"), dpi=200)
plt.close()

#release year: tracks per year
tracks_per_year = df["release_year"].value_counts().sort_index()
plt.figure()
tracks_per_year.plot()
plt.title("Tracks per Release Year (Top 10k)")
plt.xlabel("Release Year")
plt.ylabel("Number of Tracks")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "tracks_per_year.png"), dpi=200)
plt.close()

#explicit vs non-explicit
plt.figure()
df["explicit"].value_counts().plot(kind="bar")
plt.title("Explicit vs Non-explicit Tracks")
plt.xlabel("Explicit")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "explicit_counts.png"), dpi=200)
plt.close()

#explicit share by rank bucket
explicit_by_bucket = df.groupby("rank_bucket")["explicit"].apply(lambda s: (s == "Yes").mean()).sort_index()
plt.figure()
explicit_by_bucket.plot(kind="bar")
plt.title("Share of Explicit Tracks by Rank Bucket")
plt.xlabel("Rank Bucket")
plt.ylabel("Share Explicit")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "explicit_share_by_rank_bucket.png"), dpi=200)
plt.close()

#collaboration share by rank bucket
collab_by_bucket = df.groupby("rank_bucket")["is_collaboration"].mean().sort_index()
plt.figure()
collab_by_bucket.plot(kind="bar")
plt.title("Share of Collaboration Tracks by Rank Bucket")
plt.xlabel("Rank Bucket")
plt.ylabel("Share Collaboration")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "collab_share_by_rank_bucket.png"), dpi=200)
plt.close()

#top 15 artists
exploded = df.explode("artist_list")
top_artists = exploded["artist_list"].value_counts().head(15).sort_values()

plt.figure()
top_artists.plot(kind="barh")
plt.title("Top 15 Artists by # of Tracks in Top 10k")
plt.xlabel("Track Count")
plt.ylabel("Artist")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "top_15_artists.png"), dpi=200)
plt.close()

print("EDA complete. Check the figures.")
