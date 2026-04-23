from django.shortcuts import render, redirect
from .forms import uploaded_file_form

def upload_file(request):
    if request.method == 'POST':
        form = uploaded_file_form(request.POST, request.FILES) #handle file upload with request.FILES
        if form.is_valid():
            form.save()
            return redirect('success_url') #replace 'success_url' with the actual URL name you want to redirect to after successful upload
    else:
        form = uploaded_file_form() #create an empty form instance for GET request
    
    return render(request, 'datasets/upload.html', {'form': form}) #render the form in the template 'datasets/upload.html' and pass the form instance to the context