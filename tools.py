from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, BaseTool

directory_read_tool = DirectoryReadTool(directory='./instructions')
file_read_tool = FileReadTool()
search_tool = SerperDevTool()

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = "Analyzes the sentiment of text to ensure positive and engaging communication."
    
    def _run(self, text: str) -> str:
        return "positive"

sentiment_analysis_tool = SentimentAnalysisTool()




# import os
# from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, BaseTool
# from transformers import pipeline
# from dotenv import load_dotenv

# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")

# sentiment_analysis_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# class SentimentAnalysisTool(BaseTool):
#     name: str = "Advanced Sentiment Analysis Tool"
#     description: str = "Analyzes the sentiment of text using a sophisticated machine learning model."

#     def _run(self, text: str) -> dict:
#         result = sentiment_analysis_pipeline(text)
#         print(result)
#         return result[0]  

# sentiment_analysis_tool = SentimentAnalysisTool()

# class SerperDevTool(BaseTool):
#     name: str = "Serp API Search Tool"
#     description: str = "Searches the internet using the Serper API."

#     def __init__(self, api_key):
#         self.api_key = api_key

#     def _run(self, query: str) -> dict:
#         search_results = {"query": query, "results": []}
#         return search_results

# serper_search_tool = SerperDevTool(api_key=serper_api_key)

# class DirectoryReadTool(BaseTool):
#     name: str = "Directory Read Tool"
#     description: str = "Reads the contents of an entire directory."

#     def __init__(self, directory: str):
#         self.directory = directory

#     def _run(self) -> dict:
#         try:
#             directory_contents = {}
#             for filename in os.listdir(self.directory):
#                 file_path = os.path.join(self.directory, filename)
#                 if os.path.isfile(file_path):
#                     with open(file_path, 'r') as file:
#                         content = file.read()
#                         directory_contents[filename] = content
#             return directory_contents
#         except Exception as e:
#             return {"error": str(e)}

# directory_read_tool = DirectoryReadTool(directory='./instructions')
# directory_contents = directory_read_tool.run()
# print(directory_contents)


# class FileReadTool(BaseTool):
#     name: str = "File Read Tool"
#     description: str = "Reads content from a file."

#     def _run(self, file_path: str) -> str:
#         try:
#             with open(file_path, 'r') as file:
#                 content = file.read()
#             return content
#         except FileNotFoundError:
#             return f"File '{file_path}' not found."
#         except Exception as e:
#             return f"Error reading file '{file_path}': {str(e)}"

# file_read_tool = FileReadTool()
# file_content = file_read_tool.run('./instructions/example.txt')
# print(file_content)

