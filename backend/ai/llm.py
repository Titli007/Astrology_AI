from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

class LLMProcessor:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

    def chatProcess(self, prompt):
        result = self.llm.invoke(prompt)
        print(result.content)

        return result.content
    
def generate_response(user_message):
    prompt = f'''
        When will I get married?
        Is my partner compatible with me?
        Do we have Manglik Dosha in our charts?
        What are the favorable timings for my wedding?
        Will my marriage be arranged or love?
        Are there any negative influences on my marriage?
        Is my partner's Nakshatra compatible with mine?
        How many Poruthams do we match?
        Will I marry someone from a different culture or country?
        Are there any Yogas influencing my married life?
        When will I get a job?
        Will I succeed in my current job?
        What is my financial future?
        Should I start a new business?
        Which profession suits me the best?
        Will I face financial problems in the future?
        How can I improve my wealth and success?
        Will I gain money through inheritance?
        Are there obstacles in my career growth?
        Is this year favorable for investments?
        Will I face any major health issues?
        How can I maintain good health?
        Are there any doshas affecting my health?
        What are the favorable timings for surgeries?
        Will my health improve this year?
        What remedies can improve my health?
        Are there any Yogas related to my health?
        How will the planetary positions affect my health?
        When will I have children?
        How many children will I have?
        Will I face issues in family harmony?
        Are there any doshas affecting my family?
        Will I succeed in higher education?
        What is the best field of study for me?
        Will I get a scholarship or funding?
        Should I study abroad?
        Will I travel abroad this year?
        Are there any doshas preventing travel?
        Is this year favorable for relocation?
        What should I focus on today?
        Is today favorable for new beginnings?
        Will I have good luck today?
        How will my love life be today?
        Are there any inauspicious timings today?
        What are my spiritual strengths?
        Will I achieve peace of mind through meditation?
        Are there any Yogas favoring spiritual growth?
        Will I face legal issues in the future?
        How will planetary transits affect my year?
        What are my lucky directions?
        What are my lucky colors and stones?
        Is this year favorable for starting a new business?
        Will my business succeed in the future?
        What type of business is best for me?
        Should I enter into a partnership?
        Are there any financial risks in my business?
        When should I expand my business?
        Is foreign trade beneficial for me?
        Are there any planetary influences on my business?
        Should I invest in the stock market this year?
        Are there any obstacles in my business growth?
        How can I overcome challenges in business?
        Will I achieve financial stability?
        What are my wealth-building opportunities?
        Should I buy property or land this year?
        Are there any Yogas for sudden financial gains?
        How will planetary transits affect my wealth?
        Will I inherit any property or assets?
        What is the right time to start a new course?
        Will I clear my competitive exams?
        What skills should I focus on?
        Should I invest in real estate this year?
        Is this a good time to sell my property?
        Will I face legal disputes regarding property?
        Are there remedies for my health issues?
        How can I ensure good health for my family?
        How will my relationship with my siblings evolve?
        Are there any disputes in my family's future?
        Should I travel for business this year?
        Will I face issues during my travels?
        What are the most auspicious timings for today?
        Will I have a productive day today?
        Are there any Yogas influencing today's events?
        How can I align with my spiritual path?
        Are there favorable timings for rituals?
        Will I face any legal challenges?
        Are there remedies for legal issues?
        What is the overall prediction for this year?
        How will planetary transits affect my life?
        What are my strengths and weaknesses?
        What are my lucky colors and directions?
        What are my best days for making decisions?

        seen this question and tell me which question is closely related to this : 
        {user_message}
            '''


    obj = LLMProcessor()
    response = obj.chatProcess(prompt)
    print(response)

generate_response("hi, when my marriage will happen?")