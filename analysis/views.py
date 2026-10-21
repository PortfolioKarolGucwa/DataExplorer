from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from datasets.models import UploadedFile

from .logic import DatasetReadError, read_dataset, summarize_dataset
from .plots import missing_values_chart


def dataset_analysis(request, pk):
    dataset = get_object_or_404(UploadedFile, pk=pk)

    try:
        df = read_dataset(dataset.file.path)
    except DatasetReadError as exc:
        messages.error(request, str(exc))
        return redirect('dataset_list')

    summary = summarize_dataset(df)
    chart = missing_values_chart(df) if df.isna().any().any() else None

    return render(request, 'analysis/detail.html', {
        'dataset': dataset,
        'summary': summary,
        'chart': chart,
    })
