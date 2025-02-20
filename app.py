import streamlit as st
from agents import ResearchAgents
from data_loader import DataLoader

# Page configuration
st.set_page_config(
    page_title="Research Assistant",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stTitle {
        font-size: 45px;
        color: #3366ff;
        margin-bottom: 20px;
    }
    .paper-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for API key
with st.sidebar:
    st.title("⚙️ Settings")
    groq_api_key = st.text_input("Enter GROQ API Key", type="password")
    st.markdown("---")
    st.markdown("""
    ### How to get GROQ API Key:
    1. Visit [Groq Cloud](https://console.groq.com)
    2. Sign up and create an account
    3. Generate API key from dashboard
    4. Copy and paste it here
    """)

# Main content
st.title("📚 Virtual Research Assistant")
st.markdown("### Your AI-Powered Research Companion")

# Initialize components if API key is provided
if groq_api_key:
    agents = ResearchAgents(groq_api_key)
    data_loader = DataLoader()

    # Search interface
    col1, col2 = st.columns([4, 1])
    with col1:
        query = st.text_input("Enter a research topic:", placeholder="e.g., quantum computing, machine learning")
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)

    if search_button and query:
        with st.spinner("🔄 Fetching and analyzing research papers..."):
            try:
                arxiv_papers = data_loader.fetch_arxiv_papers(query)

                if not arxiv_papers:
                    st.error("No papers found. Please try a different search term.")
                else:
                    processed_papers = []

                    progress_bar = st.progress(0)
                    for idx, paper in enumerate(arxiv_papers):
                        summary = agents.summarize_paper(paper['summary'])
                        adv_dis = agents.analyze_advantages_disadvantages(summary)
                        
                        processed_papers.append({
                            "title": paper["title"],
                            "link": paper["link"],
                            "summary": summary,
                            "advantages_disadvantages": adv_dis,
                        })
                        progress_bar.progress((idx + 1) / len(arxiv_papers))

                    # Display results in tabs
                    st.markdown("## 📑 Research Findings")
                    for i, paper in enumerate(processed_papers, 1):
                        with st.expander(f"📄 Paper {i}: {paper['title']}", expanded=i==1):
                            st.markdown(f"**Link:** [Open Paper]({paper['link']})")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown("### 📝 Summary")
                                st.markdown(paper['summary'])
                            with col2:
                                st.markdown("### 📊 Analysis")
                                st.markdown(paper['advantages_disadvantages'])

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
else:
    st.warning("⚠️ Please enter your GROQ API key in the sidebar to start using the application.")