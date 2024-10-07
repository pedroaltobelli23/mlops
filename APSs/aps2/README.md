# 24-2-mlops-aps02-pedroaltobelli23

1. Get the data inside the database and save into parquet file 
<pre><code>cd src/</code></pre>
<pre><code>python3 get_data.py</code></pre>

2. Train model using data
<pre><code>python3 train.py ../data/train_data.parquet</code></pre>

3. Use predict.sql to create table that will be predicted 

4. Predict using the trained model
<pre><code>python3 predict.py ../models/model.pkl</code></pre>
