Typically a REST API that permits you to store and recover sections of content in conjunction with the mapping of words to the sections they show up in.
The API is built utilizing Python and the Django REST System, and it stores the information in a SQLlite database. 


API Endpoints

1.Store Paragraphs:

Endpoint: /api/paragraphs/
Method: POST
Request Body:
{
  "context": "This is the first paragraph. This is the second paragraph."
}


2.Search for a Word:

Endpoint: /api/paragraphs/?search=<word>
Method: GET

Response:
[
  {
    "id": "1234",
    "context": "This is the first paragraph. This is the second paragraph.",
  
  },
  {
    "id": "5678",
    "context": "Another paragraph with the word 'this' in it.",
 
  }
]


Technical Details
The API is built using Python and the Django REST Framework.
The data is stored in a SQLite database.
The words are tokenized by splitting at whitespace and converted to lowercase.
A unique ID is generated for every paragraph that is indexed.
A paragraph is defined by two newline characters.


The API will be available at http://localhost:8000/api/

