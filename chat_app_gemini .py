
import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key='API_ACCESS_KEY')

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash-latest')


# ***for searching for a model ***
# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(f"اسم النموذج: {m.name}, الوصف: {m.description}")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to Gemini Chat! (Type 'quit' to exit)")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'ok bye':
            print("Goodbye!")
            break
        
        if user_input:
            print("\nGemini: ", end="")
            response = get_gemini_response(user_input)
            print(response)
        else:
            print("Please enter a question!")

if __name__ == "__main__":
    main()
