# Project Template

The `template` creates a [project structure](#what-s-inside) with an out-of-the-box documentation with [Jupyter Book](https://jupyterbook.org/intro.html) that can be published automatically on [GitHub Pages](https://pages.github.com). In addition, the `template` configures [issue templates](https://github.com/datapartnership/template/issues/new/choose) (e.g., **Bug report** and **Feature request**) on your new repository to encourage collaboration.

> **See a [live demo](https://datapartnership.github.io/template/).**

## Getting Started

This repository is a [GitHub template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template). Thus, [use this template](https://github.com/worldbank/template/generate) to recreate the same directory structure and files for your project.

### What's Inside

Following is a suggested project structure inspired by a simplified [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

```markdown
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <  Placehodlder. IMPORTANT: Data must not be commited to GitHub
    ├── docs               <- Jupyter Book
        ├── __config.yml   <- Jupyter Book configuration
    │   └── _toc.yml       <- Jupyter Book table of contents
    ├── notebooks          <- Jupyter notebooks
        ├── 00-data.ipynb  <- Jupyter notebook example
        ├── 01-eda.ipynb   <- Jupyter notebook example
        └── 02-train.ipynb <- Jupyter notebook example
    ├── Makefile           <- Makefile with commands like `make docs` or `make data`
    ├── requirements.txt   <- Python requirements
    └── LICENSE
```

### Setting up the documentation with Jupyter Book

The `template` offers a boilerplate of a [Jupyter Book](https://jupyterbook.org/intro.html). When ready to publish, all you need to do is edit the `docs/_toc.yml` that controls the table of contents for your book. Make sure to [configure the publishing source](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) as `gh-pages`.

Voilà! On every commit to the `main` branch, your book will be automatically published to [GitHub Pages](https://pages.github.com). Please consult the [Jupyter Book documentation](https://jupyterbook.org/customize/toc.html) for more options and parameters.

```{important}
Your project's Jupyter Book will be publicly available **DO NOT** include any portion and remember to comply to your organization's data privacy policy.
```

## Additional Resources

- [DIME Analytics Data Handbook](https://worldbank.github.io/dime-data-handbook/)
    > This book is intended to serve as an introduction to the primary tasks required in development research, from experimental design to data collection to data analysis to publication. It serves as a companion to the DIME Wiki and is produced by DIME Analytics.

- [GitHub Pages](https://guides.github.com/features/pages/)
    > GitHub Pages are public webpages hosted and easily published through GitHub.

- [Jupyter Book](https://jupyterbook.org/intro.html)
    > Jupyter Book is an open source project for building beautiful, publication-quality books and documents from computational material.

## License

Remember to include a [license](LICENSE). If open source, [choose an open source license](https://choosealicense.com).
