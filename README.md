## The Effect of Trainable Parameter Count on Training Time and Accuracy
- This is the code used in Josh Silverberg's UROP research project on The Effect of Trainable Parameter Count on Training Time and Accuracy in the context of automatic Reddit comment generation, created with mentorship from Dr. Paramveer Dhillon
- The full symposium poster can be found *[here](https://drive.google.com/file/d/1spXu6-lUMrCUJRdEKuX8dligpyoGDfrH/view?usp=sharing)*
- This code is based off of the ACL 2019 SRW paper *[AGPC: Automatic Generation of Personalized Comment Based on User Profile](https://arxiv.org/pdf/1907.10371v1.pdf)* by Zeng et. al.

### Requirements
* Python 3.5
* tensorflow 1.4

### Preprocessing
```
python prep_data.py 
```
The sample data for one subreddit is provided in sample_raw_data/reddit_test_sample_data_1.csv

================================================================

### Training
```
python train_PCGN.py
```
All configurations and hyperparameters of the model are in configs/pcgn_config.yaml

================================================================

### Inference and Evaluation
```
python infer_PCGN.py
```

