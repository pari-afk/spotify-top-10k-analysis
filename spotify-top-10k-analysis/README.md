# Spotify Top 10k Songs: Exploratory Data Analysis & Feature Engineering

## Overview
This project analyzes metadata from the Top 10,000 most popular Spotify songs to explore trends in popularity, song characteristics, and artist behaviour.
The goal is to transform raw metadata into an analysis-ready dataset, perform exploratory data analysis (EDA), and extract interpretable insights about modern music trends.

The dataset used:
Name: top-10k-spotify-songs-2025-07 (~10,000 tracks)
Source: Anna's Archive (Spotify metadata subset)

---

## Methods
The following machine learning techniques were applied:

### Data Cleaning & Feature Engineering

A reproducible preprocessing pipeline was implemented to prepare the raw dataset for analysis. Key steps included:
- Removing duplicate tracks using Spotify track IDs
- Converting song duration from MM:SS format to numeric seconds
- Filtering out unrealistic song durations (30 seconds to 20 minutes)
- Parsing release dates and extracting release year
- Standardizing explicit content labels
- Splitting artist strings into structured lists
- Creating collaboration indicators
- Grouping song ranks into interpretable popularity tiers

### Exploratory Data Analysis 
Exploratory analysis was conducted using visualizations to examine:
- Distribution of song durations
- Trends in track releases over time
- Explicit vs non-explicit content prevalence
- Collaboration patterns across popularity tiers
- Artist frequency among top-ranked tracks

---

## Key Results
- Most popular tracks cluster between 2–4 minutes in duration, with very few exceeding 10 minutes.
- The number of highly popular tracks increases sharply after 2015, reflecting the growth of the streaming era.
- Explicit content is more prevalent among higher-ranked songs, particularly in the Top 1k tier.
- Collaborations are more common in higher popularity tiers, suggesting cross-artist appeal may contribute to popularity.
- A relatively small group of artists accounts for a disproportionately large share of tracks in the Top 10k.

---

## Limitations
- The dataset represents a snapshot in time rather than longitudinal popularity trends.
- Analysis is limited to metadata and does not include Spotify audio features.
- No predictive modeling was performed in this project.
- Popularity scores and ranks are platform-specific and may change over time.

---

## Repository Structure

spotify-top-10k-analysis/
├── src/
│   ├── 01_clean.py
│   └── 02_eda.py
├── data/
│   ├── raw/
│   │   └── spotify_top10k.csv
│   └── processed/
│       └── spotify_clean.csv
├── figures/
├── requirements.txt
└── README.md

---

## How to Run
1. Install dependencies:
 pip install -r requirements.txt

2. Run data cleaning:
 python src/01_clean.py

3. Run exploratory data analysis:
 python src/02_eda.py

---

## Tech Stack
- Python
- pandas
- NumPy
- matplotlib

---

## Future Improvements

- Integration of Spotify audio features for deeper musical analysis
- Artist-level aggregation and trend analysis
- Popularity prediction or ranking models
- Clustering tracks based on metadata and audio features
- Time-series analysis of popularity changes


