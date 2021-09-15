from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://127.0.0.1:27017/?readPreference=primary&serverSelectionTimeoutMS=2000&appname=MongoDB%20Compass&directConnection=true&ssl=false")
# client = MongoClient("mongodb+srv://dbUser:dbUserPassword@cluster0.c0vn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.business
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
# print(serverStatusResult)

# client = MongoClient(host='localhost',port=27017)
# db = client.business
#Step 2: Create sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
size = 2 # 501
for x in range(1, size):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    
    result=db.reviews.insert_one(business)
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print(f'finished creating {size - 1} business reviews')

fivestar = db.reviews.find_one({'rating': 5})
print('One five star review:')
pprint(fivestar)

# fiveStarCount = db.reviews.find({'rating': 5}).count()
fiveStarCount = db.reviews.count_documents({'rating': 5})
print(f'Five star reviews count: {fiveStarCount}')

print('--------------------- DEMO QUERY AGGREGATION')
# use the aggregation framework to sum the occurrence of each rating across the entire data set
print('\nThe sum of each rating occurance across all data grouped by rating ')
stargroup=db.reviews.aggregate(
# The Aggregation Pipeline is defined as an array of different operations
[
  # The first stage in this pipe is to group data
  { 
    '$group':
      {
        '_id': "$rating",
        "count" : { '$sum' :1 }
      }
  },
  # The second stage in this pipe is to sort the data
  {
    "$sort":  { "_id":1}
  }
])
# Print the result
for group in stargroup:
    print(group)

print('--------------------- DEMO UPDATE')
aSingleReview = db.reviews.find_one({})
print(f'Before: {aSingleReview}')
result = db.reviews.update_one({'_id' : aSingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

updatedDocument = db.reviews.find_one({'_id': aSingleReview.get('_id')})
print(f'The updated document: {updatedDocument}')

result = db.reviews.delete_one({'_id': aSingleReview.get('_id')})
print(f'Number of documents deleted, deleted_count:{result.deleted_count}')
result = db.reviews.find_one({'_id': aSingleReview.get('_id')})
print(f'The deleted document should be [None]: {result}')


