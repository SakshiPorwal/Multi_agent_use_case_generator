import streamlit as st
from googlesearch import search
import pandas as pd

def research_industry(company_name):
    """Fetch industry and company information using Google Search."""
    query = f"Industry and offerings of {company_name}"
    results = list(search(query, num_results=5))
    detailed_info = "\n".join([f"- {url}" for url in results])
    return detailed_info

def analyze_trends(industry_name):
    """Analyze AI trends in the given industry."""
    query = f"AI and ML trends in {industry_name} industry 2024"
    results = list(search(query, num_results=5))
    detailed_trends = "\n".join([f"- {url}" for url in results])
    return detailed_trends

def generate_use_cases(industry_name, key_focus_areas):
    """Generate relevant use cases for the company."""
    use_cases = [
        {
            "Use Case": "Supply Chain Optimization",
            "Description": f"To enhance demand forecasting, inventory management, and logistics, reducing costs and waste while improving cash flow, product availability, and delivery speed in {industry_name}.",
            "References": [
                "https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company",
                "https://www.kaggle.com/code/kelvinpratama/supply-chain-optimization",
                "https://github.com/samirsaci/supply-chain-optimization"
            ]
        },
        {
            "Use Case": "Predictive Maintenance",
            "Description": f"To predict equipment failures, reducing unplanned downtime and optimizing maintenance scheduling in {industry_name}. It extends equipment lifespan, increases production time, and lowers costs.",
            "References": [
                "https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification",
                "https://github.com/Yi-Chen-Lin2019/Predictive-maintenance-with-machine-learning"
            ]
        },
        {
            "Use Case": "Workforce Training and Support",
            "Description": f"Provides personalized training and real-time guidance, reducing errors, improving productivity, and speeding up onboarding while lowering employee turnover in {industry_name}.",
            "References": [
                "https://www.kaggle.com/code/nafisur/predictive-maintenance-using-lstm-on-sensor-data"
            ]
        }
    ]
    return use_cases

def create_dataframe(use_cases):
    """Converts use case data into a DataFrame."""
    data = []
    for case in use_cases:
        for ref in case["References"]:
            data.append({
                "Use Case": case["Use Case"],
                "Description": case["Description"],
                "Reference": ref
            })
    return pd.DataFrame(data)

def main():
    st.title("Enhanced AI Use Case Generator")

    st.sidebar.header("Configuration")
    company_name = st.sidebar.text_input("Enter the Company Name:")
    industry_name = st.sidebar.text_input("Enter the Industry Name:", value="General")
    focus_customer_experience = st.sidebar.text_input("Customer Experience Focus Area:", value="enhancement")
    focus_operations = st.sidebar.text_input("Operations Focus Area:", value="efficiency")

    key_focus_areas = {
        "customer_experience": focus_customer_experience,
        "operations": focus_operations
    }

    if st.sidebar.button("Generate Proposal"):
        with st.spinner("Gathering data and generating proposal..."):
            industry_info = research_industry(company_name)
            trends = analyze_trends(industry_name)
            use_cases = generate_use_cases(industry_name, key_focus_areas)
            df = create_dataframe(use_cases)
            st.success("Proposal generated successfully!")
            st.markdown("### Generated Use Cases")
            st.dataframe(df)
            csv = df.to_csv(index=False)
            st.download_button("Download Use Cases as CSV", csv, "use_cases.csv", "text/csv")

if __name__ == "__main__":
    main()
