Data Science Project Template
==============================

A Data Science Project Template generated from https://drivendata.github.io/cookiecutter-data-science/ and adapted to CRISP-DM workflow

This repo is a template reop, you can find how to create from repo from template repo from here
https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template

Project Organization
------------

```nohighlight
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│   │                     the creator's initials, and a short `-` delimited description, e.g.
│   │                     `1.0-jqp-initial-data-exploration`.
│   │
│   ├── 0_Business Understanding  <- Your understanding of the business problem you are trying to solve
│   ├── 1_Data Understanding <- Your understanding of data, also known as EDA (Explorative Data Analysis)
│   ├── 2_Data Processing <- How to extract/transform/loading data, and any preprocessing you need before you start modeling
│   ├── 3_Modeling     <- Develop your model
│   ├── 4_Evaluation   <- Evaluate your model against benchmark dataset
│   └── 5_Deployment   <- Deplpyment related stuff: for example, model file generation.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


--------

Documentation Deployment
------------
If you'd like to deploy your documentation via [GitHub Pages](https://pages.github.com/), you can do so automatically by navigating in a terminal to your `docs` folder and running `make html`. This will automatically find all of your docstrings and build documentation in `docs/_build/html/`. You can run `make clean` to clean out that directory. Modify your `.rst` files in `docs` to enhance the manual parts of this documentation. Once you are happy with it, you can navigate to Settings in your GitHub repository and set the Source to master/docs.

![demo](https://gecgithub01.walmart.com/raw/nextech/datascience-project-template/autodocs/docs/github_pages.png?token=AAAGOJSTEF6HWWFKIFYLYG264JTK6)

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
