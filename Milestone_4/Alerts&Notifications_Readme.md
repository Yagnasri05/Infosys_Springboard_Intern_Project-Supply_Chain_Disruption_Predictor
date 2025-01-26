# **Milestone 4 \- Slack Integration**

Slack notifications are integrated to send alerts based on critical situations like high risk, low stock, or delays.

* **Risk Prediction**: The system predicts risk levels based on inventory factors, lead time, news sentiment, and textual risk factors.  
* **Slack Alerts**: Notifications are sent to a Slack channel for various events, such as:  
  * High risk predictions  
  * Inventory issues (low stock, damaged goods)  
  * Transport delays  
  * Restocking alerts

## **Requirements**

1. **Python Libraries**: `Gradio, Joblib, Scikit-learn, Pandas, Numpy, Ipywidgets, Sqlite3, matplotlib, slack-sdk`  
2. **Software**:  
   * Python 3.11
   * Google Colab (for easy deployment and access to resources)  
3. **Dataset**:  
   * A dataset (`Product_risk_factorized_data.csv`) containing inventory data such as inventory levels, lead time, news sentiment, textual risk, and computed risk factors.

## **Setup Instructions:**

### **1\. Obtain a Slack Webhook URL:**

* Navigate to the Slack workspace and set up an incoming webhook by following these steps:  
  1. Create a new app from scratch for a workspace.  
  2. Visit Slack Incoming Webhooks.  
  3. Click **Create New Webhook** and select the channel where the alerts have to be received.  
  4. Copy the **Webhook URL** provided.

### **2\. Configure Slack Webhook URL in Code:**

* Locate the variable `SLACK_WEBHOOK_URL` in the code and replace the placeholder with the actual Webhook URL.  
* The slack webhook url used in the given code is: `SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'`

### **Process Flow:**

1. **Risk Prediction**: The system uses historical data and factors such as lead time, sales, and news sentiment to predict the risk of stock shortages. If the predicted risk level exceeds a threshold (e.g., 0.6), a warning message is sent to Slack.  
2. **Inventory Monitoring**: The system monitors the inventory levels in real-time. If any stock is below minimum levels or exceeds capacity, the system triggers a Slack message to notify the team to take action.  
3. **Sales Performance**: If sales for a product drop below a predefined threshold, the system generates a Slack notification to alert the team of potential sales issues.  
4. **Transport Monitoring**: The system checks transport statuses and sends alerts if any delays are expected to impact the inventory levels, with notifications sent to Slack to warn the team.  
5. **Restocking**: When stock levels fall below predefined minimum levels, the system will automatically place a restocking order and send a confirmation notification to Slack.

