import argparse
import ast
from plottingModule import plot_return_hist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot the historical return distribution for a given asset')
    parser.add_argument("-s", "--symbol", type=str, help="Asset symbol to plot")    
    parser.add_argument('-b', '--begin', type=str, help='Start date in YYYY-MM-DD format', default=None)
    parser.add_argument('-e', '--end', type=str, help='End date in YYYY-MM-DD format', default=None)
    parser.add_argument('-l', '--log-scale', type=str, help='Use logarithmic scale on the y-axis (True or False)', default='True')
    args = parser.parse_args()
    log_scale = ast.literal_eval(args.log_scale)
    
    plot_return_hist(args.symbol, args.begin, args.end, log_scale)
