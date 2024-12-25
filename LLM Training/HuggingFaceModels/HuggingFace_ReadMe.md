# Data Preprocessing
- Textual data tokenized using Hugging Face's BERT, RoBERTa, and DistilBERT models.
- Numerical data normalized using MinMaxScaler for integration with textual features.
  
# Modeling
- Hugging Face Models:
  1. BERT, RoBERTa, and DistilBERT are used for classification tasks.
  2. Sentiment scores are analyzed to derive insights from textual data.
- Risk Categorization: Risk factors are classified into Low, Medium, and High categories using both textual and numerical features.
- Training Process:
  1. Models are fine-tuned for 50 epochs using AdamW optimizer and cross-entropy loss.
  2. Risk labels (Risk_Label) are derived from the Risk Factor column.
- Evaluation: Models are evaluated on test datasets using metrics like accuracy and classification reports.

# Requirements:
- Python 
- Libraries:
  1. Transformers
  2. PyTorch
  3. scikit-learn 

