# Setup

1. Install the Python dependencies via:

```
pip install -r requirements.txt
```

2. Add a `.env` file in the root directory of the repo with the following environment variables:
```
UST_URL
UST_USERNAME
UST_PASSWORD
```

In addition, convert your chosen security questions according to the following examples and add them (along with the corresponding answers) to the environment variables:

"In what city or town was your first job?" -> `IN_WHAT_CITY_OR_TOWN_WAS_YOUR_FIRST_JOB`

3. Run the following to execute the script:

```
python work.py
```
