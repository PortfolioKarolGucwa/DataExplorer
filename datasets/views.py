from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import UploadedFileForm
from .models import UploadedFile


def dataset_list(request):
    datasets = UploadedFile.objects.all()
    return render(request, 'datasets/list.html', {'datasets': datasets})


def upload_dataset(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dataset uploaded.')
            return redirect('dataset_list')
    else:
        form = UploadedFileForm()

    return render(request, 'datasets/upload.html', {'form': form})


@require_POST
def delete_dataset(request, pk):
    dataset = get_object_or_404(UploadedFile, pk=pk)
    dataset.file.delete(save=False)
    dataset.delete()
    messages.success(request, 'Dataset deleted.')
    return redirect('dataset_list')
