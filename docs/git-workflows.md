# Guidelines for Git and GitHub Workflows
This section provides essential guidelines for using Git and GitHub effectively, ensuring a structured and collaborative workflow for all team members in a project.  By following these practices—such as consistently ignoring the "data" folder to protect sensitive information, avoiding direct pushes to the main branch, creating descriptive branch names, and submitting pull requests once work on a branch is complete—we can maintain a clean, organized codebase and promote efficient collaboration. These guidelines help uphold version control best practices, streamline teamwork, and reduce the potential for errors in project repositories.

## Branch Names and Other General Practices
- **Branch names**. After joining the project and cloning the repository, create a concise, descriptive branch name for your work and ensure you switch to that branch before beginning any work on your machine.
- **Update branches**. Avoid creating new update branches; instead, push your changes and resolve any conflicts directly. For instance, if bots in the repository modify your code (e.g., adjusting indentations), simply pull these changes before pushing your own updates.
- **Pull requests (PR)**. When you believe your changes are final, create a pull request and assign the project lead as the reviewer.  

## Folders and Files to Ignore
As all data science repos in the Data Lab use this template, the project repo will come with ```.ignore``` file prepopulated with most files and folders which need to be ignored. However, once you join the project and create your own branch. You will have to make sure that the following folders are being ignored.

- Data folder
- Virtual environments (```.venv```)
- Environment (```.env```)
Feel free to add any other files (e.g., system files specific to your OS) to the ```.gitignore```