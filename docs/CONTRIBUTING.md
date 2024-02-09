# CONTRIBUTING

Thank you for considering contributing to this project! Your involvement helps improve the overall quality and functionality of the project and its codebase. Please take a moment to review the following guidelines to ensure a collaborative contribution process.

## Code of Conduct

Please note that we have a [Code of Conduct](CODE_OF_CONDUCT.md) in place. We expect all contributors to adhere to it, both in interactions within this project and in interactions with other project members to promote a welcoming and inclusive environment for everyone.

## How Can I Contribute?

There are several ways you can contribute to this project:

- **🐞 Bug Reports:** If you encounter a bug or unexpected behavior, please open an issue on GitHub. Be sure to include as much detail as possible to help us identify and fix the problem.

- **✨ Feature Requests**: If you have an idea for a new feature or enhancement, please open an issue on GitHub. Describe the feature and its use case in detail.

- **📣 Community Engagement:** Ask questions, help other contributors and engage with the community on our [Discussions](https://github.com/orgs/worldbank/discussions).

- **📖 Documentation Feedback:** If you find any errors or have suggestions for improving our documentation, you can report the issue on GitHub.

- **🏗️ Pull Requests (PR):** If you'd like to contribute code or documentation changes, we encourage you to submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

## Contributing to the Code and Documentation

Whether you are novice and expert, your contribution is valuable. If you're contributing code, we recommend getting started with [GitHub Guides](https://github.com/git-guides), [GitHub Skills](https://skills.github.com/), [GitHub Desktop](https://desktop.github.com) and/or [GitHub Docs](https://docs.github.com/en/get-started). In special, see also [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests). When ready, you may follow these guidelines:

1. **[Fork the Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)**: Click the "Fork" button on the top-right corner of this repository on GitHub. This will create a copy of the project in your GitHub account. Then, clone or download this repository to your local machine. Then, navigate to the root directory of the repository.

2. **[Create a Branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository):** Create a new branch for your feature or bug fix. Use a clear and descriptive name for your branch, like `feature/new-feature`.

3. **Code Review and Changes:** Make your code changes and ensure they adhere to our coding standards.

4. **Test:** Ensure that your changes do not break existing functionality.

5. **[Commit and Push](https://github.com/git-guides/git-commit):** Commit your changes with a clear and concise commit message. Reference any related issues or pull requests in your commit message. Push your branch to your forked repository on GitHub.

6. **[Create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request):** Open a pull request against the main branch of this repository. Provide a clear description of your changes and reference any relevant issues. Your PR will be reviewed by maintainers.

7. **[Review and Iterate](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review):** Expect feedback and be prepared to make additional changes if necessary. We may request changes, and once everything looks good, your PR will be merged.

### Cloning the Repository Locally

[Cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository), in the context of version control systems like [Git](https://git-scm.com), refers to the process of creating a copy of a repository from a remote location (such as a [GitHub](https://github.com) repository) onto your local machine. When you clone a repository, you replicate all of its files, folders, commit history, and branches onto your local system. This allows you to work on the project's codebase locally, make changes, create new branches, and contribute to the project without affecting the original repository.

To clone a repository, you'll need the repository's URL and a Git client installed on your computer. First, open your [Git](https://git-scm.com) client of choice, such as [GitHub Desktop](https://desktop.github.com) or [GitKraken](https://www.gitkraken.com). Then, locate the option to clone a repository. In most [Git](https://git-scm.com) clients, this option is typically found under the "File" or "Repository" menu. Next, paste the URL of the repository you want to clone into the designated field. This URL can usually be found on the repository's [GitHub](https://github.com) page by clicking the green "Code" button and copying the URL provided. Once you've pasted the URL, choose the local directory where you want to save the cloned repository on your computer. Finally, initiate the cloning process by clicking the "Clone" button. The [Git](https://git-scm.com) client will then download a copy of the repository to your local machine, allowing you to work on the files locally and collaborate with others on the project.

Alternatively, with you're using [Git CLI](https://git-scm.com/downloads), please follow the step below:

  ```shell
  git clone https://github.com/PATH-TO/REPOSITORY
  ```

### Running Notebooks Locally

This repository provides a Conda/Mamba environment configuration to ensure consistent dependencies across different environments. [Conda](https://docs.conda.io)/[Mamba](https://mamba.readthedocs.io) are prevalent (interoperable) package managers. If haven't installed either, you may follow the installation instructions on the respective documentation.

To run the notebooks locally, after (1) and (2) above, please follow these steps:

- Create (or update) the environment:

  ```shell
  mamba env create -f notebooks/environment.yml
  ```

  This command will create a new environment based on the specifications provided in the `environment.yml` file.

- [Activate the environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment), run [JupyterLab](https://jupyterlab.readthedocs.io) and execute `notebooks`:

  ```shell
    jupyterlab
  ```

### Building Documentation Locally

To build the documentation locally, after (1) and (2) above, please follow these steps:

- Install the documentation dependencies:

  ```shell
    pip install -r docs/requirements.txt
  ```

- Build the documentation:

  ```shell
    jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml
  ```

The generated documentation will be available in the `_build/html` directory. Open the `index.html` file in a web browser to view it.

## Licensing

By contributing to this project, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE).
