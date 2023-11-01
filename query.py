from movies import Movies

movies = Movies('./movies.txt')

def search_movie(search):
    search.lower()
    for movie in movies._movies:
        if search in movie["name"].lower():
            print(movie["name"])
    

def search_cast(search):
    search.lower()
    for movie in movies._movies:
        castList = []
        for name in movie['cast']:
            if search in name.lower():
                castList.append(name)
                
        if castList:
            print(movie["name"])
            print(castList)

def list_movies():
    for movie in movies._movies:
        print(movie["name"])
   

while True:
    print("\nq: quit \nsn: search movie names \nsc: search casts \nlist: prints all movie names \n:", end='')
    userInput = input()
    if userInput == 'q':
        print('Have a nice day')
        break
    elif userInput == 'sn':
        searchTerm = input('Search Movie: ')
        search_movie(searchTerm)
    elif userInput == 'sc':
        castSearch = input('Enter cast member: ')
        search_cast(castSearch)
    elif userInput == 'list':
        list_movies()
    else :
        print('Incorrect input\n')

