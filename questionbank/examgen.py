import sys
import os
import random
import re

CWD = os.getcwd()
EXAM_NAME_VARS_ALPH = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
EXAM_NAME_VARS_NUMB = ['1','2','3','4','5','6','7','8','9']

subject = input("Enter subject name: ")
units = os.listdir(os.path.join(CWD,subject))
print('{} has the following {} units with respective questions'.format(subject.upper(),len(units)))
iter_path = iter(os.walk(os.path.join(CWD,subject)))
next(iter_path)
units_questions = [len(filenames) for dirpath, dirnames, filenames in iter_path ]
print(list(zip(units,units_questions)))

qn = input('Choose how many questions from each unit (default is one): ')
q = list(filter(None,re.split('\D+',qn)))
remaining = len(units)-len(q)
try:
    if remaining<0:
        raise Exception()

    for _ in range(remaining):
        q.append('1')
    print(list(zip(units,map(int,q))))
    sets = int(input("How many quiz sets required: "))
    exam_name_base = input("Quiz name: ")
    exam_name_var = input("Sets differentiated via (a)lphabets[a,b,c] or (n)umber[1,2,3]: ")
    if exam_name_var=='a':
        set_diff = EXAM_NAME_VARS_ALPH
    elif exam_name_var=='n':
        set_diff = EXAM_NAME_VARS_NUMB
    else:
        set_diff = EXAM_NAME_VARS_ALPH
        
    for x in range(sets):
        
        exam_file_name = exam_name_base+'_'+set_diff[x]+'.tex'

        exam_name = os.path.join(os.getcwd(),'exams',exam_file_name)
        questions = []

        for topic, number in zip(units,map(int,q)):
            # List comprehension
            qfiles = [
                os.path.join(dirpath,fname)
                for dirpath, dirnames, filenames in os.walk(os.path.join(subject,topic))
                for fname in filenames
                if os.path.splitext(fname)[-1].lower() == '.tex'
            ]

            for qfile in random.sample(qfiles, number):
                with open(qfile, 'r') as qfh:
                    questions.append(qfh.read())
            

        with open(exam_name, 'w') as efh:
            for question in questions:
                print(question, file=efh)
except Exception:
    print('Error: Too many arguments. Please give a maximum of {} options'.format(len(units)))
    


