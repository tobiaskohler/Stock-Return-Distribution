# Return Distribution Plotting Tool

A tool that plots the historical return distribution of a given asset.

## Requirements
- yfinance
- plotly
- numpy

## Usage
The tool can be executed through the command line with the following arguments (utilize -h flag to get the following view):

```Bash
-s, --symbol: Asset symbol to plot
-b, --begin: Start date in YYYY-MM-DD format (optional, default is None)
-e, --end: End date in YYYY-MM-DD format (optional, default is None)
```

If the user provides a Start date which doesn't exist, the tool graps the most early date available.

Example:
```Bash
> init.py -s AAPL -b 1950-01-01 -e 2020-01-01
```

![Example - Output (.png and .html available)](/AAPL_return-distribution_1980-12-12-2020-01-01.png)


There is not data available for Apple Stock since 1950, hence automatically adjusted to earliest date (1980-12-12):


## Output
The tool produces a histogram plot of the log returns and saves it in the `output` folder as a .png file and an .html file. If the `output` folder does not exist, it will be created.

The plot shows the frequency of log returns within specified bins. The number of bins is determined using the Freedman-Diaconis rule, which aims to minimize the variance of the estimator and provide a good balance between over- and under-representation of data. The plot is annotated with the asset symbol and the start and end dates.

The user will be prompted to save the plot after it is displayed.

