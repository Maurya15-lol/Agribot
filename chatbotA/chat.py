import json
from difflib import get_close_matches

print("PLease enter doubts about farming")
print("To end the chat , type goodnight\n")
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict= json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str| None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_basee: dict) -> str| None:
   for q in knowledge_basee["questions"]:
       if q["question"] == question:
           return q["answer"]

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'goodnight' or user_input.lower() == 'good night':
            break

        else:
            best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

            if best_match:
                answer: str = get_answer_for_question(best_match, knowledge_base)
                print(f'Agribot: {answer}')
            else:
                print('Agribot: I dont have an answer for that . Perhaps you could teach me? ')
                new_answer: str = input('Feed me the DATA or "skip" to skip: -->')

                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({"question": user_input,"answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Agribot: Thank you for your time')

if __name__ == '__main__':
    chat_bot()



