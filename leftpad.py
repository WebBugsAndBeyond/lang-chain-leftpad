from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    template = """
    Format the string '{string}' with {count} instances of the '{char}' character prepended.
    Output only the formatted string.
    """
    prompt_template = PromptTemplate.from_template(template)

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.7,
        google_api_key=gemini_api_key,
    )
    str_parser = StrOutputParser()
    chain = prompt_template | llm | str_parser
    string_to_pad = input("Enter a string to pad: ")
    pad_char = input("Enter a character to pad with: ")
    char_count = input("How many characters to pad with: ")
    try:
        char_count = int(char_count)
    except ValueError:
        print("Invalid character count")
        exit(1)
    response = chain.invoke({
        "string": string_to_pad,
        "count": char_count,
        "char": pad_char,
    })
    print(response)

