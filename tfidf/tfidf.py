import numpy as np
import pandas as pd

# Sample text data
textRaw = [ 
    "नेपाल एक सुन्दर देश हो",
    "नेपाल हिमाल विश्व प्रसिद्ध छन् हो",
    "काठमाडौ नेपाल राजधानी हो"
]

# Calculate document frequency for each term
df = {}
for doc in textRaw:
    for term in set(doc.split()):
        df[term] = df.get(term, 0) + 1

# Total number of documents
N = len(textRaw)

# Calculate IDF for each term
idf = {term: np.log(N / df[term]) for term in df}

# Calculate TF for each term in each document
tf = []
for doc in textRaw:
    term_count = {}
    for term in doc.split():
        term_count[term] = term_count.get(term, 0) + 1
    tf.append(term_count)

# Calculate TF-IDF for each term in each document
tfidf = []
for doc_tf in tf:
    doc_tfidf = {}
    for term, count in doc_tf.items():
        doc_tfidf[term] = count * idf[term]
    tfidf.append(doc_tfidf)

# Create DataFrame from TF-IDF scores
all_terms = sorted(df.keys())
tfidf_matrix = []
for doc_tfidf in tfidf:
    row = [doc_tfidf.get(term, 0) for term in all_terms]
    tfidf_matrix.append(row)

tfidf_df = pd.DataFrame(tfidf_matrix, columns=all_terms)

# Sum the TF-IDF scores for each term across all documents
dictionary = tfidf_df.sum(axis=0)

print(dictionary)
