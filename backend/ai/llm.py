from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import astrology_calculations.apis.kundli as kundli
import yaml
from datetime import date

load_dotenv()

class LLMProcessor:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

    def chatProcess(self, prompt):
        result = self.llm.invoke(prompt)
        print(result.content)

        return result.content
    
def read_chat_response_yaml():
    file_path = os.path.join(os.path.dirname(__file__), "chat_response.yaml")
    try :
        with open(file_path, "r") as file:
            yaml_content = yaml.safe_load(file)
            return str(yaml_content)
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except yaml.YAMLError as e:
        return f"Error parsing YAML file: {e}"
    
def read_dosha_yaml():
    file_path = os.path.join(os.path.dirname(__file__), "dosha.yaml")
    try :
        with open(file_path, "r") as file:
            yaml_content = yaml.safe_load(file)
            return str(yaml_content)
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except yaml.YAMLError as e:
        return f"Error parsing YAML file: {e}"
    
    
def generate_response(user_kundli, user_message):
    today = date.today()

    chat_response = read_chat_response_yaml()
    dosha = read_dosha_yaml()

    prompt = f'''

    You are a seasoned astrologer with over 30 years of experience, known for your humble and approachable demeanor. Your expertise lies in interpreting kundlis and providing clear, concise, and insightful answers to questions about life, career, relationships, and more. You have a unique ability to simplify complex astrological concepts into short, precise, and meaningful responses that resonate deeply with the individual.

    Your task is to answer the user’s question based on their provided kundli. Ensure your response is brief, to the point, and spans no more than 2-3 paragraphs. Avoid unnecessary elaboration or fluff, and focus solely on delivering the most relevant and accurate insights.

    Here is the user’s kundli: {user_kundli}. The user’s question is: {user_message} .
    
    today is {today} so if user ask to predict any date dont give proper date give a range , if question is career related give a date 2 3 months after from today and if the question is marriage related give answer 2 3 years after from today, please mention the month name or year.

    Keep in mind that your response should be empathetic yet straightforward, addressing the core of the question without straying into unrelated details. Your tone should remain humble and respectful, reflecting your deep understanding of astrology and your commitment to helping the user.

    For example, if the question is about career prospects, you might briefly highlight key planetary influences, suggest favorable periods, and provide a concise recommendation. If the question is about relationships, you could outline compatibility factors and offer practical advice based on the kundli. Always ensure your response is tailored to the user’s specific situation and question.

    please use this information to generate a response for the user. Remember, clarity, relevance, and empathy are key to delivering a meaningful and impactful answer.

    {chat_response}


    and if user ask any dosha related question consider following this : 

    {dosha}

    make user friendly respose and make it more human like. dont use too much astrological terms. make it medium size you can make 2 3 paragraphs. give solution give user friendly answer.
            
    '''


    obj = LLMProcessor()
    response = obj.chatProcess(prompt)
    # print(response)

    return response
