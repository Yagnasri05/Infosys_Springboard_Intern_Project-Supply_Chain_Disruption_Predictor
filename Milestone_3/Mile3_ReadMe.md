# Key functionalities of milestone 3:
- Predicting potential disruptions based on various risk factors.
- Automating stock updates based on the model's predictions.
- Offering insights into current inventory status.
- Logging and handling various events like stock damage, transport delays, and sales performance.

1. **Data Preprocessing**: 
   - Loads and prepares a dataset of product inventory, including features like inventory level, lead time, news sentiment, and textual risk.
   - The target variable (`Computed Risk Factor`) is used to train a predictive model.

2. **Machine Learning Model**: 
   - A **Random Forest Regressor** is trained to predict the risk factor for inventory disruption based on the following input features:
     - Inventory Level
     - Lead Time (days)
     - News Sentiment
     - Textual Risk

3. **Inventory Management**: 
   - A simulated inventory database is used to manage and track product information such as stock levels, purchases, sales, and damaged goods.

4. **Inventory Alerts**: 
   - Alerts are triggered when stock levels are below the minimum threshold or exceed the capacity.
   - Alerts for sales performance, transport delays, and stock damage are also incorporated.

5. **SQLite Database**: 
   - Stores inventory data persistently. It allows for retrieval and updating of stock levels.

6. **Interactive Interface**:
   - Real-time interactive widgets for:
     - Risk Prediction based on input features.
     - Inventory updates, including stock, damaged goods, transport delays, and sales.
     - Visualization of inventory status using a bar chart.

# Inventory Management Functions:

- `predict_risk`: Predicts the risk factor for the product based on the user input for inventory level, lead time, news sentiment, and textual risk. It assigns a risk label (High, Medium, Low).
- `update_inventory`: Updates inventory levels and generates alerts for stock levels (below minimum, above capacity).
- `log_damage`: Logs damaged stock and updates the inventory accordingly.
- `log_transport_delay`: Logs transport delays and generates warnings.
- `log_sales`: Updates sales data and generates alerts for halted or reduced sales.

## Requirements
- Python 3.11 or Google Colab
- Libraries: Pandas, sklearn, joblib, ipywidgets, matplotlib, sqlite3
  
