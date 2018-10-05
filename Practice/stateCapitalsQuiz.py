import os,random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNumber in range(35):
    quizFile = open('capitalQuiz%s.txt' % (quizNumber+1),'w')
    answerKeyFile = open('capitalQuizAnswerSheet%s.txt' % (quizNumber+1),'w')
    
    #Write the header of the file
    quizFile.write('Name:\n\nDate:\n\nPeriod\n\n')
    quizFile.write((' '*20)+'State Capitals Quiz (Form %s)' % (quizNumber+1))
    
    states = list(capitals.keys())
    random.shuffle(states)
    
    for questionNumber in range(len(states)):
        correctAnswer = capitals[states[questionNumber]]
        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        quizFile.write('\n\n\n%s. What is the capital of %s?' % (questionNumber+1,states[questionNumber]))
        
        answerOptionsSequence = ['A','B','C','D']
        for optionNumber in answerOptionsSequence:
            quizFile.write('\n%s. %s' % (optionNumber,answerOptions[answerOptionsSequence.index(optionNumber)]))
            
        answerKeyString = str(questionNumber+1) + '. ' + answerOptionsSequence[answerOptions.index(correctAnswer)]
        answerKeyFile.write(answerKeyString + '\n')
        
        
readQuizFile = open('capitalQuiz1.txt','r')
quizText = readQuizFile.read()
print(quizText)
print('\n\n\n\n\n\n')
readAnswerFile = open('capitalQuizAnswerSheet1.txt','r')
answerText = readAnswerFile.read()
print(answerText)
