import streamlit as st
import requests
from datetime import date

st.title("Ollama Health Insurance Advisor")

company = st.text_input("Enter Health Insurance Company Name (e.g., Max Bupa, HDFC Ergo, Star Health):")
package = st.text_input("Enter Package/Plan Name (e.g., Family Floater, Silver Plan):")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Analysis Start Date", value=date.today().replace(day=1))
with col2:
    end_date = st.date_input("Analysis End Date", value=date.today())

age = st.number_input("Your Age", min_value=0, max_value=120, value=30)
coverage = st.number_input("Desired Coverage Amount (in INR Lakhs)", min_value=1, max_value=100, value=5)
pre_existing = st.radio("Do you have any pre-existing conditions?", ("No", "Yes"))
family = st.radio("Is this for individual or family?", ("Individual", "Family"))
hospital_network = st.radio("Is a large hospital network important to you?", ("Yes", "No"))
premium_budget = st.number_input("Annual Premium Budget (in INR)", min_value=1000, value=10000)

coa_points = [
    "1. Sub Limit",
    "2. Room Rent Cap",
    "3. Co-Pay",
    "4. Waiting Period - 30 days (exclude accidents)",
    "5. Waiting Period - 90 days (maternity benefits)",
    "6. Waiting Period for Pre Existing Diseases (3-4 years)",
    "7. Waiting Period for Slow Growing Diseases (2 years)",
    "8. Restoration of Sum Assured",
    "9. Zonal/Pan India",
    "10. Exclusions",
    "11. Cashless + Reimbursement (Network & Non-network both)",
    "12. Daycare",
    "13. Continuity",
    "14. Super top up",
    "15. Incurred claims ratio ",
    "16. Complaints/1000 claims",
    "17. Disease wise sublimit"
]

if st.button("Analyze & Advise"):
    if not company or not package:
        st.warning("Please enter both the health insurance company and package/plan name.")
    else:
        # Prepare prompt for Ollama
        prompt = (
            f"User is considering buying health insurance from '{company}', package/plan '{package}'.\n"
            f"Analysis period: {start_date} to {end_date}\n"
            f"User details:\n"
            f"- Age: {age}\n"
            f"- Desired Coverage: {coverage} lakh INR\n"
            f"- Pre-existing conditions: {pre_existing}\n"
            f"- Policy type: {family}\n"
            f"- Large hospital network needed: {hospital_network}\n"
            f"- Premium budget: {premium_budget} INR/year\n\n"
            f"Analyze the policy '{package}' from '{company}' for this user and answer the following points in detail:\n"
            + "\n".join(coa_points) +
            "\n\nAfter addressing all points, give a clear recommendation on whether the user should buy insurance from this company/package or consider alternatives."
        )

        # Call Ollama
        ollama_url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(ollama_url, json=payload)
            if response.ok:
                analysis = response.json()["response"]
                st.subheader("Ollama's Detailed Analysis & Advice")
                st.write(analysis)
            else:
                st.error("Could not connect to Ollama. Is it running?")
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Enter your details and click 'Analyze & Advise' to get a detailed recommendation.")