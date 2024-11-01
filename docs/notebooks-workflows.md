# Documenting and Styling Analytical Notebooks
This section provides guidelines for structuring analytical notebooks to enhance readability. The guidelines include recommendations for hiding code cells to maintain a clean appearance in Jupyter Book, incorporating references where relevant, and organizing content logically to ensure clarity for readers.

## General Notes
- **Notebook subfolder**. 
As noted in the [Naming and Folder Setup section](/docs/folders-and-naming.md), ensure you create a subfolder within the project’s notebooks folder. This subfolder should be named based on the theme of your assignment, serving as a dedicated space for your notebooks. This practice is especially important, as most Data Lab projects cover multiple topics and involve collaboration among several team members.
- **Notebook Structure**. In all Data Lab projects, we adhere to [this analytics structure](https://github.com/worldbank/sudan-poverty-monitoring/blob/main/docs/2-analytics.md). Ensure that your notebook follows this same structure.
      
- **Adding a README.md** If you look at the recommended notebok structure, it has sections on data used and methodology. In some cases, this information may better presented in a separate markdown file. You can add a ```README.md``` within your notebooks subfolder. This will provide detailed information about data sources and methodology. 
- **Previewing Jupyter Book** As you are aware, the ```_toc.yml``` controls whats rendered in the Jupyter Book. Please edit the file accordinly to add your notebooks and other ```markdown``` files as needed. This will allow you to build the book locally using ```make build``` command and preview and check if your notebooks are rendering as expected. 
- **Removing/hiding cell blocks** All notebooks will be rendered in Jupyter Book. To enhance readability, ensure code cells are hidden or removed using cell tags. In some cases, you may use the hide-input cell tag.


## Other Things to Note
- **Headings**. Jupyter books renders all top level headings as sections in the Table of contents, so make sure to only use ```#``` for the top heading of your notebook.
