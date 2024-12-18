## 📘 **Expense Tracker Program**
This is a **Python-based expense tracker** that allows users to upload and categorize their financial transactions. Users can visualize their expenses through interactive charts and apply filters to customize the display of their financial data.

---

## 📂 **Directory Structure**

### **Project Files**
- **`README.md`**: Instructions on setting up and using the application.
- **`requirements.txt`**: List of required Python libraries.

### **Application Files**
- **`expense_tracker.py`**
- **`manual_inputs.py`**
- **`statements_upload.py`**
- **`apply_filters.py`**
- **`transform_data.py`**

### **Data Files**
- **`categories.csv`**: A catalogue of common expense descriptions and their associated categories.

---

## 💻 **System Requirements**
- **Python 3.9**

---

## 🚀 **Launch Instructions**

1. **Navigate to the project directory**
   ```bash
   cd /path/to/project/directory
   ```

2. **Install the required Python libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Expense Tracker application**
   ```bash
   python -m streamlit run expense_tracker.py
   ```
   By default, the app runs on **port 8501**. To change the port, use the following command:
   ```bash
   python -m streamlit run expense_tracker.py --server.port=8080
   ```

4. **Access the application**
   Open a web browser and navigate to:
   [http://localhost:8501/](http://localhost:8501/)

---

## 📦 **Virtual Environment Setup (Optional, but Recommended)**
Running the program inside a **virtual environment** helps prevent conflicts with other Python packages installed on your system.

### **Steps to create a virtual environment**
1. **Navigate to the project directory**
   ```bash
   cd /path/to/project/directory
   ```

2. **Create a new virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. **Install the required libraries**
   ```bash
   pip install -r requirements.txt
   ```

5. **Launch the application** by following the [Launch Instructions](#launch-instructions) above.

---

## 📊 **How to Use the Program**

1. **Input Your Expenses**
   - **Manual Input**: Users can enter expenses directly through a form in the app.
   - **Upload Statements**: Upload bank statements from the featured providers (Amex, Aqua and Lloyds). The system will automatically categorize and process the data.

2. **Filter Your Data**
   - **By Date**: Filter expenses by month, year, or a combination of both.
   - **By Category**: Exclude specific expense categories to customize your view (e.g., exclude "Housing" to see other expenses).

3. **View Insights and Visualizations**
   - **Pie Chart**: View the distribution of expenses by category.
   - **Bar Chart**: Compare current, previous, and average expenses for each category.

### **Example of Visualizations**
**Output Example**: See how your spending is distributed among categories and how it varies through different periods.
![Pie Chart](https://github.com/user-attachments/assets/66465ab2-4154-4f69-bb83-f3d5d1bb61d6)

**Statement Verification Check**: Uploaded files are validated to ensure they match the expected format.
![Verification Screenshot](https://github.com/user-attachments/assets/bbc7faf9-46d1-4d46-8ee8-42394c80a6c5)

---

## ✨ **Additional Features**

1. **Automatic Statement Verification**
   - When users upload statements, the app checks the file format to ensure it matches the format required by the provider. This prevents errors and mismatched data.

2. **Comprehensive Filtering Options**
   - Filter by **month**, **year**, or **both** to get a more focused view of your expenses.

3. **Customizable Category Exclusion**
   - Users can exclude certain categories (like "housing") from visualizations to focus on specific expense types. This is useful if a large category (like rent) skews the visualizations.
