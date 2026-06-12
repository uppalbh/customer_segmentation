# Customer Segmentation Using K-Means Clustering

## Overview

This project focuses on segmenting customers into distinct groups using unsupervised machine learning techniques. The goal is to identify meaningful patterns in customer behavior based on demographic and spending attributes.

The workflow includes:
* Exploratory Data Analysis (EDA)
* Feature preprocessing and scaling
* Optimal cluster selection using Elbow Method and Silhouette Score
* K-Means clustering implementation
* Cluster interpretation and profiling
* Dimensionality reduction using PCA for visualization

---

## Business / Real-World Problem

Customer segmentation is a critical task in marketing analytics and business intelligence. It enables organizations to:

* Target customers with personalized marketing strategies
* Improve customer retention through tailored engagement
* Identify high-value vs low-value customer groups
* Optimize product recommendations and pricing strategies

Understanding customer structure helps businesses move from generic marketing to data-driven personalization.

---

## Dataset

The dataset contains basic customer attributes:

### Features

* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

These features represent demographic and behavioral spending patterns.

---

## Data Preprocessing

### Feature Encoding

* Gender was encoded into numerical format:
  * Male → 1
  * Female → 0

### Feature Scaling

To ensure fair distance-based clustering:

* StandardScaler was applied
* Features were normalized to have zero mean and unit variance

This is essential because K-Means is sensitive to feature scale.

---

## Exploratory Data Analysis (EDA)

Initial analysis included:

* Checking feature distributions
* Understanding data structure and types
* Verifying encoding correctness
* Observing relationships between income and spending behavior

Key observation:
* Customers show visible grouping tendencies in income vs spending score space.

---

## Choosing the Number of Clusters

### Elbow Method

WCSS (Within-Cluster Sum of Squares) was computed for different values of K:

* K values tested from 1 to 10
* Elbow point used to identify optimal cluster count

The point where WCSS reduction slows significantly indicates optimal clustering structure.

---

### Silhouette Score Analysis

Silhouette score was used to validate clustering quality:

* K values tested from 2 to 10
* Higher silhouette score indicates better-defined clusters

This provided a secondary validation for selecting optimal K.

---

## Model Selection

Based on Elbow Method and Silhouette Score analysis:

* Final number of clusters chosen: **K = 4**

K-Means was trained on full dataset using this optimal cluster count.

---

## Cluster Assignment

After training:

* Each customer was assigned a cluster label
* Distribution of customers across clusters was analyzed
* Cluster-level averages were computed for interpretation

### Cluster Profiling

Clusters were interpreted based on:

* Age
* Annual Income
* Spending Score

This helped identify distinct customer archetypes such as:
* High income, low spending customers
* Low income, high spending customers
* Balanced customers
* Conservative spenders

---

## Key Cluster Insights

The clustering revealed clear behavioral segmentation:

* Some clusters represent high-income but low-spending customers (potential upsell targets)
* Some represent high-spending younger customers (marketing priority segment)
* Middle clusters show balanced behavior
* Older groups tend to have moderate spending patterns

These insights are valuable for targeted marketing strategies.

---

## 2D Feature-Based Clustering

A simplified model was trained using only:

* Annual Income
* Spending Score

This helped visualize clear cluster separation in 2D space.

K-Means effectively separated customers into distinct behavioral groups in this reduced feature space.

---

## PCA Visualization

Principal Component Analysis (PCA) was applied to reduce dimensionality:

* Data projected into 2 principal components
* Clusters visualized in 2D space
* Cluster centroids plotted for interpretability

### Outcome

* PCA confirmed that clusters are well-separated in lower-dimensional space
* Centroids helped visualize cluster centers and spread

---

## Model Summary

### Algorithm Used

* K-Means Clustering

### Key Strengths

* Simple and efficient
* Works well with normalized numerical data
* Produces interpretable cluster groups

### Limitations

* Requires predefined number of clusters
* Sensitive to initialization and scaling
* Assumes spherical cluster distribution

---

## Technologies Used

### Programming Language

* Python

### Data Handling

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn (KMeans, PCA, Silhouette Score)

---

## Visualizations

The project includes multiple visual outputs:

### Cluster Selection

* Elbow Method (WCSS curve)
* Silhouette Score analysis

### Cluster Visualization

* 2D scatter plots using income and spending score
* PCA-based cluster visualization
* Cluster centroid plotting

---

## Future Improvements

* Use DBSCAN or Gaussian Mixture Models for better clustering flexibility
* Apply feature engineering for richer customer behavior modeling
* Integrate additional features such as purchase history or transaction frequency
* Build a recommendation system based on cluster labels
* Deploy clustering results in a marketing dashboard

---

## Conclusion

This project demonstrates a complete unsupervised learning pipeline for customer segmentation.

K-Means clustering successfully identified meaningful customer groups based on income and spending behavior. PCA visualization further confirmed clear separation between clusters.

The insights generated can be directly used for targeted marketing, customer retention strategies, and business decision-making.
