import pandas as pd


def load_metadata(path: str, nrows=None):
    """Load metadata CSV with optional row limit."""
    df = pd.read_csv(path, nrows=nrows)
    return df


def clean_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich metadata DataFrame."""
    df = df.copy()
    
    # Parse publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    
    # Fill missing values
    df['abstract'] = df['abstract'].fillna('')
    df['title'] = df['title'].fillna('')
    df['journal'] = df['journal'].fillna('Unknown')
    
    # Abstract word count
    df['abstract_word_count'] = df['abstract'].str.split().apply(len)
    
    return df


def top_journals(df: pd.DataFrame, top_n=10):
    """Return top N journals by publication count."""
    return df['journal'].value_counts().nlargest(top_n)


def title_word_counts(df: pd.DataFrame, top_n=50):
    """Return most common words in titles without using collections.Counter."""
    all_titles = ' '.join(df['title'].dropna().astype(str)).lower()
    words = [w for w in all_titles.split() if w.isalpha() and len(w) > 2]
    
    # Use pandas Series for counting instead of Counter
    word_series = pd.Series(words)
    word_counts = word_series.value_counts().head(top_n)
    
    # Return as list of tuples (word, count) for compatibility
    return list(word_counts.items())
