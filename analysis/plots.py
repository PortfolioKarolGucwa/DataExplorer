import base64
from io import BytesIO

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

MAX_COLUMNS_SHOWN = 15


def missing_values_chart(df):
    """Bar chart of missing-value counts per column, returned as a base64 PNG."""
    missing_counts = df.isna().sum()
    missing_counts = missing_counts.iloc[:MAX_COLUMNS_SHOWN]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(missing_counts.index.astype(str), missing_counts.values, color='#4e79a7')
    ax.set_ylabel('Missing values')
    ax.set_title('Missing values per column')
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    plt.close(fig)

    return base64.b64encode(buffer.getvalue()).decode('ascii')
