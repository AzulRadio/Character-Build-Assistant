import random
import json

###
# user defined parameters 
# how many questions do you want
N = 7
# if True, print N questions for each topic (may repeated)
ALL_TOPICS = False
#
###

# all the 21 topics for world-building questions
world_topics = ['world','country','history','ethnicity','society',
                 'marriage','etiquette','food','entertainment','religion',
                 'labor','art','medicine','sex','education','science','transport',
                 'economy','funeral','government','war']

# with ... as, guarantee to release the file
with open('questions.json','r',encoding='UTF-8') as f:
    world_questions = json.loads(f.read(),strict=False)

assert type(world_questions) == dict

# write to the file
# if not exist, will create
output = open('./output_questions.txt', 'w')

# print the questions
for i in range(N):
    # if in ALL_TOPICS mode
    if ALL_TOPICS:
        # iterate all topics
        for topic in world_topics:
            topic_questions = world_questions[topic]
            # randomly select one
            question_index = random.randint(1, len(topic_questions))
            question = topic_questions[str(question_index)]
            # write to the file
            output.write(str(i + 1) + '. ' + question + '\n')
            # print to the console
            print(str(i) + '. ' + question)
            print('\n')
    else:
        # randomly select a topic
        topic_index = random.randint(0, 20)
        topic = world_topics[topic_index]
        topic_questions = world_questions[topic]
        # randomly select a question
        question_index = random.randint(1, len(topic_questions))
        question = topic_questions[str(question_index)]
        # write to the file
        output.write(str(i + 1) + '. ' + question + '\n')
        # print to the console
        print(str(i) + '. ' + question)
        print('\n')

output.close()
