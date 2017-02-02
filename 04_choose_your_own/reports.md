| Samples | Features |                   Method                    | Accuracy | Time (s) | Best |   Note   |
|---------|----------|---------------------------------------------|----------|----------|------|----------|
|         |          | KN(algorithm='brute')                       |     0.92 |     0.01 |      |          |
|         |          | KN(algorithm='brute',n_neighbors=10)        |    0.932 |     0.01 |      |          |
|         |          | KN(algorithm='brute',n_neighbors=20)        |    0.936 |    0.001 |      |          |
|         |          | KN(algorithm='brute',n_neighbors=18)        |    0.939 |    0.001 | *    |          |
|         |          | AdaBoost()                                  |    0.924 |    0.175 |      |          |
|         |          | AdaBoost(n_estimators=20)                   |    0.928 |    0.067 |      |          |
|         |          | AdaBoost(n_estimators=20,learning_rate=2.0) |    0.936 |    0.069 |      |          |
|         |          | RandomForest()                              |    0.912 |     0.04 |      |          |
|         |          | RF(n_estimators=10)                         |     0.92 |    0.067 |      |          |
|         |          | RF(n_estimators=10,min_samples_split=36)    |    0.932 |     0.05 |      | Unstable |







