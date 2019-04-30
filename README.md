# Develop simple recommendation engine with python 
This is a sample code for training building a simple recommendation engine.  
As a first step, you will learn how to organize software stuck for a simple recommendation engine with this sample code.  


## The first example: pre-defined model  
The first example of this sample code provides a quite simple recommendation engine 
just return recommendations based on pre-defined model.  
Pre-defined model just returns recommendation results from training dataset 
for specified product key. 


## Project structure of first example
### How to get training dataset  
You can get training dataset which is pre-defined in **ToyDataset** class as a form 
of python dict object.  
With **load_toydataset** method, you can get the training dataset.
 The argument **seed** can specify random seed to generate training dataset.

```python
from recommend_sample.datasets.toy_dataset import load_toydataset

train_set = load_toydataset(seed=123)
# --> train_set = {0: [3, 2, 3, 3, 1, ... }

```   

### How to get trained model and get recommendations results
The class RankRecommend provides core functionality of 
simple recommendation engine based on item occurences.  
The RankRecommend has a method named **fit** to train model based on 
given training dataset.  
Then, you can get recommendation results by executing method **predict** with 
argument key to specify the identifier for which you'd like to get recommendations.
Basic usage of this sample is as follows:  

```python
from recommend_sample.models.rank_recommend import RankRecommend

rec = RankRecommend()
rec.fit(train_set)
rec.predict(0)
# --> you'll get the recommendation results for product id = 0.

```


## Sample code
There is a sample code using this module 
with command line arguments.  

```commandline
$ git clone https://github.com/yukoga/recommend_sample1.git
$ cd recommend_sample1
$ python example/sample2.py 

Training data loaded.
Finish training for recommendations
Top 20 recommendations for item 0 is [2, 1, 3, 5, 4].  
```  

With the optional argument **all**, you will get all recommendation results 
and training dataset as follows.

```commandline
$ python example/sample2.py --all

Training data loaded.
Finish training for recommendations
Top 20 recommendations for item 0 is [2, 1, 3, 5, 4].


/*** training dataset ***/
0 [3, 5, 3, 2, 4, 3, 4, 2, 2, 1, 2, 2, 1, 1, 2, 4, 5, 1, 1, 5]
1 [2, 4, 3, 5, 3, 5, 0, 0, 2, 4, 5, 5, 5, 2, 4, 3, 2, 5, 0, 4]
2 [3, 0, 4, 3, 3, 3, 3, 5, 4, 4, 5, 5, 4, 3, 0, 5, 4, 1, 4, 3]
3 [1, 2, 5, 0, 1, 5, 2, 1, 1, 4, 5, 1, 0, 0, 4, 1, 4, 4, 4, 1]
4 [1, 2, 3, 3, 3, 3, 0, 1, 3, 1, 5, 3, 1, 2, 3, 5, 3, 1, 0, 0]
5 [3, 0, 1, 1, 0, 3, 1, 3, 4, 4, 1, 4, 4, 3, 4, 3, 0, 4, 4, 4]


/*** recommendation results ***/
Recommendations for item 0 is [2, 1, 3, 5, 4].
Recommendations for item 1 is [5, 2, 4, 3, 0].
Recommendations for item 2 is [3, 4, 5, 0, 1].
Recommendations for item 3 is [1, 4, 5, 0, 2].
Recommendations for item 4 is [3, 1, 0, 2, 5].
Recommendations for item 5 is [4, 3, 1, 0].  
```  

