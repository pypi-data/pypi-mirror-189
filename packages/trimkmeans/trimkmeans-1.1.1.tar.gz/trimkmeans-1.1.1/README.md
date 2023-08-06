# trimkmeans

The trimmed k-means clustering method by Cuesta-Albertos, Gordaliza and Matran (1997). This optimizes the k-means
criterion under trimming a portion of the points.

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

example usage:

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

from trimkmeans.metrics import trimmed_kmeans_metric_unsupervised
from trimkmeans.trimkmeans import TrimKMeans

if __name__ == "__main__":

    # Create a dataset of 2D distributions
    CENTERS = 5
    X_train, true_labels = make_blobs(n_samples=100, centers=CENTERS, random_state=42)
    X_train = StandardScaler().fit_transform(X_train)
    # Fit centroids to dataset
    trimkmeans = TrimKMeans(n_clusters=CENTERS, verbose=1)
    trimkmeans.fit(X_train)
    # View results
    labels = trimkmeans.predict(X_train)
    print(f"optimal criterion value found is: {trimkmeans.crit_val}")
    print(f"sum of variances is: {trimmed_kmeans_metric_unsupervised(X_train, labels, 'sv')}")
    print(f"sum of standart deviations is : {trimmed_kmeans_metric_unsupervised(X_train, labels, 'sed')}")
    sns.scatterplot(x=[X[0] for X in X_train],
                    y=[X[1] for X in X_train],
                    hue=labels,
                    style=labels,
                    palette="deep",
                    legend=None
                    )
    plt.plot([x for x, _ in trimkmeans.cluster_centers_],
             [y for _, y in trimkmeans.cluster_centers_],
             'k+',
             markersize=10,
             )

    for idx, centroid in enumerate(trimkmeans.cluster_centers_):
        circle = plt.Circle(centroid, trimkmeans.opt_cutoff_ranges[idx], fill=False, color='r')
        plt.gca().add_patch(circle)
    plt.show()
```
