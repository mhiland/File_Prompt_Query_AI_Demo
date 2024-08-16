import os
from openai import OpenAI

# Initialize the client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def ask_question(client, content, question):
    """Asks a question about the given content using the OpenAI API."""
    prompt = f"The following is a document:\n\n{content}\n\nAnswer the following question based on the document:\n{question}\n"

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )

    # Return the assistant's response
    return chat_completion.choices[0].message.content

def main():
    # Path to the text file
    file_path = "/var/log/wifi_monitor/training_data/095c5b99761e0d76dda4695ee264ee229651cddd1b8760966d8eec6590ea4b52.nd"  

    # Read the file content
    content = read_file(file_path)
    print("File content has been loaded.")

    while True:
        # Ask the user for a question
        question = input("\nWhat would you like to ask about the document? (Type 'exit' to quit): ")

        if question.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the answer from the OpenAI API
        answer = ask_question(client, content, question)

        # Display the answer
        print(f"\nAnswer: {answer}")

if __name__ == "__main__":
    main()
