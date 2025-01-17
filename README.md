# Multi-Agentic Workflow Application

## Overview
The Multi-Agentic Workflow Application is a Streamlit-based tool designed to automate the generation of AI/ML use cases for specific industries and companies. It leverages a modular, multi-agent architecture to:

- Conduct industry research.
- Analyze AI/ML market trends.
- Propose relevant AI/ML use cases.
- Provide references and resources for implementation.
- Deliver structured outputs in tabular and downloadable formats.

## Features
- **Industry Research Agent**: Gathers industry-specific insights using web search.
- **Market Trends Agent**: Analyzes AI/ML trends in the specified industry.
- **Use Case Generation Agent**: Proposes actionable AI/ML use cases tailored to the company and industry.
- **Resource Asset Agent**: Links to relevant datasets and resources.
- **Proposal Generation**: Outputs results in a structured table and downloadable CSV file.

---

## Architecture
The application employs a multi-agent architecture with the following components:

1. **Input**: Company name, industry name, and focus areas (e.g., customer experience, operations).
2. **Agents**:
   - Industry Research Agent
   - Market Trends Agent
   - Use Case Generation Agent
   - Resource Asset Agent
3. **Output**: Results displayed in a table with options to download as CSV.

Refer to the `architecture_flowchart.png` for a visual representation of the workflow.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run multi_agent_use_case_generator.py
   ```

---

## Usage

### Step 1: Input Details
- Enter the company name and industry in the sidebar.
- Specify focus areas for **customer experience** and **operations**.

### Step 2: Generate Proposal
- Click the **Generate Proposal** button.
- The app will display:
  - A table of use cases with descriptions and references.

### Step 3: Download Results
- Click **Download Use Cases as CSV** to save the results for further analysis or sharing.

---

## Example Output
### Use Cases for the Steel Industry
| Use Case                 | Description                                                                                  | Reference                                                                                     |
|--------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Supply Chain Optimization | To enhance demand forecasting, inventory management, and logistics, reducing costs and waste while improving cash flow, product availability, and delivery speed. | [Kaggle Link](https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company) |
| Predictive Maintenance    | To predict equipment failures, reducing unplanned downtime and optimizing maintenance scheduling. It extends equipment lifespan and lowers costs.                | [GitHub Link](https://github.com/Yi-Chen-Lin2019/Predictive-maintenance-with-machine-learning) |
| Workforce Training       | Provides personalized training and real-time guidance, reducing errors and improving productivity. | [Kaggle Link](https://www.kaggle.com/code/nafisur/predictive-maintenance-using-lstm-on-sensor-data) |

---

## Deliverables
1. **Source Code**: The main Python script (`multi_agent_use_case_generator.py`) and dependencies (`requirements.txt`).
2. **Flowchart**: The architecture flowchart (`architecture_flowchart.png`).
3. **Documentation**: This README file.
4. **Demo Video**: A walkthrough of the application.

---

## Future Enhancements
- Add a **Competitor Analysis Agent** to compare trends with competitors.
- Integrate APIs for real-time industry data.
- Expand dataset references to platforms like HuggingFace.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Support
For issues or suggestions, please create an issue in the repository or contact [support@example.com](mailto:support@example.com).

