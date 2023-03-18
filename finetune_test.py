import openai

questions = [
    'What was the name of the programming language commonly used at Cornell?',
    'What was the name of the programming language usually used at Cornell?',
    'Which programming language was commonly used at Cornell?',
]

for question in questions:
    response = openai.Completion.create(
      model="curie:ft-personal-2023-03-18-04-16-01",
      prompt=question,
      stop=["\n"],
      temperature=0
    )
    answer = response['choices'][0]['text']
    print(f'question:{question}')
    print(f'answer:{answer}')
