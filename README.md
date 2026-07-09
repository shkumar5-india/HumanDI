<body>

<div class="container">

<h1>🌍 Human Development Index (HDI) Prediction</h1>

<p>

This project predicts the <strong>Human Development Index (HDI)</strong>
using a Machine Learning Linear Regression model. The application is
developed using Python, Scikit-learn and Flask, providing an interactive
web interface where users can enter socio-economic indicators and obtain
the predicted HDI score.

</p>

<hr>

<h2>📌 Project Objective</h2>

<p>

The objective of this project is to estimate the Human Development Index
using important development indicators such as Life Expectancy,
Education and Gross National Income.

</p>

<hr>

<h2>📊 Input Features</h2>

<ul>

<li>Life Expectancy at Birth (2021)</li>

<li>Expected Years of Schooling (2021)</li>

<li>Mean Years of Schooling (2021)</li>

<li>Gross National Income Per Capita (2021)</li>

</ul>

<hr>

<h2>🎯 Output</h2>

<p>

The application predicts the Human Development Index (HDI) score using
the trained Linear Regression model.

</p>

<hr>

<h2>🛠 Technologies Used</h2>

<table>

<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>Programming Language</td>
</tr>

<tr>
<td>Pandas</td>
<td>Data Processing</td>
</tr>

<tr>
<td>NumPy</td>
<td>Numerical Computation</td>
</tr>

<tr>
<td>Matplotlib & Seaborn</td>
<td>Data Visualization</td>
</tr>

<tr>
<td>Scikit-learn</td>
<td>Machine Learning</td>
</tr>

<tr>
<td>Flask</td>
<td>Web Framework</td>
</tr>

<tr>
<td>Pickle</td>
<td>Model Serialization</td>
</tr>

<tr>
<td>HTML & CSS</td>
<td>Frontend UI</td>
</tr>

</table>

<hr>

<h2>📁 Project Structure</h2>

<pre>

HDI_Prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Dataset/
├── Training/
├── static/
│      └── style.css
└── templates/
       ├── home.html
       └── index.html

</pre>

<hr>

<h2>⚙ Installation</h2>

<pre>

pip install -r requirements.txt

</pre>

<hr>

<h2>▶ Run Application</h2>

<pre>

python app.py

</pre>

<p>

Open the browser and visit

</p>

<pre>

http://127.0.0.1:5000

</pre>

<hr>

<h2>🔄 Application Workflow</h2>

<ol>

<li>User opens the application.</li>

<li>User enters the required HDI indicators.</li>

<li>Flask receives the input values.</li>

<li>The trained model (<code>model.pkl</code>) is loaded.</li>

<li>The Linear Regression model predicts the HDI score.</li>

<li>The predicted HDI is displayed on the web page.</li>

</ol>

<hr>

<h2>📈 Machine Learning Algorithm</h2>

<p>

The project uses the <strong>Linear Regression</strong> algorithm from
Scikit-learn for predicting Human Development Index values based on
selected socio-economic indicators.

</p>

<hr>

</div>

</body>
