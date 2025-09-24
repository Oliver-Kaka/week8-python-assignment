# CORD-19 Metadata Explorer

This project provides a simple **data analysis workflow** and a **Streamlit web app** for exploring the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), focusing on the `metadata.csv` file.

---

## 🔍 How the analysis works

1. **Load the dataset**
   - The script reads the `metadata.csv` file (downloaded from Kaggle).
   - Missing values in key fields (`title`, `abstract`, `journal`) are filled with safe defaults.

2. **Clean and prepare the data**
   - Converts the `publish_time` column to a proper date format.
   - Extracts the **year** from the publication date for time-based analysis.
   - Computes **abstract word count** to provide simple text statistics.

3. **Analysis tasks**
   - Count publications by year.
   - Identify the top journals publishing COVID-19 papers.
   - Compute word frequency from paper titles (if using `analysis.py`).

4. **Visualizations**
   - 📈 Bar chart of publications over time.
   - 📊 Bar chart of top publishing journals.
   - 📝 Data sample preview.

---

## 📂 Dataset placement

⚠️ The full dataset is very large, so it is **not included in this repository**.  
You must download it yourself:

1. Go to the Kaggle dataset:  
   👉 [CORD-19 research challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

2. Download the file:  
```

metadata.csv

```

3. Place it in the following folder structure inside this project:
```

project-root/
├── data/
│   └── metadata.csv   <-- put the file here
├── app.py
├── analysis.py
└── README.md

---

## ⚙️ Setup instructions

1. Clone this repository:
```bash
git clone https://github.com/Oliver-Kaka/week8-python-assignment.git
cd week8-python-assignment
````

2. Create a virtual environment (recommended) and install dependencies:

   ```bash
   python -m venv venv
   # Activate environment
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

   pip install -r requirements.txt
   ```

   Or manually install:

   ```bash
   pip install pandas matplotlib seaborn streamlit
   ```

---

## 🚀 Running the Streamlit app

1. Make sure `metadata.csv` is in the `data/` folder.
2. Run the app:

   ```bash
   streamlit run src/app.py
   ```
3. Open the provided **local URL** (usually `http://localhost:8501/`) in your browser.

---

## 🖥️ How the Streamlit app works

* **Sidebar controls**

  * Year range slider → filter publications by year.
  * Journal selector → view results for all journals or one specific journal.
  * Top-N slider → choose how many top journals to display.

* **Main sections**

  1. **Summary cards** → total papers, unique journals, average abstract length.
  2. **Publications by year** → bar chart showing growth over time.
  3. **Top journals** → horizontal bar chart of the most prolific journals.
  4. **Data sample** → table showing a preview of papers with title, journal, date, and abstract.

---

## 📊 Example use cases

* Track publication growth across different years.
* Compare the most active journals in COVID-19 research.
* Quickly preview abstracts for exploratory analysis.

---

## ✅ Requirements

* Python 3.7+
* Packages: `pandas`, `matplotlib`, `seaborn`, `streamlit`

---

## 📌 Notes

* If `metadata.csv` is too large for your system, try sampling rows:

  ```python
  df = pd.read_csv('data/metadata.csv', nrows=50000)
  ```
* All cleaning and analysis logic is in `src/analysis.py`.
* The app itself is in `src/app.py`.
