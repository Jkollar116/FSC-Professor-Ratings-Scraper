# Professor Ratings Scraper

A Python script that scrapes course offerings from the Farmingdale State College (FSC) website, retrieves instructor ratings from RateMyProfessor, and updates the HTML file with the fetched ratings.

## Features

- Downloads FSC course offerings HTML content
- Extracts and formats instructor names
- Retrieves instructor ratings from RateMyProfessor
- Updates HTML file with instructor ratings

## Dependencies

The script requires the following Python libraries:

- os
- re
- requests
- shutil
- datetime
- pathlib
- ratemyprofessor

Install the `ratemyprofessor` library using pip:

```bash
pip install ratemyprofessor
```

## Notes

- Tested with Python 3.8 and above
- RateMyProfessor ratings may not be accurate and are subject to change; use as a guide only
- Author: Jkollar116
