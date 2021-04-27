# Project Template

The template creates a project structure inspired by the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) with an out-of-the-box [Jupyter Book](https://jupyterbook.org/intro.html) published automatically on [GitHub Pages](https://pages.github.com).

In addition, the template creates GitHub [issue templates](https://github.com/datapartnership/template/issues/new/choose) (*e.g*, Bug report and Feature request) on your new repository to encourage collaboration.

```{tip}
Check out the [live demo](https://datapartnership.github.io/template/).
```

## Getting Started

This repository is a [GitHub template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template). Thus, [use this template](https://github.com/worldbank/template/generate) to recreate the same directory structure and files for your project.

The template offers a boilerplate of a [Jupter Book](https://jupyterbook.org/intro.html). When ready to publish, all you need to do is edit the `_toc.yml` that controls the table of contents for your book. Please consult the [documentation](https://jupyterbook.org/customize/toc.html) for more options and parameters.

Make sure to [configure the publishing source](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) as `gh-pages`. On every commit to the `main` branch, your book will be automatically published to [GitHub Pages](https://pages.github.com).

```{important}
Your project's Jupyter Book will be publicly available **DO NOT** include any portion and remember to comply to your organizatin's data policy. 
```

### What's Inside

Following is a suggested project structure inspired by a simplified [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

```markdown
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <  IMPORTANT: Data must not be commited to GitHub
    ├── models             <- Trained and serialized model and model predictions
    ├── notebooks          <- Jupyter notebooks
    ├── references         <- Data dictionaries, manuals, and all explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── _config.yml        <- Jupyter Book configuration  
    ├── _toc.yml           <- Jupyter Book table of contents
    └── requirements.txt   <- The requirements for environment, e.g.
                             generated with `pip freeze > requirements.txt`
```

## Project Checklist

```{caution}
Coming Soon
```

## Learn more

- [The DIME Analytics Data Handbook](https://worldbank.github.io/dime-data-handbook/)
    > This book is intended to serve as an introduction to the primary tasks required in development research, from experimental design to data collection to data analysis to publication. It serves as a companion to the DIME Wiki and is produced by DIME Analytics.

- [GitHub Pages](https://guides.github.com/features/pages/)
    > GitHub Pages are public webpages hosted and easily published through GitHub.

- [Jupyter Book](https://jupyterbook.org/intro.html)
    > Jupyter Book is an open source project for building beautiful, publication-quality books and documents from computational material.

## License

[MIT LICENSE](LICENSE)
