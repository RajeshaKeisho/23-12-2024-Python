from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import File 
from .forms import FileForm 
from django.conf import settings 
import os

# Create your views here.
def create_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'mtmApp/create_file.html', {'form':form})

def file_list(request):
    files = File.objects.all()
    file_contents = []

    for file in files:
        try:
            with open(file.file.path, 'r', encoding='latin-1') as file_content:
                content = file_content.read()
                file_contents.append({"file":file, 'content':content})
        except FileNotFoundError:
            content = "File content not available"
            file_contents.append({"file":file, 'content':content})
        except UnicodeDecodeError:
            content = "Unable to decode file content"
            file_contents.append({"file":file, 'content':content})

    return render(request, 'mtmApp/file_list.html', {'file_contents':file_contents})

def download_file(request, file_id):
    try:
        file = File.objects.get(pk = file_id)
        file_path = file.file.path 

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type = 'application/octet-stream')
                response['Content_Disposition'] = f"Inline; Filename={os.path.basename(file_path)}"
                return response
        else:
            return HttpResponseNotFound("File Not Found")
    except File.DoesNotExist:
            return HttpResponseNotFound("File Not Found")
    except Exception as e:
        return HttpResponse(f"An error occurred{str(e)}")
    




























