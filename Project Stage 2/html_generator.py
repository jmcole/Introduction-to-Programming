#John Cole Udacity Stage 2 Submission

def lesson_generator(Lesson_Notes):#Iterates through the notes (with calls to the notes parser) and creates the HTML document
    HTML = ''
    for lesson in Lesson_Notes:
        lesson_HTML = notes_parser(lesson)#calls notes parser to get title and description
        HTML = HTML + lesson_HTML
    HTML ='''
    <section class = "section">'''+HTML+'''#creates the HTML(non-iterator) outside the Lesson Notes
    </section>'''
    return HTML

def notes_parser(lesson):# breaks notes into title and rescription
    lesson_title = lesson[0]
    lesson_description = lesson[1]
    return html_generator(lesson_title, lesson_description)


def html_generator(lesson_title, lesson_description):#puts together the HTML(iterator) from the Lesson notes
    html_text = '''
    <div>
        <h3>'''+lesson_title+'''</h3>
        ''' +lesson_description+'''
    </div>'''
    return html_text

Lesson_Notes = [['Computer', 'A computer is a machine that can do almost anything. However, it must be given specific intructions on how to accomplish its task.'],
                ['Program', 'A program is a specific sequence of instructions that tell a compter what to do.'],
                ['Program Language', 'A program languages are used by programmers to write programs. Languages can be <em>interpreted or compiled. Python is interpreted, which means it uses a seperate program to convert the code to code the computer can understand. Compiled language, such as C++, create an executable file that does not need a compiler to break the program down so the computer can understand it.']]

print lesson_generator(Lesson_Notes)