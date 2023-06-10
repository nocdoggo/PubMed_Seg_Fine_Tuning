# 06-10-2023 Meeting Notes

## `TO-DO:`

1. Try to balance the dataset across different classes. For instance, randomly sample 50k samples for each category, currently, we have way too excessive amount of results. —> for point one, I guess most importantly we need to make sure that the class distribution should keep the same between the training and testing set (like if the training set has 10% of the results category and 20% of the methods category then the testing set should have the same percentage). Balancing over all classes is good to try as well. 

2. When choosing the dataset, it is okay for one of the papers to lack some of the labels, say, missing the results section, then it might be okay since we are randomly selecting and training our model

3. Try to use PCA or umap while constructing the model. For instance, we initially have 256 features, then apply pca, reduce the number of features by only selecting the top useful features, in this way, we can get to keep our model as efficient as we can. —> For point three, one of the ways to pick the top features is to plot the variance. Try to pick the threshold where the explanation of variance drops. The algorithm will do the ranking itself, we only need to come up with the threshold

   > [PCA Explained Variance Concepts with Python Example - Data Analytics (vitalflux.com)](https://vitalflux.com/pca-explained-variance-concept-python-example/)
   >
   > [python 3.x - Interpretation of PCA explained variance ratio - Stack Overflow](https://stackoverflow.com/questions/55678708/interpretation-of-pca-explained-variance-ratio)

4. Train on ALTA-NICTA:

   1. If the accuracy is around 80-90 %, then we can still talk about it in the paper;
   2. If over 90 % or even higher, then it is super good to discuss about it in the paper;
   3. If accuracy is a hit or miss, it could be: distribution, or categorizing

    