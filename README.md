
# Astrology AI - Backend

This project contains the backend for the Astrology AI application. Follow the steps below to set up and run the application locally.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.6 or later
- Git

---

## Steps to Run the Application

### 1. Clone the Repository
Use the following command to clone the repository:
```bash
git clone https://github.com/Titli007/Astrology_AI.git
```

### 2. Navigate to the Backend Directory
```bash
cd Astrology_AI/backend
```

### 3. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
- **On Linux/Mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Install Dependencies
Install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application
Start the application using the following command:
```bash
streamlit run app.py
```

### 6. Open in Browser
Once the app starts, it will provide a local URL (usually `http://localhost:8501`). Open this URL in your browser to access the application.

---

## Notes

- Ensure you have all necessary secret keys or configuration files (e.g., `.env` or `secrets.toml`) set up as required by the application.
- For any issues, please raise an [issue](https://github.com/Titli007/Astrology_AI/issues) on the repository.

---

### License
This project is licensed under the [MIT License](LICENSE).
