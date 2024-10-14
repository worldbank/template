# Project Template

[![CalVer](https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg)](https://calver.org)
[![GitHub Release](https://img.shields.io/github/v/release/worldbank/template)](https://github.com/worldbank/template/releases)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/worldbank/template/main.svg)](https://results.pre-commit.ci/latest/github/worldbank/template/main)

The <span style="color:#3EACAD">template</span> is a standardized, but flexible *project* and *documentation* structure of folders and files for sharing your data science work.

Inspired by [literate programming](http://literateprogramming.com), maintained by the [Development Data Group](https://www.worldbank.org/en/about/unit/unit-dec/dev) and built as [GitHub template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), the <span style="color:#3EACAD">template</span> contains:

- [**README**](README), [**CODE_OF_CONDUCT**](docs/CODE_OF_CONDUCT.md), [**CONTRIBUTING**](docs/CONTRIBUTING.md) templates
    > README files are important and often neglected. The files should inform anyone about the first steps to use, learn and contribute to your project.

- [**CITATION.cff**](CITATION.cff)
  > Embracing [CFF](https://citation-file-format.github.io) aligns with best practices for reproducible research and software development. By adhering to established standards for documenting project dependencies and citations, we demonstrate our commitment to quality, transparency, and integrity in our work.

- [**LICENSE**](LICENSE)
  > The LICENSE is a document that  determines what others can and cannot do with contents of the repository. If no license is present, no one has permission to use and/or modify your code. The <span style="color:#3EACAD">template</span> is licensed under the [**Mozilla Public License**](https://www.mozilla.org/en-US/MPL/). And so will projects generated from it. For further information, see also [this discussion](https://github.com/orgs/worldbank/discussions/4).

- **docs/**

    > Documentation is often never prioritized until last minute. The <span style="color:#3EACAD">template</span> aims to revert the malpractice by setting up the documentation as an integral part, inspired by [literate programming](http://literateprogramming.com). With the power of [Jupyter Book](https://jupyterbook.org), data practitioners have a way to share [Jupyter notebooks](https://jupyter.org) on [GitHub Pages](https://pages.github.com) in a standardized and effortless way.

- [**docs/bibliography.bib**](/docs/bibliography.bib)
    > A `bibliography` using the [BibTeX](https://www.bibtex.org/Format/) format. Use this file to include and cite your project's bibliography. See also [Citations and bibliographies](https://jupyterbook.org/en/stable/content/citations.html).

- **data/**
    > Placeholder folder for data. Data is immutable. By default, the data folder is present but ignored from version control, in order to prevent files of being mistakenly versioned in the code repository.

- **src/**
    > Placeholder folder for source code. If Python, it is recommended the package is made pip-installable.

- **notebooks/**
    > Placeholder folder for [Jupyter notebooks](https://jupyter.org). Markdown files and Jupyter notebooks can be added to `docs/_toc.yml` (Table of Contents) to compose the *documentation*.

- [**.pre-commit-config.yml**](https://github.com/worldbank/template/blob/main/.pre-commit-config.yaml)
    > Using [pre-commit](https://pre-commit.com) offers a significant advantage in streamlining the development process by enforcing code standards and reducing errors before code reaches the review stage or is committed to the repository. It automates the execution of various checks, such as syntax errors, code formatting, and ensuring compliance with coding standards, which saves time and improves code quality.

- [GitHub Actions](https://github.com/features/actions) and [Dependabot](https://docs.github.com/en/code-security/dependabot)
    > [GitHub Actions](https://github.com/features/actions) and [Dependabot](https://docs.github.com/en/code-security/dependabot) are two powerful features provided by [GitHub](https://github.com) to automate and secure software development workflows, making it easier for developers to maintain high-quality and safe codebases.

- [GitHub Issues and Pull Requests GitHub](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
    > GitHub allows to customize how issues and pull requests are presented to the public. Custom templates encourage collaboration and maintainability.

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

```{important}
*With flexibility comes great responsibility*. The <span style="color:#3EACAD">template</span> makes a few opiniated choices for the structure and code/documentation management of a project for what we envision to be most cases. However, even the best of the templates would never be perfect for the universe of cases out there. All in all, the <span style="color:#3EACAD">template</span> aims to encourage teams to start thinking and assimilate **collaborative coding**, **documentation**​, **enginerring**, **reproducibility​** and **best practices** as an integral part of the project. *In a standardized way*.

In this spirit, if the <span style="color:#3EACAD">template</span> is not for you or in case you have feedback, please consider [opening an issue](https://github.com/worldbank/template/issues) or [submitting a pull request](https://github.com/worldbank/template/pulls) to share your ideas and suggestions. Your contributions would be appreciated immensely.
```

## Usage

### Getting Started

```{margin} ✨ Can't see the <span style="color:#3EACAD">template</span> ?
Please ensure you are logged in on [GitHub](https://github.com) and have permissions to create a repository.
```

#### 1. **Create new repository from template**

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

#### 2. **Enable [GitHub Actions](https://github.com/features/actions) and [GitHub Pages](https://pages.github.com)**

After creating the repository from the <span style="color:#3EACAD">template</span>, you will have to enable [GitHub Actions](https://github.com/features/actions) and [GitHub Pages](https://pages.github.com) to allow the [Jupyter Book](https://jupyterbook.org) to be built and published.

To activate the workflow, please enable [GitHub Actions](https://github.com/features/actions) by going to the repository's settings (`Settings > Actions > General`), and selecting **read and write permissions** as shown below.

```{figure} docs/images/github-template-action-enable.png
    ---
    ---
```

To publish, please enable [GitHub Pages](https://pages.github.com) by going to the repository's settings (`Settings > Pages`), and selecting to deploy from the **GitHub Actions** option.

```{figure} docs/images/github-template-pages.png
---
---
```

On the next push to `main`, the [Jupyter Book](https://jupyterbook.org) will be automatically built and published. You can check the progress on the `Actions` tab.

```{figure} docs/images/github-template-action.png
---
---
```

```{caution}
The *documentation* can be published from either *public* and *private* repositories. If publishing private content, please remember to carefully select the content to be made public and to abide by your organization's Data Privacy Policy.
```

#### 3. **Update configurations**

The <span style="color:#3EACAD">template</span> comes with a default `docs/_config.yml` Jupyter Book configuration file. Remember to update it to reflect your project's name and details.

```yaml
repository:
url: https://github.com/worldbank/template
branch: main
```

```{seealso}
[Jupyter Book Configuration Reference](https://jupyterbook.org/en/stable/customize/config.html)
```

#### 4. **Review and update README files**

The <span style="color:#3EACAD">template</span> comes with README files - including [this **README**](README) - that should provide anyone with the information about the first steps to use, learn and contribute to your project. Please **replace** and/or **repurpose** the files with instructions and detailed information about your project.

> - **CODE_OF_CONDUCT**
> - **CONTRIBUTING**
> - **README**
> - Issues and Pull Requests GitHub templates

```{seealso}
[Awesome README](https://github.com/matiassingers/awesome-readme)
```

#### 5. **Choose a license**

The <span style="color:#3EACAD">template</span> is licensed under the [**Mozilla Public License**](https://www.mozilla.org/en-US/MPL). A LICENSE is the document that guarantees the repository can be shared, modified and receive contributions. Otherwise, if no license is present, all rights are reserved.

<hr>

**Congratulations!** You just created a beautiful home for your project. To access your project page, use (and share) the link as shown below.

> 🌟 `https://<your-github-username>.github.io/<your-project-name>`

````{note}
For example, you can view [this live demo](http://worldbank.github.io/template) using the following link:

> 🌟 [Live Demo - worldbank.github.io/template](http://worldbank.github.io/template)

You can also install the latest version directly from the main branch:

```bash
pip install git+https://github.com/worldbank/template
````

### Add content

The <span style="color:#3EACAD">template</span> is created as a [Jupyter Book](https://jupyterbook.org/intro.html) - an open-source project to build beautiful, publication-quality books and documents from computational content. Let's see below how to add, execute and publish new content for your project.

#### Updating the Jupyter Book `_config.yml` metadata

To configure your Jupyter Book for your project, you’ll need to update the `_config.yml` file. This file controls various aspects of the Jupyter Book, including the project title, description, and relevant URLs. Below is a template to update this file to reflect the project’s details.

```yaml
# Book settings
title: <your-project-title>
author: <your-team>

repository:
url: https://github.com/<your-organization>/<your-project>

# Jupyter Book options
execute:
  execute_notebooks: "auto"  #  Automatically execute notebooks during the build process
```

#### Update table of contents

When ready to publish the *documentation* on [GitHub Pages](https://pages.github.com/), all you need to do is edit the [table of contents](https://github.com/worldbank/template/blob/main/docs/_toc.yml) and add and/or update content you would like to display. [Jupyter Book](https://jupyterbook.org) supports content written as [Markdown](https://daringfireball.net/projects/markdown/), [Jupyter](https://jupyter.org) notebooks and [reStructuredText](https://docutils.sourceforge.io/rst.html) files and the `docs/_toc.yml` file controls the [table of contents](https://github.com/worldbank/template/blob/main/docs/_toc.yml) of your book.

The <span style="color:#3EACAD">template</span> comes with the [table of contents](https://github.com/worldbank/template/blob/main/docs/_toc.yml) below as an example.

```yaml

format: jb-book
root: README

parts:

  - caption: Examples
    numbered: True
    chapters:
      - file: notebooks/world-bank-api.ipynb
      - file: notebooks/world-bank-package.ipynb
      - file: notebooks/nasa-apod.ipynb
      - file: notebooks/bibliography.ipynb
```

```{seealso}
[Jupyter Book Structure and organize content](https://jupyterbook.org/en/stable/basics/organize.html)
```

#### Add executable content

[Jupyter Notebooks](https://jupyter.org) can be beautifully rendered and downloaded from your book. By default, the <span style="color:#3EACAD">template</span> will render any files listed on the [table of contents](#update-table-of-contents) that have a notebook structure. The <span style="color:#3EACAD">template</span> comes with a Jupyter notebook example, `notebooks/world-bank-api.ipynb`, to illustrate.

```{important}

By default, Jupyter notebooks are **not** executed. However, you can configure[Jupyter Book](https://jupyterbook.org) to run notebooks during the build process (on GitHub), allowing **code outputs** and **interactive visualizations** to be generated and included in the *documentation* automatically. When enabled, Jupyter notebooks are executed by [GitHub Actions](https://github.com/features/actions) each time a commit is made to the `main` branch. For this to work, it’s crucial to ensure that all necessary [dependencies](##use-pyproject-toml-for-python-package-management) are included in the repository. If you want to prevent a specific notebook from being executed, you can [exclude it from execution](https://jupyterbook.org/en/stable/content/execute.html#exclude-files-from-execution).
```

```{seealso}
[Jupyter Book Write executable content](https://jupyterbook.org/en/stable/content/executable/index.html)
```

#### Distributing Your Project as a Python Package

If your project uses [Python](https://python.org), it’s highly recommended to distribute it as a [package](https://packaging.python.org/en/latest/tutorials/packaging-projects/). By including a `pyproject.toml` file, the packaging process becomes more streamlined - *trust me [things can get intense](https://imgs.xkcd.com/comics/python_environment.png)*.

Additionally:

```{tip}
- Using `pyproject.toml` future-proofs your setup by aligning with modern packaging standards.
- The `pyproject.toml` file acts as a single source of truth for your Python dependencies and project metadata.
- You can combine Conda for system-level dependencies with `pyproject.toml` for Python dependencies, using Conda for environments and pip/poetry for Python packages.
- Any packages in the `src/` folder will be automatically discovered and installed.
```

##### Use `pyproject.toml` for Python Package Management

While the <span style="color:#3EACAD">template</span> recommends using [Conda](https://conda.io/projects/conda/en/latest/index.html) (or [Mamba](https://github.com/mamba-org/mamba)) as the environment manager and managing dependencies through an `environment.yml` file, there is an alternative approach that leverages `pyproject.toml`. This can be particularly advantageous if your project is a Python package or if you want to simplify and standardize the management of Python-specific dependencies.

##### Why use `pyproject.toml`?

The next step is ensure your code is maintainable, reliable and reproducible by including
any dependencies and requirements, such as packages, configurations, secrets (template) and additional instructions.

1. **Standardization**: `pyproject.toml` is a modern, standardized format defined by [PEP 518](https://peps.python.org/pep-0518/) and [PEP 621](https://peps.python.org/pep-0621/) that centralizes project configuration in Python projects, including build requirements and dependencies.

2. **Python Packaging**: If your project is to be distributed as a package, `pyproject.toml` is the preferred way to define build tools (like [hatch](https://hatch.pypa.io/latest/config/dependency/) or [poetry](https://python-poetry.org)) and metadata for your package (like name, version, dependencies, etc.). It allows tools like `pip` and `build` to install and package your project more effectively.

3. **Compatibility with Tools**: The `pyproject.toml` file is compatible with multiple Python packaging and dependency management tools such as `poetry` and `pip`. This allows for smoother integration with CI/CD pipelines, PyPI, and other environments.

4. **Separation of Concerns**: While Conda manages both system-level and Python-specific packages, using `pyproject.toml` helps isolate Python dependencies. This is useful if your project uses primarily Python packages and you want finer control over Python versioning and dependency resolution.

#### Example: Using `pyproject.toml`

This `pyproject.toml` file specifies the dependencies and other metadata for your Python package. You can install these packages using `pip`, ensuring that your Python environment is properly managed. You can still use Conda for system-level packages (such as `libc`, `gdal`, etc.), while using `pyproject.toml` for Python package management.

1. **`pyproject.toml` Example**:

    ```toml
    [build-system]
    requires = ["hatchling>=1.21.0", "hatch-vcs>=0.3.0"]
    build-backend = "hatchling.build"

    [project]
    name = "template"
    description = "A data science project"
    readme = { file = "README.md", content-type = "text/markdown" }
    license = { file = "LICENSE" }
    authors = [
      { name = "Your Name", email = "your.email@example.com" }
    ]
    dynamic = ["version"]

    python = ">=3.9"
    dependencies = [
      "pandas>=1.4.3,<2",
    ]
    [project.optional-dependencies]
    docs = [
        "docutils==0.17.1",
        "jupyter-book>=1,<2",
    ]

    [tool.hatch.build.targets.sdist]
    include = [
        "src/**/*"
    ]

    [tool.hatch.version]
    source = "vcs"
    ```

2. **Keep the Conda Environment for System-level Packages**:
    You can continue to use `environment.yml` to specify non-Python dependencies or packages not available on PyPI, such as `mamba` or `gdal`.

    ```yaml
    channels:
      - conda-forge
    dependencies:
      - python=3.9
      - mamba
      - gdal
    ```

3. **Installation**:
  To create an environment, you would first install the Conda dependencies and then use `pip` to install Python-specific dependencies from `pyproject.toml`. Alternatively, you can skip Conda and use `pip` for the entire setup.

    ```shell
    # Create Conda environment
    conda env create -f environment.yml -n <your-environment-name>

    # Activate the environment
    conda activate <your-environment-name>

    # Install Python dependencies
    pip install .
    ```

  To install a Python package directly from a [GitHub](https://github.com) repository using [pip](https://pip.pypa.io/en/stable/installation/), you can use the command pip install `git+https://github.com/<username>/<repository>.git`. This allows you to install the latest version of the package from the repository. You can also specify a particular branch or release tag by adding `@<branch_or_tag>` at the end of the URL This is particularly useful when you want to access features or fixes that haven’t been published on PyPI yet, or to get the latest updates from the repository.

  If you want to install the latest release, you should specify the tag associated with that release. For instance:

  ```shell
    pip install git+https://github.com/<username>/<repository>.git@<latest_release_tag>
  ```

```{seealso}
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Conda Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
```

#### Building Documentation Locally

To build the documentation locally, please follow these steps:

- Install the package with documentation dependencies:

  ```shell
    pip install -e .[docs]
  ```
  in some environments (e.g., on Mac OS), try this instead to scape the brackets:
   ```shell
    pip install -e .\[docs]\
  ```

- Build the documentation:

  ```shell
   jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml
  ```

The generated documentation will be available in the `_build/html` directory. Open the `index.html` file in a web browser to view it.

## Code of Conduct

The <span style="color:#3EACAD">template</span> maintains a [Code of Conduct](docs/CODE_OF_CONDUCT.md) to ensure an inclusive and respectful environment for everyone. Please adhere to it in all interactions within our community.

## License

The <span style="color:#3EACAD">template</span> is licensed under the [**Mozilla Public License**](https://www.mozilla.org/en-US/MPL). Remember to replace the [license](LICENSE) if necessary. If open source, [choose an open source license](https://choosealicense.com).
