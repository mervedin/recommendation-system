# 1. Recommendation System

This is a basic collaborative filtering model. I have used MovieLens dataset for this model, you can find it [here](https://grouplens.org/datasets/movielens/1m/) 

Dependencies:
- Pandas
- Tensorflow

Usage:
USER_ID must be between [1-6040]. Given an USER_ID, predict.py recommends 5 movies for that user.

<br> ```python predict.py USER_ID``` </br>
    

Examples:
#### Recommendation for user 2
<br> ```python predict.py 2``` </br>

Output:
```    
Recommendation for user 2:
1.	 It's a Wonderful Life (1946)
2.	 Sanjuro (1962)
3.	 Schindler's List (1993)
4.	 Close Shave, A (1995)
5.	 Sound of Music, The (1965)
```
#### Recommendation for user 300

```python predict.py 300```

Output:
```  
Recommendation for user 300:
1.	 Sanjuro (1962)
2.	 Schindler's List (1993)
3.	 Star Wars: Episode IV - A New Hope (1977)
4.	 Forrest Gump (1994)
5.	 Green Mile, The (1999)
```