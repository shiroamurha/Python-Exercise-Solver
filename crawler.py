from PyPDF2 import PdfReader as pdf



def get_text(reader: pdf) -> str:

    ## get the all thee text from the pdf's pages
    text = str()

    for page in reader.pages:
        text += page.extract_text()
    
    return text


def extract_tasks(text, reader: pdf) -> list[str]:

    tasks = []
    task_indexes = [0]
    
    ## text junk to pop out
    header = 'INSTITUTO FEDERAL DO RIO GRANDE DO SUL Professor: Ricardo Luis dos Santos'
    footer =  "\nBaseado no material gentilmente cedido pela professora Mônica Py"

    text = text.replace(header, '')
    text = text.replace(footer, '')
    text = text.replace('\nQ', '')

    ## deleting all 'pagina x' ocurrencies 
    for page in range(1, len(reader.pages)+1):
        text = text.replace(f'Página {page} ', '')

    ## getting start and end index of every question into task_indexes 
    for i in range(len(text)):
        try:
            temp_index = text.index('Questão ', i)
            if temp_index != task_indexes[-1]:
                task_indexes.append(temp_index)
        except ValueError:
            task_indexes.append(len(text)-1)
            break

    ## subtracting the first segment of the pdf from the indexes
    ## due to its posterior deletion
    for i in range(2, len(task_indexes)):
        task_indexes[i] -= task_indexes[1]
    
    ## here deleting the first segment of the pdf before the first question
    text = list(text)
    del text[task_indexes[0]:task_indexes[1]]
    text = str().join(text)
    del task_indexes[1]

    ## deleting random Q's that appear from pdf conversion
    ## to string errors
    for i in range(len(task_indexes)):
        try:
            tasks.append(text[task_indexes[i]:task_indexes[i+1]+1])
            tasks[-1] = tasks[-1].replace(' Q', '')
        except IndexError:
            break

    #open('test.txt', 'w', encoding='utf-8').write(str('\n').join(tasks))
    return tasks

def run(filename) -> list[str]:

    ## runs all the functions altogheter

    reader = pdf(filename)
    text = get_text(reader)

    return extract_tasks(text, reader)

#run('lista3.pdf')

