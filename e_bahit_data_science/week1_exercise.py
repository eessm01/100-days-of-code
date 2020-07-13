"""Se trata del tema «What is Data Science?» del capítulo de un libro sobre Data Science, de un autor ruso.

En el archivo, está toda la información sobre el libro:
Nombre del libro, editorial, autor, el número y nombre del capítulo de este texto en concreto, el ISBN, etc.
La idea no es escribir código fuente, sino ANALIZAR, qué métodos y/o funciones utilizaríamos para alcanzar los objetivos propuestos.

OBJETIVOS:
1) Obtener los datos (sin análisis)
2) Obtener el nombre del libro
3) Obtener el nombre del autor
4) Obtener el número del capítulo y el nombre del capítulo por separado
5) Obtener la cantidad de apariciones de los términos "data science", en el texto
6) Obtener el nombre de los 8 temas que, según este texto, son tratados en el libro y conciernen a la ciencia de datos
"""

count = 0

with open('what-is-data-science.txt', 'r') as f:
    for line in f:
        if line.startswith('Book'):
            book = line.lstrip('Book: ')
            print(book)
        if line.startswith('Author'):
            author = line.lstrip('Author: ')
            print(author)
        if line.startswith('Chapter'):
            num, chapter_name = line.lstrip('Chapter: ').split('. ')
            print(num)
            print(chapter_name)
        if line.startswith('• '):
            print(line)
        times = line.lower().count('data science')
        if times > 0:
            count += times

print('data science aparace {0} veces en el texto'.format(count))