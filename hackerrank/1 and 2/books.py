allBooks = input().split()
checkedBooks = input().split()
availBooks = []
for book in allBooks:
    if book not in checkedBooks:
        availBooks.append(book)
print(" ".join(availBooks))