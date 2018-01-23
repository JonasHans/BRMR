#########################################
#
# http://strawlab.github.io/python-pcl/#pcl.VoxelGridFilter
#
#########################################

import pcl
import numpy as np
import sys

def importDataFromCSV(fileName):
    original = np.genfromtxt(fileName, delimiter=',')
    data = original[1:]
    return data

# Euclidean cluster extraction
# https://github.com/strawlab/python-pcl/blob/master/tests/test_segmentation.py
def createECE(data):
    # X,Y,X
    inputData = data[:,[3,4,5]]

    # Create pointcloud
    pointCloud = pcl.PointCloud(inputData.astype('float32'))

    #create KD tree
    tree = pointCloud.make_kdtree()

    # Segmenter
    segmenter = pointCloud.make_EuclideanClusterExtraction()
    segmenter.set_ClusterTolerance(0.02)
    segmenter.set_MinClusterSize(100)
    segmenter.set_MaxClusterSize(25000)
    segmenter.set_SearchMethod(tree)
    cluster_indices = segmenter.Extract()

    # Create new clustered cloud
    cloud_cluster = pcl.PointCloud()
    for j, indices in enumerate(cluster_indices):
        points = np.zeros((len(indices), 3), dtype=np.float32)

        for i, indice in enumerate(indices):
            points[i][0] = pointCloud[indice][0]
            points[i][1] = pointCloud[indice][1]
            points[i][2] = pointCloud[indice][2]

    cloud_cluster.from_array(points)
    pcl.save(cloud_cluster, 'output/euclidian-cloud-tol002.pcd')

# Cylinder model segmentation
def createCMS(data):
    # X,Y,X
    inputData = data[:,[3,4,5]]

    # Create pointcloud
    pointCloud = pcl.PointCloud(inputData.astype('float32'))

    # Create segmenter
    segmenter = pointCloud.make_segmenter_normals(ksearch=50)
    segmenter.set_optimize_coefficients(True)
    segmenter.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
    segmenter.set_normal_distance_weight(0.1)
    segmenter.set_method_type(pcl.SAC_RANSAC)
    segmenter.set_max_iterations(500)
    segmenter.set_distance_threshold(25)
    indices, model = segmenter.segment()

    if len(indices) is not 0:
        # Get segmented regions from cloud
        cloud_segmented_true = pointCloud.extract(indices, negative=True)
        cloud_segmented_false = pointCloud.extract(indices, negative=False)

        # Save pointclouds
        pcl.save(cloud_segmented_true, 'output/CMS-cloud-label0-distance25.pcd')
        pcl.save(cloud_segmented_false, 'output/CMS-cloud-label1-distance25.pcd')
    else:
        print "Indices are empty!"

def createPointcloudSegmentation(data):
    # X,Y,X
    inputData = data[:,[3,4,5]]

    # Create pointcloud
    pointCloud = pcl.PointCloud(inputData.astype('float32'))

    segmenter = pointCloud.make_segmenter()
    # segmenter.set_optimize_coefficients(True)
    segmenter.set_model_type(pcl.SACMODEL_PLANE)
    segmenter.set_method_type(pcl.SAC_RANSAC)
    segmenter.set_distance_threshold(50)
    indices, model = segmenter.segment()

    if len(indices) is not 0:
        # Get segmented regions from cloud
        cloud_segmented_true = pointCloud.extract(indices, negative=True)
        cloud_segmented_false = pointCloud.extract(indices, negative=False)

        # Save pointclouds
        pcl.save(cloud_segmented_true, 'output/segmented-cloud-label0-distance25.pcd')
        pcl.save(cloud_segmented_false, 'output/segmented-cloud-label1-distance25.pcd')
    else:
        print "Indices are empty!"

def main(argv):
    print "******************** Begin main function *******************************"
    data = importDataFromCSV('csvData/160930/160930-20-00.csv')
    createCMS(data)
    print "********************* End main function ********************************"
    pass

if __name__ == "__main__":
    main(sys.argv)
