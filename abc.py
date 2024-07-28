import json

# Define the initial data structure for the subjects
questions_data = {
    "Engineering Chemistry": [],
    "Engineering Physics": [],
    "Mathematics": []
}

# Load existing questions data from JSON file
def load_questions(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return questions_data

# Save questions data to JSON file
def save_questions(questions_data, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(questions_data, json_file, indent=4)

# Add a question to a subject
def add_question(subject, question, year, q_type, questions_data):
    new_question = {
        "Question": question,
        "Year": year,
        "Type": q_type
    }
    if subject in questions_data:
        questions_data[subject].append(new_question)
    else:
        questions_data[subject] = [new_question]

# Define the file path where the JSON data will be saved
json_file_path = 'questions_data.json'

# Load existing data
questions_data = load_questions(json_file_path)

# Example of adding multiple questions
add_question("Engineering Chemistry", "What is the chemical formula of water?", 2021, "Chemistry", questions_data)
add_question("Engineering Chemistry", "Explain the pH scale.", 2020, "Chemistry", questions_data)
add_question("Engineering Physics", "What is the speed of light?", 2020, "Physics", questions_data)
add_question("Engineering Physics", "Explain Newton's second law of motion.", 2019, "Physics", questions_data)
add_question("Mathematics", "What is the integral of x^2?", 2021, "Mathematics", questions_data)
add_question("Mathematics", "Solve the differential equation dy/dx = 3y.", 2020, "Mathematics", questions_data)

# Save updated data
save_questions(questions_data, json_file_path)

print(f"Data successfully written to {json_file_path}")
