import csv
import json
import os

all = {
"@attributes":
    {
        "version":"16.1.0 "
    },
"header":
    {
        "@attributes":
            {
                "lang":"en",
                "date":"2024-03-17 15:42:08"
            }
    },
"body":
    {
        "module":
            [
                {"name":"PAPER 1","enabled":"true","subject":[
                    {"name":"CHE 211","question":[],"description":"Professional Ethics","enabled":"true"},{"name":"CHE 214","question":[],"description":"Human Nutrition","enabled":"true"},{"name":"CHE 223","question":[],"description":"Clinical Skills","enabled":"true"},{"name":"CHE 225","question":[],"description":"Control of Communicable Diseases","enabled":"true"},{"name":"CHE 232","question":[],"description":"Oral Health","enabled":"true"},{"name":"CHE 235","question":[],"description":"Child Health","enabled":"true"},{"name":"CHE 238","question":[],"description":"Community Linkages and Development","enabled":"true"},{"name":"CHE 242","question":[],"description":"Maternal Health","enabled":"true"},{"name":"CHE 245","question":[],"description":"Community Eye Care","enabled":"true"},{"name":"CHE 248","question":[],"description":"Supervised Clinical Experience","enabled":"true"},{"name":"CHE 253","question":[],"description":"Health Statistics","enabled":"true"},{"name":"CHE 256","question":[],"description":"Research Methodology","enabled":"true"},{"name":"CHE 261","question":[],"description":"Primary Health Care Management","enabled":"true"},{"name":"CHE 264","question":[],"description":"Health Information Management System","enabled":"true"},{"name":"EHT 111","question":[],"description":"Introduction to Environmental Health","enabled":"true"},{"name":"GNS 213","question":[],"description":"Introduction to Medical Sociology","enabled":"true"}]},
                {"name":"PAPER 2","enabled":"true","subject":[
                    {"name":"CHE 212","question":[],"description":"Anatomy and Physiology","enabled":"true"},{"name":"CHE 215","question":[],"description":"Introduction to Primary Health Care","enabled":"true"},{"name":"CHE 221","question":[],"description":"Symptomatology","enabled":"true"},{"name":"CHE 226","question":[],"description":"Accident and Emergency","enabled":"true"},{"name":"CHE 233","question":[],"description":"Community Mental Health","enabled":"true"},{"name":"CHE 236","question":[],"description":"School Health Programme","enabled":"true"},{"name":"CHE 239","question":[],"description":"Care and Management of HIV and AIDS","enabled":"true"},{"name":"CHE 243","question":[],"description":"Modified Essential Newborn Care","enabled":"true"},{"name":"CHE 251","question":[],"description":"Care of Older Persons","enabled":"true"},{"name":"CHE 254","question":[],"description":"Essential Medicines","enabled":"true"},{"name":"CHE 257","question":[],"description":"Community Based Newborn Care","enabled":"true"},{"name":"CHE 262","question":[],"description":"Referral System and Outreach Services","enabled":"true"},{"name":"FOT 111","question":[],"description":"Geography","enabled":"true"},{"name":"GNP 123","question":[],"description":"Introduction to Pharmacology","enabled":"true"},{"name":"STB 211","question":[],"description":"Science Laboratory Technology","enabled":"true"}]},
                {"name":"PAPER 3","enabled":"true","subject":[
                    {"name":"CHE 213","question":[],"description":"Behavioural Change Communications ","enabled":"true"},{"name":"CHE 222","question":[],"description":"Population Dynamics and Family Planning","enabled":"true"},{"name":"CHE 224","question":[],"description":"Immunity and Immunization","enabled":"true"},{"name":"CHE 227","question":[],"description":"Supervised Clinical Experience","enabled":"true"},{"name":"CHE 234","question":[],"description":"Reproductive Health","enabled":"true"},{"name":"CHE 237","question":[],"description":"Control of Non-Communicable Diseases","enabled":"true"},{"name":"CHE 240","question":[],"description":"Occupational Health and Safety","enabled":"true"},{"name":"CHE 244","question":[],"description":"Community Ear, Nose and Throat Care (ENT)","enabled":"true"},{"name":"CHE 247","question":[],"description":"Nigerian Health System","enabled":"true"},{"name":"CHE 252","question":[],"description":"Care of Person with Special Needs","enabled":"true"},{"name":"CHE 255","question":[],"description":"Human Reseorce for Health","enabled":"true"},{"name":"CHE 258","question":[],"description":"Supervised Community Based Exprerience (SCBE)","enabled":"true"},{"name":"CHE 263","question":[],"description":"Accounting System in Primary Health Care","enabled":"true"},{"name":"COM 111","question":[],"description":"Introduction to Computer","enabled":"true"},{"name":"GNS 411","question":[],"description":"Introductionn to Psychology","enabled":"true"}]}
            ]
    }
}

# Define the folder path containing CSV files
folder_path = "./csv_questions"

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' does not exist.")
else:
    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    if not csv_files:
        print(f"No CSV files found in the folder '{folder_path}'.")
    else:
        # Iterate through each CSV file
        for csv_file in csv_files:
            file_parts = csv_file.split('_')
            csv_file_path = os.path.join(folder_path, csv_file)
            with open(csv_file_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    question = {
                        "enabled":"true",
                        "type":"single",
                        "difficulty":"1",
                        "position":{},
                        "timer":"0",
                        "fullscreen":"true",
                        "inline_answers":"false",
                        "auto_next":"false",
                        "question":[],"description":row[0],
                        "explanation":{},
                        "answer":
                        [
                            {
                                "enabled":"true",
                                "isright":"true",
                                "position":{},
                                "keyboard_key":{},
                                "question":[],"description":row[1],
                                "explanation":{}
                            },
                            {
                                "enabled":"true",
                                "isright":"false",
                                "position":{},
                                "keyboard_key":{},
                                "question":[],"description":row[2],
                                "explanation":{}
                                
                            }, 
                            {
                                "enabled":"true",
                                "isright":"false",
                                "position":{},
                                "keyboard_key":{},
                                "question":[],"description":row[3],
                                "explanation":{}
                            },
                            {
                                "enabled":"true",
                                "isright":"false",
                                "position":{},
                                "keyboard_key":{},
                                "question":[],"description":row[4],
                                "explanation":{}
                            }
                        ]
                    }
                    index = 0
                    for module in all['body']['module']:
                        if module['name'] == file_parts[0]:
                            index2 = 0
                            for subject in all['body']['module'][index]['subject']:
                                if subject['name'] == file_parts[1]:
                                    print(subject['name'])
                                    all['body']['module'][index]['subject'][index2]['question'].append(question)
                                index2+=1
                            index+=1
        with open('questions.json', 'w') as jsonfile:
            json.dump(all, jsonfile, indent=4)



