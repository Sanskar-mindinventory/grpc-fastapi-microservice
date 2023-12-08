from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
import textract
from itertools import chain
from pyresparser import ResumeParser
import json
import string
import re
import os
from joblib import load
import pickle
import en_core_web_sm
nlp = en_core_web_sm.load()





def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)
    resumeText = re.sub('RT|cc', ' ', resumeText)
    resumeText = re.sub('#\S+', '', resumeText)
    resumeText = re.sub('@\S+', '  ', resumeText)
    resumeText = re.sub('[%s]' % re.escape(
        """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)
    resumeText = re.sub(r'[^\x00-\x7f]', r' ', resumeText)
    resumeText = re.sub('\s+', ' ', resumeText)
    return resumeText


def Preprocessfile(filename):
    skills = skill_extractor()
    text = filename
    if ".pdf" in filename:
        try:
            text = textract.process(f"/home/mind/PyCharm_projects/ML/resume_parser/files/{filename}")
        except UnicodeDecodeError:
            print('File', filename, 'cannot be extracted! - skipped')
        text = text.decode('utf-8').replace("\\n", " ")
    else:
        text = text.replace("\\n", " ")
    # x = []
    tokens = word_tokenize(text)
    tok = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    strpp = [w.translate(table) for w in tok]
    words = [word for word in strpp if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    # x.append(words)
    new_words = set([i for i in words if i in skills])
    res = " ".join(words)
    return res

def predictResume(filename):
    try:
        text = textract.process(f"/home/mind/PyCharm_projects/ML/resume_parser/files/{filename}")
        text = text.decode('utf-8').replace("\\n", " ")
        text = cleanResume(text)
        text = [text]
        text = np.array(text)
        vectorizer = pickle.load(open("src/api/v1/ResumeParser/utils/vectorizer.pickle", "rb"))
        resume = vectorizer.transform(text)
        model = load('src/api/v1/ResumeParser/utils/model.joblib')
        result = model.predict(resume)
        labeldict = {
            0: 'Arts',
            1: 'Automation Testing',
            2: 'Operations Manager',
            3: 'DotNet Developer',
            4: 'Civil Engineer',
            5: 'Data Science',
            6: 'Database',
            7: 'DevOps Engineer',
            8: 'Business Analyst',
            9: 'Health and fitness',
            10: 'HR',
            11: 'Electrical Engineering',
            12: 'Java Developer',
            13: 'Mechanical Engineer',
            14: 'Network Security Engineer',
            15: 'Blockchain ',
            16: 'Python Developer',
            17: 'Sales',
            18: 'Testing',
            19: 'Web Designing'
        }
        return labeldict[result[0]]
    except UnicodeDecodeError:
        print('File', filename, 'cannot be extracted for prediction! - skipped')

def skill_extractor():
    employee_skills_set = pd.read_csv('src/api/v1/ResumeParser/utils/employee_skills.csv')['name'].to_list()
    return set([i.lower() for i in employee_skills_set])

def find_score(jobdes, filename):
    resume = Preprocessfile(filename)
    text = [resume, jobdes]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    matchpercent = cosine_similarity(count_matrix)[0][1]*100
    matchpercent = round(matchpercent, 2)
    return matchpercent