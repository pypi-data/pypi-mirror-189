# pysentimentanalyzer [![codecov](https://codecov.io/gh/UBC-MDS/py-sentimentanalyzer/branch/main/graph/badge.svg?token=OwGoN7xkT8)](https://codecov.io/gh/UBC-MDS/py-sentimentanalyzer) [![Documentation Status](https://readthedocs.org/projects/py-sentimentanalyzer/badge/?version=latest)](https://py-sentimentanalyzer.readthedocs.io/en/latest/?badge=latest)



This package performs sentiment analysis on the given texts and summarizes information from the text.

When a survey asks for written comments, it is often tedious to read through every response to extract useful information or just to get a quick summary.
By using this package, responses can be quickly summarized to get a general idea of the sentiments of the comments, which can be useful such as when a PR
team wants to know the overall sentiment on a company or when instructors want to know the overall sentiment on a course. The goal is to provide a quick
summary that is easily interpretable by combining results from a pre-trained Python natural language processing package with the use of visualizations.

## Installation

Ensure that your python version is <=3.9.
To install the package, run the following.
```bash
pip install pysentimentanalyzer
```

## Usage

This package provides the following 4 functions:

* `generate_wordcloud` - Create a wordcloud of the most common positive and negative words.
* `aggregate_sentiment_score` - Calculates the overall sentiment score of the input texts.
* `convert_to_likert` - Converts the sentiment score to a likert scale ranging from 1-5.
* `sentiment_score_plot` - Creates a binned histogram showing count of reviews against the sentiment score.

All functions take a Pandas DataFrame and string of the column name containing the texts as arguments.

See below for an example of how to use the package.

```
import pandas as pd
from pysentimentanalyzer.generate_wordcloud import *
from pysentimentanalyzer.get_aggregated_sentiment_score import *
from pysentimentanalyzer.likert_scale import *
from pysentimentanalyzer.sentiment_score_plot import *

df = pd.read_csv("test_tweets.csv") # assuming the csv exists in the current directory
df = df.head(200)       
```

```
aggregate_sentiment_score(df, "text")
>>> -0.143
```

```
convert_to_likert(df, "text")
>>> ('neutral', 3)
```

```
sentiment_score_plot(df, "text")
```
![histogram](img/histogram_output.png)

```
wordcloud_list = generate_wordcloud(df, "text")
wordcloud_list[0]
```
![wordcloud](img/wordcloud_output.png)

## Similar Packages

While there exists many packages and libraries for sentiment analysis and many projects built on top of those packages, we could not find specific packages that combines the use of sentiment analysis with visualizations. However, we expect there to be many projects done by individuals that likely perform similar functions by making use of existing NLP packages. Our package aims enhance the existing NLP packages by providing a quick and simple way to generate summary visualizations.
Some Python packages that perform sentiment analysis include:

* [spaCy](https://spacy.io/)
* [VADER](https://github.com/cjhutto/vaderSentiment)

## Contributing

This package was created by Group 8 of the DSCI 524 course with members Eric Tsai, Ranjit Sundaramurthi, Tanmay Agarwal and Ziyi Chen. Nonetheless, we welcome suggestions and improvements. See below for further details.

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`pysentimentanalyzer` was created by Eric Tsai, Ranjit Sundaramurthi, Tanmay Agarwal and Ziyi Chen. It is licensed under the terms of the MIT license.

## Credits

`pysentimentanalyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
