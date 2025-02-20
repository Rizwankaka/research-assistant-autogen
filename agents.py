import os
from autogen import AssistantAgent, config_list_from_json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResearchAgents:
    def __init__(self, api_key):
        self.groq_api_key = api_key
        # Configure for Groq specifically
        self.llm_config = {
            'config_list': [{
                'model': 'mixtral-8x7b-32768',
                'api_key': self.groq_api_key,
                'base_url': "https://api.groq.com/openai/v1",  # Updated base URL
                'api_type': "openai"  # Changed to openai type
            }],
            'cache_seed': None,
            'temperature': 0.7
        }

        # Summarizer Agent - Summarizes research papers
        self.summarizer_agent = AssistantAgent(
            name="summarizer_agent",
            system_message="Summarize the retrieved research papers and present concise summaries to the user, JUST GIVE THE RELEVANT SUMMARIES OF THE RESEARCH PAPER AND NOT YOUR THOUGHT PROCESS.",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

        # Advantages and Disadvantages Agent - Analyzes pros and cons
        self.advantages_disadvantages_agent = AssistantAgent(
            name="advantages_disadvantages_agent",
            system_message="Analyze the summaries of the research papers and provide a list of advantages and disadvantages for each paper in a pointwise format. JUST GIVE THE ADVANTAGES AND DISADVANTAGES, NOT YOUR THOUGHT PROCESS",
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )

    def get_response_content(self, response):
        """Helper method to extract content from response regardless of type"""
        if isinstance(response, dict):
            return response.get("content", "")
        elif isinstance(response, str):
            return response
        return "Error: Unexpected response format"

    def summarize_paper(self, paper_summary):
        """Generates a summary of the research paper."""
        try:
            summary_response = self.summarizer_agent.generate_reply(
                messages=[{"role": "user", "content": f"Summarize this paper: {paper_summary}"}]
            )
            return self.get_response_content(summary_response)
        except Exception as e:
            print(f"Error in summarize_paper: {str(e)}")
            return "Error generating summary"

    def analyze_advantages_disadvantages(self, summary):
        """Generates advantages and disadvantages of the research paper."""
        try:
            adv_dis_response = self.advantages_disadvantages_agent.generate_reply(
                messages=[{"role": "user", "content": f"Provide advantages and disadvantages for this paper: {summary}"}]
            )
            return self.get_response_content(adv_dis_response)
        except Exception as e:
            print(f"Error in analyze_advantages_disadvantages: {str(e)}")
            return "Error analyzing advantages and disadvantages"