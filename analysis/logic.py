import pandas as pd

PREVIEW_ROWS = 10


class DatasetReadError(Exception):
    """Raised when the uploaded file can't be parsed as a CSV."""


def read_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as exc:
        raise DatasetReadError(f"Couldn't read this file as a CSV: {exc}") from exc


def summarize_dataset(df):
    columns = []
    for name in df.columns:
        columns.append({
            'name': name,
            'dtype': str(df[name].dtype),
            'missing': int(df[name].isna().sum()),
        })

    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        stat_names, stats = [], []
    else:
        described = numeric_df.describe().round(2)
        stat_names = list(described.index)
        stats = described.T.reset_index(names='column').to_dict('records')

    return {
        'row_count': len(df),
        'column_count': len(df.columns),
        'columns': columns,
        'preview': df.head(PREVIEW_ROWS).fillna('').to_dict('records'),
        'stat_names': stat_names,
        'stats': stats,
    }
