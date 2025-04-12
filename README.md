# Indian-Job-Market-Analysis
Analyzes Indian job market trends using Python + Indian API. Fetches, processes &amp; visualizes monthly Software Engineer job postings in Bangalore (2025). Built with pandas, matplotlib, and requests.

Job Market Analysis Project
A Python project to fetch, analyze, and visualize monthly job postings for Software Engineers in Bangalore (2025) using the Indian API Jobs dataset.

✨ Features
✅ Fetches real-time job data from Indian API
✅ Processes and cleans raw JSON data
✅ Visualizes monthly trends with a colorful bar chart
✅ Shows all 12 months (even if data is missing)
✅ Professional styling with value labels and grid

Prerequisites
1. Python 3.8+
2. Libraries: requests, pandas, matplotlib, numpy
3. An API key from Indian API Market

🔑 API Key Setup
1. Visit Indian API Market(https://indianapi.in/)
2. Sign up / Log in
3. Navigate to "Jobs API" → "Subscribe"
4. Choose a plan (free tier available)
5. Copy your API Key from the dashboard

🚀 Installation & Execution
Google Colab (Recommended)
1. Open the notebook:
2. Paste the code from this project into cells.
3. Replace <api-key> with your actual key.
4. Run all cells (Runtime → Run All).

Local Machine
Clone the repo:
git clone https://github.com/yourusername/job-market-analysis.git
cd job-market-analysis

Install dependencies: pip install requests pandas matplotlib numpy

Run the script: python job_analysis.py

🛠 Customization:

Change Location/Job Title

params = {
    "location": "Delhi",          # Change city
    "title": "Data Scientist",    # Change job title
    "experience": "Entry-Level",  # Change level
    "limit": "500"                # Adjust data size
}
