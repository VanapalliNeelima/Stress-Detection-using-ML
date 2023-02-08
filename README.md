# Stress-Detection-using-ML
## Prerequisites :

##### Programming Language(PythonFundamentals,Pandas,Numpys)
##### Statistics
##### Probability
##### Linear Algebra
##### Calculus

## Project Description : 

##### Stress,tension, and misery are undermining the psychological well-being of individuals.Each individual has a justification behind having an unpleasant life. Individuals frequently discuss their thoughts via web-based entertainment stages like on Instagram as posts and stories, and on Reddit through requesting ideas about their life on Subreddits.In the beyond couple of years, many substance makers have approached to make content to assist individuals with their psychological wellness. Numerous associations can utilize pressure discovery to find which virtual entertainment clients are focused on to rapidly help them.
Stress discovery is a difficult undertaking, as there are so many words that can be utilized by individuals on their posts that can show regardless of whether an individual is having mental pressure.

The dataset I’m utilizing for this errand contains information presented on subreddits related to emotional wellness. This dataset contains different emotional well-being issues shared by individuals about their life.

People often share their feelings on social media platforms. Many organizations can use stress detection to find which social media users are stressed to help them quickly.


## Steps For Creating Project

##### 1. Launch Jupiter Notebook
##### 2. Import numpy and pandas
##### 3. Import Dataset
##### 4. Check Description of out data
##### 5. Check if dataset contains null value or not
##### 6. Prepare the text column of this dataset to clean the text column with stopwords,links,special symbols and language errors
##### 7. View the most utilized words by individuals sharing about their life issues  via online entertainment by picturing a word cloud of the text column
##### 8. The label column in this dataset contains labels as 0 and 1. 0 means no stress, and 1 means stress. We will use Stress and No stress lables instead of 1 and 0. So lets prepare this column accordingly and select the text and label columns for the process of training a machine learning model
##### 9. Split the dataset into training and test sets
##### 10. This task is based on the problem of binary classification, We will be using the Bernoulli Naive Bayes algorithm,which one of the best algorithm for binary classification
##### 11. Test the performance of our model on some random sentences based on mental health
######  Ex:- "I think we need to take care of ourselves"
######  Ex:- "I am feeling sad"
