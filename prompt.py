import crawler
from groq import Groq



def get_answer(client: Groq, question: str) -> str:

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Nós vamos fazer exercícios em python"
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": question,
            }
        ],
        # The language model which will generate the completion.
        model="llama3-8b-8192", temperature=0.5, max_tokens=1024, top_p=1, stop=None, stream=False
    )

    # returns the answer from the AI
    return chat_completion.choices[0].message.content



def solve(debug=True):

    client_api = Groq(api_key="put your api keys here")

    for numero_lista in range(1,4):

        # get the questions from every pdf list
        questions = crawler.run(f'lista{numero_lista}.pdf')

        # context to be put into the AI prompt
        prefix = 'Me dê apenas o código, sem comentários nem nenhum outro texto desta questão: '

        numero_ex = 1
        for quest in questions:
            # requesting the prompt's response to the AI
            solved = f'{ get_answer(client_api, f"{prefix}{quest}") }\n\n'
            solved = solved.replace('`', '')
            # debugging the ongoing progress
            if debug:
                print(f' - question {numero_lista}-{numero_ex} done XD')

            # dumping the response into a py script file with the list-exercise in the filename
            open(f'exercises\\{numero_lista}-{numero_ex}.py', 'w', encoding='utf-8').write(solved)
            numero_ex+=1



if __name__ == '__main__':
    solve()
