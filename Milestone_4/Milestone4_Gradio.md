# **Milestone 4 \- UI Using Gradio**

* Gradio is an open-source Python library that allows for creating interactive UIs for machine learning models, to demonstrate, test, and share models with non-technical stakeholders.   
* Here, gradio is used to build an interface for inventory management and risk prediction based on multiple factors, such as inventory levels, lead times, news sentiment, and textual risk, all impacting the computed risk factor. 

## **Implementation & Process Flow**

### **Steps involved in the implementation:**

1. **Data Preprocessing**:  
   * Uses a CSV file to load inventory-related data, including features like inventory levels, lead time, news sentiment, and textual risk.  
   * The dataset is then prepared for predictive modeling using the features and target variable (`Computed Risk Factor`).  
2. **Model Training**:  
   * A **RandomForestRegressor** model is trained using the features to predict the computed risk factor.  
   * After training, the model is saved to a file using **joblib** for later use.  
3. **Inventory Management**:  
   * An inventory dictionary is created with essential details like product capacity, current stock, monthly purchase, sales, and damages.  
   * Functions are implemented to handle updating the inventory, logging damages, logging transport delays, sales performance, and auto-restocking.  
4. **SQLite Database**:  
   * SQLite is used to set up a local database (`inventory.db`) for storing inventory-related data.  
5. **Gradio Interface**:  
   * Several Gradio interfaces are created to handle different inventory management tasks, such as risk prediction, inventory updates, logging damages, logging transport delays, logging sales, viewing inventory status, and auto-restocking.  
6. **Risk Prediction**:  
   * The risk factor is predicted using a trained RandomForest model, based on input values like inventory level, lead time, news sentiment, and textual risk.  
   * The risk factor is classified into different risk labels: **High**, **Medium**, and **Low**.  
7. **Alerts and Warnings**:  
   * Various conditions trigger alerts or warnings, such as low stock levels, transport delays, sales exceeding stock, and high damage percentages.  
8. **Visualization**:  
   * Includes visualizations (using **matplotlib**) for inventory status, showing current stock levels, capacity, and minimum stock levels in bar charts.

---

## **Requirements**

1. **Python Libraries**: `Gradio, Joblib, Scikit-learn, Pandas, Numpy, Ipywidgets, Sqlite3, matplotlib`  
2. **Software**:  
   * Python 3.x  
   * Google Colab (for easy deployment and access to resources)  
3. **Dataset**:  
   * A dataset (`Product_risk_factorized_data.csv`) containing inventory data such as inventory levels, lead time, news sentiment, textual risk, and computed risk factors.  
4. **Hardware**:  
   * A system capable of running Python code with necessary libraries installed or using Google Colab for easy access.

---

## **The Different Conditions for Alerts and Warnings**

The system generates alerts and warnings based on inventory conditions. These include:

1. **Low Stock Warning**:  
   * Triggered when the current stock falls below the minimum stock level.  
   * Example Alert: `"ALERT: Stock below minimum (100). Restock immediately!"`  
2. **Stock Exceeds Capacity Warning**:  
   * Triggered when the stock exceeds the maximum capacity.  
   * Example Warning: `"WARNING: Stock exceeds capacity (1000). Consider reducing stock."`  
3. **Sales vs. Inventory Warning**:  
   * Triggered when monthly sales exceed the current stock or when monthly sales are significantly lower than monthly purchase.  
   * Example Alert: `"ALERT: Sales exceed current stock! Replenish inventory."`  
   * Example Warning: `"WARNING: Sales significantly below purchase levels. Investigate demand."`  
4. **Damaged Stock Warning**:  
   * Triggered when the damaged stock exceeds 10% of the total capacity.  
   * Example Warning: `"WARNING: High damage recorded! Investigate causes."`  
5. **Transport Delay Warning**:  
   * Triggered when a transport delay is logged, potentially affecting inventory replenishment.  
   * Example Warning: `"WARNING: Transport delay may impact inventory replenishment."`

---

## **Different Sections in the System**

1. **Risk Prediction**:  
   * This section allows users to input values like inventory level, lead time, news sentiment, and textual risk, and get predicted risk factors and corresponding labels (High, Medium, Low).  
2. **Inventory Update**:  
   * Users can update the current stock of products and receive alerts or warnings based on stock conditions.  
3. **Log Damaged Stock**:  
   * This section allows logging of damaged stock and provides warnings if the damage exceeds 10% of the capacity.  
4. **Log Transport Delay**:  
   * Users can log transport delays, which could potentially impact the restocking process.  
5. **Log Sales**:  
   * Sales data can be logged, and alerts will be generated if sales exceed the current stock or fall significantly below the purchase levels.  
6. **View Inventory**:  
   * This section allows users to view the current inventory status, including current stock, capacity, and minimum stock.  
7. **Auto Restock**:  
   * The system can automatically restock products when the current stock falls below the minimum threshold, based on predefined logic.

---

* **High Risk**: Indicates that immediate attention is required, such as restocking or investigating issues.  
* **Medium Risk**: Requires monitoring and action if the situation worsens.  
* **Low Risk**: The system is in a stable state.

---

