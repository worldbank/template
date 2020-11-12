# Project Template

The template creates a project structure inspired by the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) with an out-of-box [Jupyter Book](https://jupyterbook.org/intro.html) published automatically on [GitHub Pages](https://pages.github.com).

Here are some of the practices that project template aims to encourage:
- Reproducibility
- Transparency
- Credibility

## Resources

- [Development Data Partnership](https://docs.datapartnership.org)
    > A partnership between international organizations and companies, created to facilitate the use of third-party data in research and international development.

- [Awesome Data Partnership](https://datapartnership.github.io/awesome-datapartnership/)
    > A curated list of projects, data goods and derivative works associated with the Development Data Partnership

- [The DIME Wiki](https://dimewiki.worldbank.org/wiki/Main_Page)
    > The DIME Wiki is a public good developed and maintained by DIME Analytics, a team which creates tools that improve the quality of impact evaluation research at DIME. The DIME Wiki is targeted to all researchers and M&E specialists at the World Bank, clients who are managing data collection efforts in the field, donor institutions, universities, NGOs, and governments. While there are many existing impact evaluation resources, none meet the specific gap the DIME Wiki aims to fulfill: a resource focused on practical implementation guidelines rather than theory, open to the public, easily searchable, suitable for users of varying levels of expertise, up-to-date with the latest technological advances in electronic data collection, with a vibrant network of editors who are experts in this field.

- [The DIME Analytics Data Handbook](https://worldbank.github.io/dime-data-handbook/)
    > This book is intended to serve as an introduction to the primary tasks required in development research, from experimental design to data collection to data analysis to publication. It serves as a companion to the DIME Wiki and is produced by DIME Analytics.

- [GitHub Pages](https://guides.github.com/features/pages/)
    > GitHub Pages are public webpages hosted and easily published through GitHub. 

- [Jupyter Book](https://jupyterbook.org/intro.html)
    > Jupyter Book is an open source project for building beautiful, publication-quality books and documents from computational material.

## Project Checklist

```{important}
Coming Soon
```

## Project Organization

```markdown
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
