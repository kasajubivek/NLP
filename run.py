import spacy
import pandas as pd

ner_model_path = r"Models/model-best"
ner_model = spacy.load(ner_model_path)

def extract_skills(job_description, softskills):
    doc = ner_model(job_description)
    skills = []
    seen_skills = set()  # To keep track of seen skills within the same row
    if(softskills == "false"):
        for ent in doc.ents:
            if ent.label_ == "SKILLS" and ent.text not in seen_skills:
                skills.append(ent.text)
                seen_skills.add(ent.text)  # Add the skill to seen_skills set

    else:
        for ent in doc.ents:
            if ent.label_ in ["SKILLS", "SOFT-SKILLS"] and ent.text not in seen_skills:
                skills.append(ent.text)
                seen_skills.add(ent.text)  # Add the skill to seen_skills set
    return skills


# def extract_skills(job_description):
#     doc = ner_model(job_description)
#     skills = []
#     seen_skills = set()  # To keep track of seen skills within the same row
#     for ent in doc.ents:
#         if ent.label_ == "SKILLS" and ent.text not in seen_skills:
#             skills.append(ent.text)
#             seen_skills.add(ent.text)  # Add the skill to seen_skills set
#     return skills

