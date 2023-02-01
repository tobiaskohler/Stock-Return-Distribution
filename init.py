import argparse
from plottingModule import plot_return_hist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the historical return distribution for a given asset')
    parser.add_argument("-s", "--symbol", type=str, help="Asset symbol to plot")    
    parser.add_argument('-b', '--begin', type=str, help='Start date in YYYY-MM-DD format', default=None)
    parser.add_argument('-e', '--end', type=str, help='End date in YYYY-MM-DD format', default=None)
    args = parser.parse_args()
    
    plot_return_hist(args.symbol, args.begin, args.end)
