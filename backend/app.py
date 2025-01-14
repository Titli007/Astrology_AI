# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from astrology_calculations.apis.kundli import kundli_creator
# from ai.llm import generate_response
# from astrology_calculations.utils.get_token import get_access_token

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# def first_function(person, gender, location, dob, tob):
#     kundli = kundli_creator(person, gender, location, dob, tob)
#     print("==============================",kundli)
#     return kundli

# def second_function(user_kundli, user_question):
#     response = generate_response(user_kundli, user_question)
#     return response

# def token_generator():
#     result =  get_access_token()
#     print(result)
#     return result

# @app.route('/process', methods=['POST'])
# def process_request():
#     data = request.get_json()

#     # Extract parameters for the first function
#     person = data.get('person')
#     gender = data.get('gender')
#     location = data.get('location')
#     dob = data.get('dob')
#     tob = data.get('tob')

#     set_token = token_generator()

#     if set_token == None:
#         return jsonify({"response": "Failed to get access token"})

#     # Call the first function
#     response_from_first_function = first_function(person, gender, location, dob, tob)

#     # Extract parameters for the second function
#     user_question = data.get('user_question')

#     # Call the second function
#     final_response = second_function(response_from_first_function, user_question)

#     return jsonify({"response": final_response})

# if __name__ == '__main__':
#     app.run(debug=True)



import streamlit as st
from astrology_calculations.apis.kundli import kundli_creator
from ai.llm import generate_response
from astrology_calculations.utils.get_token import get_access_token
from datetime import datetime, date


def first_function(person, gender, location, dob, tob, set_token):
    kundli = kundli_creator(person, gender, location, dob, tob, set_token)
    print("==============================", kundli)
    return kundli


def second_function(user_kundli, user_question):
    response = generate_response(user_kundli, user_question)
    return response


def token_generator():
    result = get_access_token()
    print(result)
    return result


def main():
    st.set_page_config(page_title="Astrology Query", layout="wide")
    st.title("Astrology Query Form")

    # Custom CSS for the Streamlit app
    custom_css = """
    <style>
        .heading {
            color: white; 
            font-size: 29px; 
            margin: 30px;
        }
        .title {
            color: #4CAF50; 
            font-size: 36px; 
            text-align: center; 
        }
        .query-input {
            margin: 10px 0; 
            padding: 10px; 
            font-size: 16px; 
            border: 1px solid #ccc; 
            border-radius: 5px; 
        }
        .form-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .form-input {
            margin: 10px 0; 
            padding: 12px;
            border-radius: 5px;
            border: 1px solid #ddd;
            width: 100%;
            font-size: 16px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
        .success {
            color: #4CAF50; 
        }
        .error {
            color: #f44336; 
        }
        .markdown-text {
            font-size: 18px; 
            line-height: 1.6; 
        }
        .warning {
            color: #f8d7da;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    with st.form(key='astrology_form'):
        person = st.text_input("Person Name", placeholder="Enter your name", key="person", label_visibility="visible")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
        location = st.text_input("Location", placeholder="Enter your location (e.g., Kolkata, West Bengal, India)", key="location")
        # Date input from 1900 to today
        today = datetime.today()
        dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1), max_value=today, key="dob")
        tob = st.text_input("Time of Birth", placeholder="Enter time in HH:MM:SS format", key="tob")
        user_question = st.text_input("Your Question", placeholder="Ask your astrology question", key="user_question")

        submit_button = st.form_submit_button(label="Submit", use_container_width=True)

    if submit_button:
        # Convert location to the required format
        location = location.replace(",", "+").lower()

        # Convert ToB to a string
        tob = str(tob)

        if person and gender and location and dob and tob and user_question:
            with st.spinner("Processing your request..."):
                set_token = token_generator()

                if set_token is None:
                    st.error("Failed to get access token.", icon="🚫")
                    return

                # Call the first function
                response_from_first_function = first_function(person, gender, location, dob, tob, set_token)

                # Call the second function
                final_response = second_function(response_from_first_function, user_question)

                # Display the final response
                if final_response:
                    st.success(final_response, icon="✅")
                else:
                    st.warning("No response generated. Please try again.", icon="⚠️")
        else:
            st.warning("Please fill out all fields.", icon="⚠️")


if __name__ == "__main__":
    main()
