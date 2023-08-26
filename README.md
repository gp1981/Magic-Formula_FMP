# Magic Formula FMP
This repository provides functionality to analyze financial data and rank companies based on the principles outlined in the book "The Little Book that Still Beats the Market" by J. Greenblatt. The system utilizes data from the Finnhub API to analyze and rank stocks based on specific criteria.

The purpose of this project is for educational purposes only. The code provided here is not intended as financial advice and should be used at your own risk.

## Disclaimer

This library is developed independently and is not affiliated with financialmodelingprep.com nor with magicformula.com or other organizations. The use of this library and any investment decisions made based on the analysis performed are the sole responsibility of the user. We take no responsibility for any risks or losses associated with the use of this library or investments made using the provided data.

## Usage

To use this library, follow these steps:

1. Get an API key from financialmodelingprep.com.
2. Clone this repository to your local machine.
3. Install dependencies including pandas
4. Create a `.env` file in the root directory of the project and add the following line, replacing `*your-api-key*` with your actual API key:

   ```plaintext
   API_KEY=*your-api-key*

5. Modify the code in main.py according to your requirements.
6. Run the main.py script to analyze the financial data and generate rankings.

## Files
The library consists of the following files:

| File | Description |
| ----------- | ----------- |
| main.ipynb | Main script for analyzing financial data | 
| Functions/api.py | Functions for interacting with the API |
| Functions/utils.py |Utility functions|
| Functions/analysis.py | Analysis functions for stock ranking |

### Commit Descriptions
When making commits to the repository, please follow these guidelines for writing descriptive commit messages:

- **Feat**: Use this prefix for new features or enhancements to existing functionality.
- **Fix**: Use this prefix for bug fixes or resolving issues.
- **Docs**: Use this prefix for documentation updates or improvements.
- **refactor** : Use this prefix for code refactoring or restructuring without changing functionality.
- **test** : Use this prefix for adding or modifying test cases.
Please provide a clear and concise description of the changes made in the commit message.

### Branch Naming
When creating branches, please use descriptive names that indicate the purpose or functionality of the branch. Some common branch naming conventions include:

- *Feature*-*branch-name*: Use this prefix for branches that add new features or enhancements.
- *Bugfix*-*branch-name*: Use this prefix for branches that fix bugs or resolve issues.
- *Refactor*-*branch-name*: Use this prefix for branches that involve code refactoring 
- *docs*-*branch-name*: Use this prefix for branches that involve documentation updates or improvements.
Choose a branch name that clearly represents the purpose of the branch and provides context to other contributors.
