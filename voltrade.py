from volatility import volest
import yfinance as yf

# data
symbol = 'JPM'
bench = 'SPY'
estimator = 'GarmanKlass'

# estimator windows
window = 30
windows = [30, 60, 90, 120]
quantiles = [0.25, 0.75]
bins = 100
normed = True

# use the yahoo helper to correctly format data from finance.yahoo.com
jpm_price_data = yf.Ticker(symbol).history(period="5y")
jpm_price_data.symbol = symbol
spx_price_data = yf.Ticker(bench).history(period="5y")
spx_price_data.symbol = bench

# initialize class
vol = volest.VolatilityEstimator(
    price_data=jpm_price_data,
    estimator=estimator,
    bench_data=spx_price_data
)

# call plt.show() on any of the below...
_, plt = vol.cones(windows=windows, quantiles=quantiles)
_, plt = vol.rolling_quantiles(window=window, quantiles=quantiles)
_, plt = vol.rolling_extremes(window=window)
_, plt = vol.rolling_descriptives(window=window)
# _, plt = vol.histogram(window=window, bins=bins, normed=normed)

_, plt = vol.benchmark_compare(window=window)
_, plt = vol.benchmark_correlation(window=window)
plt.show()

# ... or create a pdf term sheet with all metrics in term-sheets/
"""
vol.term_sheet(
    window,
    windows,
    quantiles,
    bins,
    normed
)
"""
