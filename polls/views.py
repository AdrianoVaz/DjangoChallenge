from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import uuid

def index(request):
    fs = FileSystemStorage()
    filesList = fs.listdir(settings.MEDIA_ROOT)
    context = {
        'files' : filesList[1],
    }
    return render(request, 'polls/index.html', context)
    
def upload(request):
    if request.method == 'POST' and request.FILES['fileToUpload']:
        myfile = request.FILES['fileToUpload']
        fs = FileSystemStorage()
        filenameTokens = myfile.name.split(".")
        extension = filenameTokens[len(filenameTokens) - 1]
        newFilename = str(uuid.uuid4()) + '.' + extension
        filename = fs.save(newFilename, myfile)
        context = {
            'upload_success' : True,
        }
        return render(request, 'polls/upload.html', context)
    return render(request, 'polls/upload.html')

def image(request, image_name):
    context = {
        'image_name': image_name,
    }
    return render(request, 'polls/image.html', context)

def deleteImage(request, image_name):
    fs = FileSystemStorage()
    fs.delete(settings.MEDIA_ROOT + '/' + image_name)
    filesList = fs.listdir(settings.MEDIA_ROOT)
    context = {
        'files' : filesList[1],
    }
    return render(request, 'polls/index.html', context)


