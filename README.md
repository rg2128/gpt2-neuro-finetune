# 🧠 GPT2-Neuro Semantic Search

A simple app to semantically search neuroscience papers for topics like "mitral cells and learning" using sentence embeddings.

## Features
- Semantic paragraph search using `sentence-transformers`
- Streamlit app UI
- Precomputed paragraph embeddings + source mapping

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Launch the app:
```bash
streamlit run app/app.py
```

## File Structure

```
.
├── app/
│   └── app.py
├── data/
│   ├── paragraph_data.csv
│   └── paragraph_embeddings.npy
├── scripts/
│   └── search_embed.py
├── requirements.txt
└── README.md
```
