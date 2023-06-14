# Professor Ratings Scraper

A Python script that scrapes course offerings from the Farmingdale State College (FSC) website, retrieves instructor ratings from RateMyProfessor, and updates the HTML file with the fetched ratings.

## Features

- Downloads FSC course offerings HTML content
- Extracts and formats instructor names
- Retrieves instructor ratings from RateMyProfessor
- Updates HTML file with instructor ratings
- Uploads updated HTML file to an S3 bucket

## Dependencies

The script requires the following Python libraries:

- os
- re
- requests
- shutil
- datetime
- pathlib
- ratemyprofessor
- boto3

Install the `ratemyprofessor` library using pip:

```bash
pip install ratemyprofessor
```

Install the `boto3` library using pip:

```bash
pip install boto3
```

## Notes

- Tested with Python 3.8 and above
- RateMyProfessor ratings may not be accurate and are subject to change; use as a guide only
- You need to configure AWS credentials (e.g., access_key_id, secret_access_key) for the `boto3` library to work
- Author: Jkollar116
- Check out the updated HTML file with the professor ratings at [https://fscratedschedule.com/](https://fscratedschedule.com/)

                              Before                                                            After
 <img width="500" alt="Screenshot 2023-06-14 143351" src="https://github.com/Jkollar116/FSC-Professor-Ratings-Scraper/assets/77344875/249a2f16-0d9a-4cea-8ad3-bd65e563ab43">              
<img width="500" alt="Screenshot 2023-06-14 143329" src="https://github.com/Jkollar116/FSC-Professor-Ratings-Scraper/assets/77344875/193516b8-d8f9-4e8a-a96b-c86e630e327f">


