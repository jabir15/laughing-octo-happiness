import sys
import os
import random

EXAM_NAME_VARS_ALPH = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
EXAM_NAME_VARS_NUMB = ['1','2','3','4','5','6','7','8','9']

sets = int(input("How many quiz sets required: "))
exam_name_base = input("Quiz name: ")
exam_name_var = input("Sets differentiated via (a)lphabets[a,b,c] or (n)umber[1,2,3]: ")


exam_name = os.path.join(os.getcwd(),'exams',sys.argv[1]+'.tex')
subject = os.path.join(os.getcwd(),sys.argv[2])
questions = []

for topic, number in zip(sys.argv[3::2],map(int,sys.argv[4::2])):
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