# Folder Structure and Naming Conventions for Project Setup

Establishing a clear and consistent folder structure with standardized naming conventions is essential for efficient project setup and collaboration. This guide outlines best practices for organizing files and directories, helping team members quickly understand the layout, find key resources, and maintain consistency across projects.

Following these conventions will not only improve productivity but also ensure that new team members can easily navigate projects, reducing the learning curve and minimizing errors. These practices are designed to adapt to the needs of our data science workflows while maintaining flexibility for project-specific requirements.

## Data Science Project Folder Setup
Our data science project folder setup follows [this standardized GitHub template](https://github.com/worldbank/template), ensuring consistency and streamlined collaboration across projects. This template provides a well-organized structure with predefined folders for data, notebooks, src,  and docs. Please navigate to the template, read and understand the template and its philosophy.
- **data**. This folder holds all the data utilized in the project. When appropriate, we recommend distinguishing between ```raw-data```, which serves as input for data analysis processes, and ```derived-datasets```, which are outputs generated after analysis. Additionally, within this ```data``` folder, we suggest organizing datasets by thematic folders. For example, folders could be named: conflict, admin-boundaries, population, and so forth.
- **notebooks**.This folder contains all Jupyter notebooks for the project. As noted above, create subfolders within this directory with descriptive names, such as agriculture, conflict, etc., to improve organization. If your notebooks output datasets, ensure these are saved in the derived-data folder rather than within the notebooks folder. Also, note that scripts (e.g., Python ```.py``` files) belong in the ```src``` folder.
- **docs**. The docs folder primarily holds documentation used for building Jupyter Books. However, any other relevant project documentation can also be placed in this folder.
- **src**. Data processing scripts such as Python scripts sit here. Please refer to documentation on [the standardized GitHub template](https://github.com/worldbank/template) for futher details.

## Naming Conventions
since there are many things which can be named, here provide general guidelines.
- **Lower case Vs. Upper Case.** Please use all lower cases instead of Camel case or other variations.
- **Underscore Vs. hyphen.** Except for cases where use of hyphen is not allowed (e.g., Python script names), all folder and file names should be separated by hyphen. For example, ```damage-assessment``` as opposed to ```DamageAssessment``` or ```Damage-Assessment```.
- **Theme based naming.** As much as possible, ensure names are informative and match with topic/theme. For example, in the data folder, one can have directory for ```admin-boundaries```
