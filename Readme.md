A Streamlit app that uses a local Ollama LLM to analyze health insurance packages from any company, based on your personal requirements and a detailed checklist.  
Get a point-wise analysis and a clear recommendation on whether to buy a specific health insurance plan.

---

## Features

- Enter health insurance company and package/plan name
- Specify analysis date range
- Fill in your age, coverage, pre-existing conditions, family/individual, hospital network needs, and premium budget
- Ollama analyzes 14 key policy points (sub-limit, room rent cap, co-pay, waiting periods, exclusions, etc.)
- Get a detailed, personalized recommendation

---

## Requirements

- **Python 3.8+**
- **Ollama** installed and running locally ([Download Ollama](https://ollama.com/))
- **Python packages:**  
  - streamlit  
  - requests

Install Python dependencies:
```sh
pip install --user streamlit requests
```

---

## Setup & Running the App

### 1. **Start Ollama**

Open a terminal and run:
```sh
ollama run llama3
```
*(You can use any other model you have installed.)*

### 2. **Save the App Code**

Save the provided Python script as `main.py` in a folder.

### 3. **Run the Streamlit App**

In your terminal, navigate to the folder and run:
```sh
streamlit run main.py
```

### 4. **Access the App**

- The app will open in your browser at [http://localhost:8501](http://localhost:8501).
- Fill in your details and click **"Analyze & Advise"** to get a detailed analysis.

---

## How to Access from Android

1. **Find your PC’s local IP address:**
   - On Windows, run `ipconfig` in Command Prompt and note the `IPv4 Address`.
2. **Run Streamlit to listen on all interfaces:**
   ```sh
   streamlit run main.py --server.address=0.0.0.0
   ```
3. **On your Android device:**
   - Connect to the same Wi-Fi as your PC.
   - Open a browser and go to `http://<your-pc-ip>:8501` (e.g., `http://192.168.1.5:8501`).

---

## How to Stop or Restart Ollama

### **Stop Ollama**
- If running in a terminal, press `Ctrl+C`.
- If running in the background:
  - **Windows:** Open Task Manager, find `ollama.exe`, and end the task.
  - **macOS/Linux:** Run `pkill ollama` in the terminal.

### **Restart Ollama**
- Open a terminal and run:
  ```sh
  ollama run llama3
  ```

---

## How to Stop the Streamlit App

- In the terminal where Streamlit is running, press `Ctrl+C`.

---

## Notes

- Ollama must be running for the app to generate analysis.
- The app does **not** fetch real policy data; it relies on Ollama’s LLM knowledge and your input.
- For best results, use up-to-date package/plan names and company names.

---

## License

MIT License

---

## Credits

- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)