# Setup

Add the following environment variables under your Github Repo's "Settings" -> "Secrets":

```
UST_URL
UST_USERNAME
UST_PASSWORD
```

In addition, convert your chosen security questions according to the following examples and add them (along with the corresponding answers) to the environment variables:

"In what city or town was your first job?" -> `IN_WHAT_CITY_OR_TOWN_WAS_YOUR_FIRST_JOB`

Voila! Once this is set up as a Github Action, it runs every Friday at 7PM UTC, or 12PM PST.
