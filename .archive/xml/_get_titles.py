import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


MODEL = "gpt-3.5-turbo"
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "format": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "The temperature unit to use. Infer this from the users location.",
                },
            },
            "required": ["location", "format"],
        },
    },
]

def generate_title(doc_title, section_text):
    section_text = section_text[:1000]  # Limit to first 1000 characters
    message = f"""
    We are working on a set of documents for servicing, diagnosing and maintaining a 1993 Volvo 940.
    You are helping to provide titles for sections within the documents. 
    The following section is in the document entitled: {doc_title}
    ```
    {section_text}
    ```
    suggest a one line title, do not use quotes in the title:
    """

    response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": message},
                ],
            functions=[
                {
                    "name": "set_title",
                    "description": "generates a concise title for the entry",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "text to insert as title",
                                },
                            },
                        "required": ["title", "format"],
                        },
                    }],
            temperature=0.6,
            max_tokens=60,
            )


    response_text = response.choices[0]['message']['content']
    print(response_text)
    return response_text

def get_entry_titles(json_file):
    #  with open(md_file, 'r') as file:
        #  content = file.readlines()

    book = json.load(json_file)

    new_book = {}

    for key, entry in book.items():
        
        title = generate_title(entry)
        new_book[key] = entry

        

    #  for line in content:
        #  if line.strip() == '---':
            #  title = generate_title(doc_title, section_text)
            #  new_content.append('\n## ' + title + '\n\n')
            #  new_content.append(section_text)
            #  new_content.append(line)
            #  section_text = ''  # Reset the section_text
        #  else:
            #  section_text += line

    #  with open(md_file, 'w') as file:
        #  file.writelines(new_content)

def main():
    book_json = "export/euclid-01.xml.json"
    add_section_titles(md_file)

if __name__ == "__main__":
    main()

