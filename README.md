# Project Template

The <span style="color:#3EACAD">template</span> is a standardized, but flexible *project* and *documentation* structure of folders and files for sharing your data science work.

Inspired by [literate programming](http://literateprogramming.com), maintained by the [Development Data Group](https://www.worldbank.org/en/about/unit/unit-dec/dev) and built as [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), the <span style="color:#3EACAD">template</span> contains:

- [**README**](README), [**CODE_OF_CONDUCT**](docs/CODE_OF_CONDUCT.md), [**CONTRIBUTING**](CONTRIBUTING.md) templates
    > README files are important and often neglected. The files should inform anyone about the first steps to use, learn and contribute to your project.

- **LICENSE**
  > The LICENSE is a document that  determines what others can and cannot do with contents of the repository. If no license is present, no one has permission to use and/or modify your code. The <span style="color:#3EACAD">template</span> is licensed under the [**Mozilla Public License**](https://www.mozilla.org/en-US/MPL/). And so will projects generated from it.

- **docs/**

    > Documentation is often never priotized until last minute. The <span style="color:#3EACAD">template</span> aims to revert the malpractice by setting up the documentation as an integral part, inspired by [literate programming](http://literateprogramming.com). With the power of [Jupyter Book](https://jupyterbook.org), data practioners have a way to share [Jupyter notebooks](https://jupyter.org) on [GitHub Pages](https://pages.github.com) in a standardized and effortless way.

- **docs/bibliography.bib**
    > A `bibliography` using the [BibTeX](https://www.bibtex.org/Format/) format.

- **data/**
    > Placeholder folder for data. Data is immutable. By default, the data folder is present but ignored from version control, in order to prevent files of being mistakenly versioned in the code repository.

- **src/**
    > Placeholder folder for source code. If Python, it is recommended the package is made pip-installable.

- **notebooks/**
    > Placeholder folder for [Jupyter notebooks](https://jupyter.org). Markdown files and Jupyter notebooks can be added to `docs/_toc.yml` (Table of Contents) to compose the *documentation*.

- [Issues and Pull Requests GitHub templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
    > GitHub allows to customize how issues and pull requests are presented to the public. Custom templates encourage collaboration and maintainability.

```{important}
*With flexibility comes great responsibility*. The <span style="color:#3EACAD">template</span> makes a few opiniated choices for the structure and code/documentation management of a project for what we envision to be most cases. However, even the best of the templates would never be perfect for the universe of cases out there. All in all, the <span style="color:#3EACAD">template</span> aims to encourage teams to start thinking and assimilate **collaborative coding**, **documentation**​, **enginerring**, **reproducibility​** and **best practices** as an integral part of the project. *In a standardized way*.

In this spirit, if the <span style="color:#3EACAD">template</span> is not for you or in case you have feedback, please consider [opening an issue](https://github.com/worldbank/template/issues) or [submitting a pull request](https://github.com/worldbank/template/pulls) to share your ideas and suggestions. Your contributions would be appreciated immensely.
```

## Benefits

Project templates on GitHub are essential for streamlining the data science and collaboration processes, and they offer several key benefits:

- 🛠️ **Consistency and Best Practices:** Project templates encourage consistency in project structure, coding standards, and best practices. They provide a standardized starting point, ensuring that all team members follow the same guidelines and reduce the risk of introducing errors.

- ⏳ **Time and Effort Savings:** Templates save time by eliminating the need to set up a project from scratch. Developers can quickly start working on their projects without the overhead of configuring the initial project structure, dependencies, or workflows.

- 🚀 **Faster Onboarding:** New team members or contributors can easily get up to speed by using project templates. It simplifies the onboarding process, allowing them to understand the project structure and development practices more quickly.

- 🎨 **Customization and Adaptability:** GitHub project templates can be customized to suit the specific needs of different types of projects or organizations. They serve as a foundation that can be adapted to meet unique requirements.

- 🤝 **Community Engagement:** Open-source projects can attract more contributors when they provide accessible project templates. These templates facilitate contributions by reducing the barriers to entry for potential collaborators.

- 🔄 **Version Control Integration:**  GitHub project templates are tightly integrated with Git version control. This makes it easier to manage changes, collaborate, and track the history of project configurations.

- 📖 **Documentation and Guidance:** Templates often include documentation and guidance to help developers understand the project's structure and how to get started. This can include README files, code comments, and links to relevant resources.

- 🔍 **Discoverability:** Templates are discoverable on GitHub, making it easy for developers to find and use project templates for their preferred programming languages, frameworks, and tools. This helps build a supportive ecosystem.

- ✍️ **Continual Improvement:** Project templates can evolve and improve over time as best practices, technology, and requirements change. This ensures that projects remain up to date and maintainable.

In summary, GitHub project templates are valuable resources that enhance project management, development practices, and collaboration. They promote consistency, efficiency, and quality in software development, whether for individual projects, open-source contributions, or within organizational contexts.

## Usage

### Getting Started

```{margin} ✨ Can't see the <span style="color:#3EACAD">template</span> ?
Please ensure you are logged in on [GitHub](https://github.com) and have permissions to create a repository.
```

1. **Create new repository from template**

    The <span style="color:#3EACAD">template</span> is a [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template); in other words, you can generate a new GitHub repository with the same files and folders to use as the starting point for your project.

    > 🌟 [Create new repository from **template**](https://github.com/worldbank/template/generate)

    ```{figure} docs/images/github-template.png
    ---
    ---
    ```

    Now, give your repository a name, choose the **visibility** (Public or Private) and click **Create repository from template**.

    ```{figure} docs/images/github-template-create.png
    ---
    ---
    ```

    *Voilà!* The repository has been created with the same files and folders of the <span style="color:#3EACAD">template</span>.

    ```{seealso}
    For additional information, see the [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
    ```

2. **Enable [GitHub Actions](https://github.com/features/actions) and [GitHub Pages](https://pages.github.com)**

    After creating the repository from the <span style="color:#3EACAD">template</span>, you will have to enable [GitHub Actions](https://github.com/features/actions) and [GitHub Pages](https://pages.github.com) to allow the [Jupyter Book](https://jupyterbook.org) to be built and published.

    To activate the workflow, please enable [GitHub Actions](https://github.com/features/actions) by going to the repository's settings (`Settings > Actions > General`), and selecting **read and write permissions** as shown below.

    ```{figure} docs/images/github-template-action-enable.png
      ---
      ---
    ```

    To publish, please enable [GitHub Pages](https://pages.github.com) by going to the repository's settings (`Settings > Pages`), and selecting to deploy from the `gh-pages` branch.

    ```{figure} docs/images/github-template-pages.png
    ---
    ---
    ```

    On the next push to `main`, the [Jupyter Book](https://jupyterbook.org) will be automatically built and published. You can check the progress on the  `Actions` tab.

    ```{figure} docs/images/github-template-action.png
    ---
    ---
    ```

    ```{caution}
    The *documentation* can be published from either *public* and *private* repositories. If publishing private content, please remember to carefully select the content to be made public and to abide by your organization's Data Privacy Policy.
    ```

3. **Update configurations**

    The <span style="color:#3EACAD">template</span> comes with a default `docs/_config.yml` Jupyter Book configuration file. Remember to update it to reflect your project's name and details.

      ```
      repository:
      url: https://github.com/worldbank/template
      branch: main
      ```

   ```{seealso}
    [Jupyter Book Configuration Reference](https://jupyterbook.org/en/stable/customize/config.html)
    ```

4. **Review and update README files**

    The <span style="color:#3EACAD">template</span> comes with README files - including [this **README**](README) - that should provide anyone with the information about the first steps to use, learn and contribute to your project. Please **replace** and/or **repurpose** the files with instructions and detailed information about your project.

    > - **CODE_OF_CONDUCT**
    > - **CONTRIBUTING**
    > - **README**
    > - Issues and Pull Requests GitHub templates

    ```{seealso}
    [Awesome README](https://github.com/matiassingers/awesome-readme)
    ```

5. **Choose a license**

    The <span style="color:#3EACAD">template</span> is licensed under the [**World Bank Master Community License Agreement**](LICENSE). A LICENSE is the document that guarantees the repository can be shared, modified and receive contributions. Otherwise, if no license is present, all rights are reserved.

<hr>

**Congratulations!** You just created a beautiful home for your project. To access your project page, use (and share) the link as shown below.

> 🌟 `https://<your-github-username>.github.io/<your-project-name>`

For example, see this <span style="color:#3EACAD">template</span> as a live demo.

> 🌟 [worldbank.github.io/template](http://worldbank.github.io/template) (Live Demo)

### Adding Content

The <span style="color:#3EACAD">template</span> is created as a [Jupyter Book](https://jupyterbook.org/intro.html) - an open-source project to build beautiful, publication-quality books and documents from computational content. Let's see below how to add, execute and publish new content for your project.

#### Table of Contents

When ready to publish the *documentation* on [GitHub Pages](https://pages.github.com/), all you need to do is edit the [table of contents](#table-of-contents) and add and/or update content you would like to display. [Jupyter Book](https://jupyterbook.org) supports content written as [Markdown](https://daringfireball.net/projects/markdown/), [Jupyter](https://jupyter.org) notebooks and [reStructuredText](https://docutils.sourceforge.io/rst.html) files and the `docs/_toc.yml` file controls the [table of contents](#table-of-contents) of your book.

The <span style="color:#3EACAD">template</span> comes with the [table of contents](#table-of-contents) below as an example.

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
  - url: <https://datapartnership.org>
        title: Development Data Partnership
  - url: <https://www.worldbank.org/en/about/unit/unit-dec>
        title: World Bank DEC
  - url: <https://www.worldbank.org/en/research/dime>
        title: World Bank DIME

```

```{seealso}
[Jupyter Book Structure and organize content](https://jupyterbook.org/en/stable/basics/organize.html)
```

#### Dependencies

The next step is ensure your code is maintainable, realiable and reproducible by including
any dependencies and requirements, such as packages, configurations, secrets (template) and addtional instructions.

The <span style="color:#3EACAD">template</span> suggests to use [conda](https://docs.conda.io/) (or [mamba](https://mamba.readthedocs.io/en/latest/)) as environment manager and, as [conventional](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), the environment is controlled by the `environment.yml` file.

The `environment.yml` file is where you specify any packages available on the [Anaconda repository](https://anaconda.org) as well as from the Anaconda Cloud (including [conda-forge](https://conda-forge.org)) to install for your project. Ensure to include the pinned version of packages required by your project (including by Jupyter notebooks).

```
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - bokeh=2.4.3
  - pandas=1.4.3
  - pip:
    - requests==2.28.1
```

To (re)create the environment on your installation of [conda](https://conda.io) via [anaconda](https://docs.anaconda.com/anaconda/install/), [miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/) or preferably [miniforge](https://github.com/conda-forge/miniforge), you only need to pass the `environment.yml` file, which will install requirements and guarantee that whoever uses your code has the necessary packages (and correct versions). By default, the <span style="color:#3EACAD">template</span> uses [Python 3.9](https://www.python.org).

```
conda env create -n <your-environment-name> -f environment.yml
```

In case your project uses Python, it is *strongly* recommended to distribute it as a [package](https://packaging.python.org/).

```{important}
The <span style="color:#3EACAD">template</span> contains an example - the [datalab](https://github.com/worldbank/template/tree/main/src/datalab) Python package - and will automatically find and install any `src` packages as long as `pyproject.yml` is kept up-to-date.
```

```{seealso}
[Conda Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

#### Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org) can be beautifully rendered and downloaded from your book. By default, the <span style="color:#3EACAD">template</span> will render any files listed on the [table of contents](#table-of-contents) that have a notebook structure. The <span style="color:#3EACAD">template</span> comes with a Jupyter notebook example, `notebooks/world-bank-api.ipynb`, to illustrate.

```{important}
Optionally, [Jupyter Book](https://jupyterbook.org) can execute notebooks during the build (on GitHub) and display **code outputs** and **interactive visualizations** as part of the *documentation* on the fly. In this case, Jupyter notebooks will be executed by [GitHub Actions](https://github.com/features/actions) during build on each commit to the `main` branch. Thus, it is important to include all [requirements and dependencies](#dependencies) in the repository. In case you would like to ignore a notebook, you can [exclude files from execution](https://jupyterbook.org/en/stable/content/execute.html#exclude-files-from-execution).
```

```{seealso}
[Jupyter Book Write executable content](https://jupyterbook.org/en/stable/content/executable/index.html)
```

## Code of Conduct

The <span style="color:#3EACAD">template</span> maintains a [Code of Conduct](docs/CODE_OF_CONDUCT.md) to ensure an inclusive and respectful environment for everyone. Please adhere to it in all interactions within our community.

## License

The <span style="color:#3EACAD">template</span> is licensed under the [**Mozilla Public License**](https://www.mozilla.org/en-US/MPL). Remember to replace the [license](LICENSE) if necessary. If open source, [choose an open source license](https://choosealicense.com).
