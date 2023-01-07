vocales = ['a', 'e', 'i', 'o', 'u']
palabras = input('Introduce una o mas palabras y te devolvere las vocales solamente:')
for i in palabras:
    if i in vocales:
        print(i)
