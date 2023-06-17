## 06-17-2023 Meeting Notes

## `TO-DO`:

1. A more comprehensive and less biased approach would be to download the most recent 100k to 200k articles from the overall pool of submissions on PubMed. This approach differs from our current method where we selectively downloaded datasets pertaining to specific diseases, which was randomly chosen. By opting for this new data collection strategy, we can ensure a wider range of topics, including new and emerging trends in medical research, and have a sample that is representative of recent research activities. This method allows for a broader scope of analysis rather than focusing solely on specific diseases. Also, this proactive approach could help address potential concerns from reviewers about the selective nature of our data collection. Reviewers might question the representativeness and comprehensiveness of our dataset if we continue to cherry-pick specific diseases.
2. In terms of utilizing the disease-centric dataset we currently possess, a crucial consideration is ensuring that our training, testing, and validation sets each contain a balanced or equal number of entries for every disease. This is to ensure that our model is well-equipped to handle all the diseases in our dataset, rather than being particularly good at predicting some and poor at predicting others due to an imbalance in the distribution of diseases across the datasets. To achieve this, we need to implement a stratified sampling technique, where we ensure that each class/disease is equally represented in our train, test, and validation sets, to ensure that each disease category is adequately represented in the datasets that we use for model training and evaluation. Also, it would be worthwhile to run an experimental comparison to evaluate the effectiveness of this method, whether this balanced distribution of diseases across the datasets can yield better accuracy in our text summarization task.
3. Continue focusing on removing special symbols and characters which may have found their way into our dataset during the data gathering process. These symbols and characters often add no meaningful content and can hinder our model's ability to learn effectively from the data. We should also consider employing other text normalization techniques like converting all text to lowercase and removing stop words - common words that often carry little meaning like 'and', 'the', or so on. Our goal is to enhance the quality of our dataset until it's on par with the quality of published datasets.
4. Try examining the language models that have been specifically trained on PubMed data. Given the specialized language and complex subject matter often found in medical literature, leveraging a model that is already familiar with this type of content could provide substantial benefits for our project. We should look into models like BioBERT, BioXLNet, or BlueBERT which are designed and trained for biomedical text mining tasks. There's also the possibility of using general-purpose language models like GPT-3 or BERT and fine-tuning them on our specific PubMed dataset.



## 06-10-2023 Meeting Notes

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

    