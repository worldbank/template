# 🚀 Project Template

The `template` is a standardized, but flexible *project* and *documentation* structure of folders and files for sharing your data science work.

Inspired by [literate programming](http://www.literateprogramming.com) and [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) and built as [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), the `template` contains:

- **README**, **CODE_OF_CONDUCT**, **CONTRIBUTING**, **LICENSE**
    > README files are important and often neglected. The files should provide anyone with information about the first steps to use, learn and contribute to your project. Please **repurpose** as required.

- GitHub [Issues and Pull Requests templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
    > GitHub allows to customize how issues and pull requests are presented to the public. Custom templates encourage collaboration and maintainability.

- docs

    > Documentation is often never priotized until last minute. The `template` aims to revert the malpractice by setting up the documentation as an integral part of the code repository. With the power of [Jupyter Book](https://jupyterbook.org), data practioners have a way to share beautifully rendered [Jupyter notebooks](https://jupyter.org) using [GitHub Pages](https://pages.github.com) in a standardized and effortless way.

- data
    > Placeholder folder for data. Data is immutable. By default, the data folder is present but ignored from version control, in order to prevent files of being mistakenly versioned in the code repository.

- notebooks
    > Placeholder folder for [Jupyter notebooks](https://jupyter.org). Markdown files and Jupyter notebooks can be added to `docs/_toc.yml` (Table of Contents) to compose the the *documentation*.

```{important}
Admittedly, even the best of the templates would never be perfect; the `template` aims to encourage teams to start thinking and assimilate **best practices**, **collaborative coding**, **documentation**​, **reproducibility​** as an integral part of the project. *In a standardized way*.

In this spirit, please [open an issue](https://github.com/worldbank/DECAT_Data_Science_Template/issues) or [submit a pull request](https://github.com/worldbank/DECAT_Data_Science_Template/pulls) to share your ideas and suggestions. See [CONTRIBUTING](/CONTRIBUTING).
```

## Getting Started

### Usage

```{margin} ✨ Can't see the repository?
Please ensure you are logged in on [GitHub](https://github.com) and have permissions to create a repository.
```

1. **Create new repository from template**

    The `template` is [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template); in other words, you can generate a new repository with the same files and folders to use as the starting point for your project with a click of a button.

    > 🌟 [Create new repository from **template**](https://github.com/datapartnership/template/generate)

    ```{figure} docs/images/github-template.png
    ---
    ---
    ```

    Now, give your repository a name, choose the **visibility** (Public or Private) and click **Create repository from template**.

    ```{figure} docs/images/github-template-create.png
    ---
    ---
    ```

    Voilà! The repository has been created with the same files and folders of the `template`.

    ```{seealso}
    For additional information, see the [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
    ```

2. **Enable and Publish via [GitHub Pages](https://pages.github.com)**

    After creating the repository from the `template`, the *documentation* will be automatically built as a [Jupyter Book](https://jupyterbook.org) via [GitHub Actions](https://github.com/features/actions) from the `main` branch and deployed to the `gh-pages` branch on every commit.

    ```{figure} docs/images/github-template-action.png
    ---
    ---
    ```

    To publish the *documentation*, please enable [GitHub Pages](https://pages.github.com) by going to the repository's settings (`Settings > Pages`), and selecting to deploy the from `gh-pages` branch.

    ```{figure} docs/images/github-template-pages.png
    ---
    ---
    ```

    ```{tip}
    The *documentation* can be published from either *public* and *private* repositories. If publishing private content, please remember to abide by your organization's Data Privacy Policy.

    ```

3. **Replace or repurpose README and community files**

    The `template` comes with README and community files, including [this **README**](README), to ensure the repository can be legally shared (otherwise, if a repository has no license, all rights are reserved) and to encourage collaboration.

      - **CODE_OF_CONDUCT**
      - **CONTRIBUTING**
      - **LICENSE**
      - **README**
      - GitHub Issues and Pull Requests templates

    Please **replace** or **repurpose** the files with information about your project.

    ```{seealso}
    For additional information and examples, we recommend [Awesome README](https://github.com/matiassingers/awesome-readme)
    ```

Congratulations! You just created a beautiful home for your project. To access (and share) your project page, use the link as it shows below.

> `https://github-username.github.io/project-name`

For example, see the live demo below.

> 🌟 [Live Demo](https://datapartnership.org/template)

### Adding Content

The `template` is created as a [Jupyter Book](https://jupyterbook.org/intro.html) - an open-source project to build beautiful, publication-quality books and documents from computational content.

Let's see below how to add and publish new content for your project.

#### Table of Contents

When ready to publish the *documentation*, all you need to do is to add content and edit the file `docs/_toc.yml` that controls the [table of contents](#table-of-contents) for your book. [Jupyter Book](https://jupyterbook.org) supports [Markdown](https://daringfireball.net/projects/markdown/), [Jupyter](https://jupyter.org) notebooks and [reStructuredText](https://docutils.sourceforge.io/rst.html) files. The `template` comes with a boilerplate [table of contents](#table-of-contents).

```
format: jb-book
root: README

parts:
  - caption: Documentation
    numbered: True
    chapters:
    - file: notebooks/world-bank-api.ipynb
  - caption: Additional Resources
    chapters:
      - url: https://datapartnership.org
        title: Development Data Partnership
      - url: https://www.worldbank.org/en/about/unit/unit-dec
        title: World Bank DEC
      - url: https://www.worldbank.org/en/research/dime
        title: World Bank DIME
```

```{seealso}
[Jupyter Book Structure and organize content](https://jupyterbook.org/en/stable/basics/organize.html)
```

#### Jupyter Notebooks

The `template` comes with an example of Jupyter notebook - `notebooks/world-bank-api.ipynb`.

[Jupyter Book](https://jupyterbook.org) will execute notebooks during the build and display **code outputs** and **interactive visualizations** as part of the *documentation*. By default, the `template` will execute any content files that have a notebook structure listed on the [table of contents](#table-of-contents).

```{important}
Note that **all** Jupyter notebooks will be executed by GitHub Actions during build. In case you would like to ignore any files, you can [exclude files from execution](https://jupyterbook.org/en/stable/content/execute.html#exclude-files-from-execution).
```

```{seealso}
[Jupyter Book Write executable content](https://jupyterbook.org/en/stable/content/executable/index.html)
```

### What's Inside

The following is the `template`'s suggested *project* and *documentation* structure inspired by the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

```markdown
    ├── README.md                 <- The top-level README to get started using this project.
    ├── data                      <- Placehodlder. IMPORTANT: Data must not be commited to GitHub
    ├── docs                      <- Documentation create with Jupyter Book
        ├── _config.yml           <- Jupyter Book configuration
    │   └── _toc.yml              <- Jupyter Book table of contents
    ├── notebooks                 <- Jupyter notebooks
        └── world-bank-api.ipynb  <- Jupyter notebook example
    ├── Makefile                  <- Makefile with commands like `make docs` or `make data`
    ├── requirements.txt          <- Python requirements
    ├── CODE_OF_CONDUCT           <- The top-level CODE_OF_CONDUCT
    ├── CONTRIBUTING              <- The top-level CONTRIBUTING
    └── LICENSE                   <- The project license
```

## Additional Resources

- [DIME Analytics Data Handbook](https://worldbank.github.io/dime-data-handbook/)
    > This book is intended to serve as an introduction to the primary tasks required in development research, from experimental design to data collection to data analysis to publication. It serves as a companion to the DIME Wiki and is produced by DIME Analytics.

## License

The `template` is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). **Remember** to replace the [license](LICENSE) as needed. If open-source, [choose an open source license](https://choosealicense.com).
