import pandas as pd
import streamlit as st

# Load the CSV file
csv_file_path = "C:/Users/HP/OneDrive/Desktop/Weather/judgments.csv"  # Update this path with your CSV file location
df = pd.read_csv(csv_file_path)

# Set page title and layout
st.set_page_config(page_title="Court Judgment Chatbot", layout="wide")
st.title("🗂️ Court Judgment Chatbot")
st.write("Welcome to the Court Judgment Chatbot! Ask about a court case using the case number, petitioner, or respondent.")

# User input
query = st.text_input("🔍 Enter your query about a court case:")

# Debugging line
st.write("User query:", query)

if query:
    # Search for relevant cases based on the query
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    
    # Display number of results found
    st.write("📝 **Number of results found:**", results.shape[0])

    # Display results in a chatbot-like format
    if not results.empty:
        st.write("### 🗃️ Results:")
        for index, row in results.iterrows():
            # Card-style output for each case
            with st.container():
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; margin: 10px 0;">
                        <h5>**Case No:** {row['case_no']}</h5>
                        <p>**Petitioner:** {row['pet']}</p>
                        <p>**Respondent:** {row['res']}</p>
                        <p>**Judgment By:** {row['judgement_by'] if pd.notna(row['judgement_by']) else 'Not Available'}</p>
                        <p>**Judgment Date:** {row['judgment_dates']}</p>
                        <p>**Language:** {row['language'] if pd.notna(row['language']) else 'Not Available'}</p>
                        <p><a href="{row['temp_link']}" target="_blank" rel="noopener noreferrer">📥 Download PDF</a></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.write("---")
    else:
        st.write("🚫 No results found. Please try a different query.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)  # Optional: Adds a horizontal line above the footer
st.markdown("<p style='text-align: center;'>Developed By:-  Om Sonawane</p>", unsafe_allow_html=True)
