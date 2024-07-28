import json

# Define the data structure for 3 subjects
questions_data = {
    "Engineering Chemistry": [
        {
            "Question": "What is the chemical formula of water?",
            "Year": 2021,
            "Type": "Chemistry"
        },
        {
            "Question": "Explain the pH scale.",
            "Year": 2020,
            "Type": "Chemistry"
        }
    ],
    "Engineering Physics": [
        {
            "Question": "What is the speed of light?",
            "Year": 2020,
            "Type": "Physics"
        },
        {
            "Question": "Explain Newton's second law of motion.",
            "Year": 2019,
            "Type": "Physics"
        }
    ],
    "Mathematics": [
        {
            "Question": "What is the integral of x^2?",
            "Year": 2021,
            "Type": "Mathematics"
        },
        {
            "Question": "Solve the differential equation dy/dx = 3y.",
            "Year": 2020,
            "Type": "Mathematics"
        }
    ]
}

# Define the file path where the JSON data will be saved
json_file_path = 'questions_data.json'

# Write the questions data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(questions_data, json_file, indent=4)

print(f"Data successfully written to {json_file_path}")
