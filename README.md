# machine-learning-fundamentals

## Dependencies 
### Software Dependencies
1. [Python (v3.13.5)](https://www.python.org/downloads/)
2. [Visual Studio Code (v1.101.2)](https://code.visualstudio.com/?WT.mc_id=academic-77958-bethanycheum)  


### Internal Project Dependencies

### External Project Dependencies (**pip install -r requirements.txt**)
1. Jupyter Notebook: Jupyter Notebooks are essentially interactive computing environments that allow for code execution, visualization, and sharing of insights within a single document, making them ideal for data exploration, analysis, and prototyping. Their ease of use and ability to combine code, visualizations, and documentation make them a cornerstone tool for many data science workflows.   
2. Scikit-learn (sklearn): This is a popular choice for machine learning tasks. Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities.
3. matplotlib: a graph plotting library
4. numpy: for handling numeric data in python



## 🗃️ Topics
| #    | Topic | **Programs/Assignments Link** | **Description** |
| --- | ---------------|---------------------|-------------------|
| 01 | Regression | [Programs](./regression/README.md) | let's discover how to build regression models. |   


## Some Technical Useful tips
### Create and Use Virtual Environment
Using an isolated environment such as pip venv or conda makes it possible to install a specific version of scikit-learn with pip or conda and its dependencies independently of any previously installed Python packages. Follow below steps in order to create and activate virtual environment.  
```
# Create virtual environment
python -m venv venv
# Activate virtual environement
venv\Scripts\activate
```

### To install dependencies
```
pip install -r requirements.txt  
python -m pip show scikit-learn  # show scikit-learn version and location
python -m pip freeze             # show all installed packages in the environment
python -c "import sklearn; sklearn.show_versions()"
```

### Start/Stop Jupyter Notebook
```
# Start
jupyter notebook

# Stop
To stop the server, press Ctrl+C in the terminal and confirm with y when prompted.
```

## 🌟 Developer/Contributor
Name: Rohit Shamrao Muneshwar  
Email: rohit.muneshwar1406@gmail.com  
LinkedIn Profile: [Click Here](https://www.linkedin.com/in/rohit-muneshwar-a9079258/)  
Other Github repositories: [Click Here](https://github.com/rohit1406?tab=repositories)  

---