from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body' : None,
            'description': 'Returns an array of notes'

        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body' : None,
            'description': 'Returns a single note object'

        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body' : {'body': ""},
            'description': 'Creates new note with data sent in post request'

        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body' : {'body': ""},
            'description': 'Creates an existing note with data sent in put request'

        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body' : None,
            'description': 'Deletes an existing note'

        },
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body' : None,
            'description': 'Returns an array of notes'

        }
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    #query the database
    notes = Note.objects.all()
    #Use NoteSerializer to serialize multiple data objects
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#Serialize data
def getNoteById(request, pk):
    #query the database by primary key
    note = Note.objects.get(id=pk)
    #Use NoteSerializer to serialize a single data object
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted   ")
    


