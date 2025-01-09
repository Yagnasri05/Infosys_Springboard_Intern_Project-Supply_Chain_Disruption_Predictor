* **Data Collection:** Extract semiconductor-specific supply chain data from global sources using the Event Registry API.  
* **Risk Factorization:** Analyze textual and numerical data to compute dynamic risk factors and categorize them as High, Medium, or Low.  
* **Summarization:** Provide detailed summarization of textual insights and numerical trends, including interactive querying capabilities.

## **Data Sources and Datasets:**

1. **Collected Data:** Extracted from the Event Registry API focusing on semiconductors.  
   * URL: https://docs.google.com/spreadsheets/d/1R7zOBjhOKyHyeB1cD9MoGmr28zQtW2EmgLqkRB9nqdE/edit?usp=sharing
   * Columns: `Keyword`, `Title`, `Source`, `URL`, `Summary`, `Location`, `Delays`, `Reason`, `Duration`  
2. **Risk Factorized Data (Textual Only):**  
   * URL: https://docs.google.com/spreadsheets/d/1o392c3ELatpuU5CeqViLvN-qpYh_XqaDi2J1qemV-C8/edit?usp=sharing  
   * Adds `Textual Risk` and `Risk Label`.  
3. **Merged Product Data:**  
   * URL: https://docs.google.com/spreadsheets/d/1rjisc2vbaXogklmNAB_5QaO9v8FoHP4EOoOZvLdK9MY/edit?usp=sharing 
   * Combines numerical data (`Inventory Level`, `Lead Time`, etc.) with textual insights.  
4. **Final Risk Factorized Dataset:**  
   * URL: https://docs.google.com/spreadsheets/d/1R7zOBjhOKyHyeB1cD9MoGmr28zQtW2EmgLqkRB9nqdE/edit?usp=sharing
   * Combines computed risk factors with dynamic thresholds and risk labels.

### **Risk Factorization:**

1. **Sentiment Analysis:**  
   * Leverages Hugging Face's `distilbert-base-uncased` for sentiment scoring of summaries.  
   * Scores are transformed into a `Textual Risk` metric.  
2. **Risk Factor Computation:**  
   * Combines normalized numerical data (`Inventory Level`, `Lead Time`, etc.) with `Textual Risk`.  
   * Risk factor equation:  
     `Computed Risk Factor = 0.5 * Textual Risk + 0.2 * Inventory Level + 0.2 * Lead Time + 0.1 * News Sentiment`  
3. **Dynamic Thresholds:**  
   * Risk levels (Low, Medium, High) are determined dynamically using the min-max range of computed risk factors.  
4. **Risk Label Assignment:**  
   * **Low:** Below the lower threshold.  
   * **Medium:** Between lower and upper thresholds.  
   * **High:** Above the upper threshold.

### **Summarization:**

* **Numerical Insights:** Supports queries for average, minimum, and maximum values of numerical columns.  
* **Textual Insights:** Uses TF-IDF to extract top terms by importance for quick summarization of trends.

## **Outputs:**

1. **Textual Risk Factorization:**  
   * Thresholds dynamically calculated based on data range.  
   * Risk labels assigned (High, Medium, Low).  
2. **Query-Based Summarization:**  
   * Provides aggregate statistics for numerical fields like risk factors and lead times.  
   * Outputs top TF-IDF terms for textual insights.  
3. **Final Dataset:**  
   * Combines insights into a single structured CSV for reporting and downstream analysis.

## **Requirements**

* Pandas, requests, spacy, transformers, scikit-learn, numpy

