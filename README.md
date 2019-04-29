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
You can get training dataset which is pre-defined in **SimpleToy** class as a form 
of python dict object.  
With **load_simpletoy** method, you can get the training dataset as follows:

```python
from recommend_sample.datasets.simple_toy import load_simpletoy

train_set = load_simpletoy()
# --> train_set = {0: [4, 1, 4, 4, 3], 1: [4, 2, 4, 3, 2], ... }

```   

### How to get trained model and get recommendations results
The class ToyRecommend provides core functionality of 
simple recommendation engine.  
The ToyRecommend has a method named **fit** to train model based on 
given training dataset.  
Then, you can get recommendation results by executing method **predict** with 
argument key to specify the identifier for which you'd like to get recommendations.
Basic usage of this sample is as follows:  

```python
from recommend_sample.models.toy_recommend import ToyRecommend

rec = ToyRecommend()
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
$ python example/sample1.py 

Training data loaded.
Finish training for recommendations
Top 5 recommendations for item 0 is [4, 1, 4, 4, 3].  
```  

You can set the argument **key** to specify item key 
and **top_n** to specify how many recommendations you get.

```commandline
$ python example/sample1.py --key=1 --top_n=3

Training data loaded.
Finish training for recommendations
Top 3 recommendations for item 1 is [4, 2, 4].  
```  
