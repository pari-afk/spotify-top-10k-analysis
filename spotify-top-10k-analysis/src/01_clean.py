import os
import pandas as pd

#project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)

raw_path = "data/raw/spotify_top10k.csv"
out_path = "data/processed/spotify_clean.csv"

#duplicate tracks dropped by spotify track id
df = pd.read_csv(raw_path)

if "track_id" in df.columns:
    df = df.drop_duplicates(subset="track_id")

#duration: MM:SS to seconds
def duration_to_seconds(x):
    try:
        mins, secs = x.split(":")
        return int(mins) * 60 + int(secs)
    except:
        return None

df["duration_seconds"] = df["duration"].apply(duration_to_seconds)

#removing unrealistic durations (30s to 20 min)
df = df[df["duration_seconds"].between(30, 1200)]

#release date -> year
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["release_year"] = df["release_date"].dt.year
df = df[df["release_year"].between(1950, 2026)]

#flagging explicit
df["explicit"]=df["explicit"].map({0: "No", 1: "Yes"}).fillna(df["explicit"])

#artist list
df["artist_list"] = df["artist_names"].str.split("|")
df["num_artists"] = df["artist_list"].apply(len)
df["is_collaboration"] = df["num_artists"] > 1

#rank buckets
df["rank_bucket"] = pd.cut(
    df["rank"],
    bins=[0, 1000, 3000, 6000, 10000],
    labels=["Top 1k", "Top 3k", "Top 6k", "Top 10k"]
)

df.to_csv(out_path, index=False)

print("Cleaning complete")
print("Rows Kept:", len(df))
print("Saved to:", out_path)


                                

