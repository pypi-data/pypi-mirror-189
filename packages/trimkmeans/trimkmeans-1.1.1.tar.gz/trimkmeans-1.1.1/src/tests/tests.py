"""
unittests for packaging
"""
import heapq
import unittest

import numpy as np

from src.trimkmeans.metrics import trimmed_kmeans_metric_supervised
from src.trimkmeans.metrics import trimmed_kmeans_metric_unsupervised
from src.trimkmeans.trimkmeans import TrimKMeans


class TestingTrimKMeans(unittest.TestCase):
    """
    tests for the TrimKMeans class
    """

    def test_private_create_points(self):
        """
        asserts if ClusterPoints created by TrimKMeans private method are created like expected
        :return: None
        """
        trimkmeans = TrimKMeans()
        x_train = np.array([[1, 1], [2, 2], [3, 3]])
        centroids = np.array([[1, 1], [2, 2], [3, 3]])
        cp1 = trimkmeans.ClusterPoint(np.array([1, 1]))
        cp2 = trimkmeans.ClusterPoint(np.array([2, 2]))
        cp3 = trimkmeans.ClusterPoint(np.array([3, 3]))
        cp1.dist, cp2.dist, cp3.dist = -0.0, -0.0, -0.0
        cp1.cluster, cp2.cluster, cp3.cluster = 0, 1, 2
        sorted_points = []
        heapq.heappush(sorted_points, cp1)
        heapq.heappush(sorted_points, cp2)
        heapq.heappush(sorted_points, cp3)
        test_data = trimkmeans._TrimKMeans__create_points(x_train, centroids)
        self.assertIsNone(np.testing.assert_array_equal(np.array(sorted_points), np.array(test_data)))

    def test_empty_data(self):
        """
        Tests if empty input data raises the right error
        :return: None
        """
        trimkmeans = TrimKMeans(n_clusters=3)
        testdata = np.array([])
        with self.assertRaises(ValueError):
            trimkmeans.fit(testdata)

    def test_cluster_one_dim(self):
        """
        Tests if fit() method works as expected if points are one-dimensional
        :return: None
        """
        trimkmeans = TrimKMeans(n_clusters=3, trim=0.3, n_init=1000)
        testdata = np.array([[-100.], [0.], [1.], [100.]])
        try:
            trimkmeans.fit(testdata)
        except RuntimeError:
            self.fail("fit() with one dimensional data failed")

    def test_init_with_centroids(self):
        """
        Tests if fit() method works as expected if points are provided via the init parameter
        :return: None
        """
        trimkmeans = TrimKMeans(n_clusters=3, trim=0.3, n_init=1, init=np.array([[0., 1.], [1., 2.], [2., 3.]]))
        testdata = np.array([[0., 1.], [1., 2.], [2., 3.], [3., 4.]])
        try:
            trimkmeans.fit(testdata)
            trimkmeans.predict(testdata)
        except RuntimeError:
            self.fail("fit() with init centroids failed")

    def test_less_points_then_cluster(self):
        """
        Tests if a size error is raised which stems from a dataset with fewer points than clusters specified
        :return: None
        """
        trimkmeans = TrimKMeans(n_clusters=4)
        testdata = np.array([[1], [2], [3]])
        with self.assertRaises(ValueError):
            trimkmeans.fit(testdata)

    def test_trim_to_big(self):
        """
        Tests if a size error is raised even if the size error is created during trimming
        :return: None
        """
        trimkmeans = TrimKMeans(n_clusters=3, trim=0.4)
        testdata = np.array([[1], [2], [3]])
        with self.assertRaises(ValueError):
            trimkmeans.fit(testdata)


class TestingMetrics(unittest.TestCase):
    """
    Tests for the trimmed kmeans metrics from trimkmeans.metrics
    """

    def test_trimmed_kmeans_silhouette(self):
        """
        Tests the silhouette score metric for trimmed data
        :return:
        """
        self.assertEqual(1, trimmed_kmeans_metric_unsupervised([[0], [1], [2], [1.5], [2], [1], [0]],
                                                               [0, 1, 2, 3, 2, 1, 0],
                                                               'silhouette_score'))

    def test_trimmed_kmeans_rand(self):
        """
        Tests the rand score metric for trimmed data
        :return:
        """
        self.assertEqual(1, trimmed_kmeans_metric_supervised([0, 1, 2], [0, 1, 2], 'rand_score'))


if __name__ == '__main__':
    unittest.main()
