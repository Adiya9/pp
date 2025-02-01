movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1 
a = input()
def movie(mov):
    if mov.get("name") == a: 
         return mov.get("imdb") > 5.5
    return False
for i in range(len(movies)):
    if movie(movies[i]):
        print(True)

#2 
def mov(movie):
    return movie["imdb"] > 5.5
a = int(input())
if mov(movies[a]):
    print(movies[a])
else:
    print("none")

#3
def by_categ(aspect):
        if name in movies[i].get("category"):
            print(movies[i])
name = input("write category name: ")
for i in range(len(movies)):
    by_categ(movies[i])

#4 
def average(movies):
    sum = 0
    cnt = 0
    for i in range(len(movies)):
        sum += movies[i].get("imdb")
        cnt += 1
    print(sum/cnt) 
average(movies)

#5
list1 = []
sum = 0
def by_categ(aspect):
    if name == aspect.get("category"):
        list1.append(aspect.get("imdb"))
name = input("write category name: ")
for i in range(len(movies)):
    by_categ(movies[i])
for i in range(len(list1)):
    sum += list1[i]
print(sum/len(list1))