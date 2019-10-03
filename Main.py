def cosseno(rating1, rating2):
    x = 0
    y = 0
    xy = 0
    sum_x2 = 0
    sum_y2 = 0

    for key in rating1:
        if key in rating2:
            x += pow(rating1[key], 2)
            y += pow(rating2[key], 2)
            sum_x2 = sqrt(x)
            sum_y2 = sqrt(y)
            xy += rating1[key] * rating2[key]

    if xy == 0:
        return 0
    else:
        return (xy / (sum_x2 * sum_y2))

###########################################3

#https://data.world/andidewa/books/workspace/file?filename=ratings.csv

def loadBooksDataSet(path='/Users/robsonjamesjunior/PycharmProjects/Project-Recommendation-System/'):
    books = {}
    for linha in open(path + '/books.csv'):
        (book_id, book_title) = linha.split(',')[0:2]

        books[book_id] = book_title

    base = {}
    for linha in open(path + '/ratings.csv'):
        (book_id,user_id,rating) = linha.split(',')
        base.setdefault(user_id, {})
        base[user_id][books[book_id]] = float(rating)
    return base