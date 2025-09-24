import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Streamlit page setup ---
st.set_page_config(page_title='CORD-19 Data Explorer', layout='wide')
st.title('CORD-19 Data Explorer')
st.write('Interactive exploration of the CORD-19 metadata file')


# --- Helper functions (inline) ---
@st.cache_data
def load_and_clean(path: str):
    df = pd.read_csv(path)

    # Parse publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year

    # Handle missing values
    df['abstract'] = df['abstract'].fillna('')
    df['title'] = df['title'].fillna('')
    df['journal'] = df['journal'].fillna('Unknown')

    # Add abstract word count
    df['abstract_word_count'] = df['abstract'].str.split().apply(len)

    return df


# --- Load data ---
DATA_PATH = 'data/metadata.csv'
df = load_and_clean(DATA_PATH)


# --- Sidebar controls ---
min_year = int(df['year'].dropna().min())
max_year = int(df['year'].dropna().max())

year_range = st.sidebar.slider(
    'Select year range',
    min_year, max_year,
    (2019, max_year)
)

selected_journal = st.sidebar.selectbox(
    'Select journal (All)',
    ['All'] + list(df['journal'].dropna().unique())[:200]
)


# --- Filter data ---
mask = df['year'].between(year_range[0], year_range[1])
if selected_journal != 'All':
    mask = mask & (df['journal'] == selected_journal)

filtered = df[mask]


# --- Summary ---
st.subheader('Summary')
col1, col2, col3 = st.columns(3)
col1.metric('Total papers (filtered)', len(filtered))
col2.metric('Unique journals', filtered['journal'].nunique())
col3.metric('Avg abstract words', int(filtered['abstract_word_count'].mean()))


# --- Publications over time ---
st.subheader('Publications by year')
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index.astype(int), year_counts.values)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)


# --- Top journals ---
st.subheader('Top publishing journals')
top_n = st.sidebar.slider('Top N journals', 5, 50, 10)
journal_counts = filtered['journal'].value_counts().nlargest(top_n)

fig2, ax2 = plt.subplots()
sns.barplot(x=journal_counts.values, y=journal_counts.index, ax=ax2)
ax2.set_xlabel('Count')
st.pyplot(fig2)


# --- Data sample ---
st.subheader('Data sample')
st.dataframe(
    filtered[['cord_uid', 'title', 'journal', 'publish_time', 'abstract']].head(200)
)
