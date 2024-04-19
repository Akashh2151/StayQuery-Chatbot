import pandas as pd
from gensim.summarization import summarize

# Read the CSV file into a DataFrame
df = pd.read_csv('/var/www/html/rms-rag-llama/samplereport.csv')

# Concatenate all text columns into a single string
text = ' '.join(df['text_column'])

# Perform text summarization
summary = summarize(text)

# Display or save the summary
print(summary)