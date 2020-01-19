From Pandas Profile Github Page they've described it as a package that:

Generates profile reports from a pandas DataFrame. The pandas df.describe() function is great but a little basic for serious exploratory data analysis. pandas_profiling extends the pandas DataFrame with ProfileReport(df, title='') for quick data analysis.

For each column the following statistics - if relevant for the column type - are presented in an interactive HTML report:

- **Essentials:** type, unique values, missing values
- **Quantile statistics** like minimum value, Q1, median, Q3, maximum, range, interquartile range
- **Descriptive statistics** like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
- **Most frequent values**
- **Histogram**
- **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
- **Missing values** matrix, count, heatmap and dendrogram of missing values

Install the pandas profiler by copying and paste the code below on your Anaconda terminal.

`conda install -c conda-forge pandas-profiling`

Or use ``Pip install`` on window terminal.

# NOTE: #

Kindly create a new environemnt to install this package as there might be some dependencies with numpy and pandas versions. By installing the profiler, numpy, pandas, and matplotlib will automatically be installed.  This is because the profiler is built and depends on these packages, so they must be installed for it to work.  If there are any other packages you need to work remeber to instal them on this environment.