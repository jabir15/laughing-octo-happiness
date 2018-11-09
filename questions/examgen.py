import sys
import os
import random
import re
import subprocess

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
if remaining<0:
    print('Error: Too many arguments. Please give a maximum of {} options'.format(len(units)))
else:
    for _ in range(remaining):
        q.append('1')
    print(list(zip(units,map(int,q))))
    sets = int(input("How many quiz sets required: "))
    exam_name_base = subject.upper()+'_Quiz'
    exam_name_var = input("Sets differentiated via (a)lphabets[a,b,c] or (n)umber[1,2,3]: ")
    if exam_name_var=='a':
        set_diff = EXAM_NAME_VARS_ALPH
    elif exam_name_var=='n':
        set_diff = EXAM_NAME_VARS_NUMB
    else:
        set_diff = EXAM_NAME_VARS_ALPH
        
    for x in range(sets):
        
        exam_file = exam_name_base+'_'+set_diff[x]
        exam_file_name = exam_file+'.tex'

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

        os.chdir(os.path.join(CWD,'exams'))
        args_quiz = "\\gdef\\setvar{{{}}}\\gdef\\condition{{{}}}\\gdef\\questionbank{{{}}}\\input base".format(set_diff[x].upper(),0,exam_file)
        cmd_quiz = ['pdflatex', '-jobname', os.path.join('quiz',exam_file),'-interaction','batchmode',args_quiz]
        args_solution = "\\gdef\\setvar{{{}}}\\gdef\\condition{{{}}}\\gdef\\questionbank{{{}}}\\input base".format(set_diff[x].upper(),1,exam_file)
        cmd_solution = ['pdflatex', '-jobname', os.path.join('solution',exam_file+"_solution"),'-interaction','batchmode',args_solution]
        proc = subprocess.call(cmd_quiz)
        proc = subprocess.call(cmd_quiz)
        proc = subprocess.call(cmd_solution)
        proc = subprocess.call(cmd_solution)
        os.unlink(os.path.join(os.getcwd(),'quiz',exam_file+".log"))
        os.unlink(os.path.join(os.getcwd(),'quiz',exam_file+".aux"))
        os.unlink(os.path.join(os.getcwd(),'solution',exam_file+"_solution.log"))
        os.unlink(os.path.join(os.getcwd(),'solution',exam_file+"_solution.aux"))
        os.chdir(CWD)
