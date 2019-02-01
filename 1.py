users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    for frnd in friendship:
        if(frnd[0] == user["id"] or frnd[1] == user["id"]):
            count += 1
    return count

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    sortDict={}
    for user in users:
        userCount=num_friends(user)
        sortDict[user["name"]]=userCount
    for user in sorted(sortDict.items(), key=lambda k: k[1], reverse = True):
        print ("%s has %s friends" % (user[0], user[1]))
    

sort_by_num_friends()
