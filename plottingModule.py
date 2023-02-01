import yfinance as yf
import plotly.express as px
import plotly.subplots as sp
import numpy as np
import plotly.graph_objects as go 
import math
import os
import traceback

def plot_return_hist(symbol, start, end):
    
    """
    Plots the histogram of log returns for a given stock symbol between a specified start and end date. 
    The function uses yfinance and plotly libraries to retrieve stock information and create a histogram. 
    The number of bins for the histogram is determined using the optimal bin size formula.
    The user is prompted to save the histogram as a PNG and HTML file in a new folder named "output".
    If there is any error, an error message is returned.

    Inputs:
    - symbol (str): A string representing the stock symbol.
    - start (str): A string representing the start date in the format "YYYY-MM-DD".
    - end (str): A string representing the end date in the format "YYYY-MM-DD".

    Outputs:
    - A plotly histogram showing the distribution of log returns.
    - The histogram is saved as a PNG and HTML file in the "output" folder if the user chooses to save it.
    - In case of any error, an error message is returned.

    Returns:
        pd.df: A pandas dataframe containing the stock information.
        str: In case of any errors, an error message is returned.
    """
    
    try: 
        ticker = yf.Ticker(symbol)
        
        df = ticker.history(start=start, end=end)
        df.dropna(inplace=True)

        df["log_returns"] = np.log(df["Close"]) - np.log(df["Close"].shift(1))
        first_date = df.index[0].strftime("%Y-%m-%d")

        optimal_bin_size = f'{round(1 + 3.322 * math.log(len(df["log_returns"])) * 2,0):g}'
        print(optimal_bin_size)
        
        
        fig = px.histogram(df, x="log_returns", nbins=int(optimal_bin_size))
        fig.update_layout(xaxis_title="Log Returns", yaxis_title="Frequency", xaxis_tickformat = '.2%', template='plotly_white', width=600, height=600, title_x=0.5)
        fig.update_traces(marker=dict(line=dict(color='black', width=0.5)))
        fig.update_layout(
        title=go.layout.Title(
            text=f"<b>{symbol} Return Distribution</b><br><sup>{first_date}/{end}</sup>",
            xref="paper",
            x=0.5
        )
        )
            
        fig.show()
        
        save = input("Save graph to the current folder? (y/n)")

        if save.lower() == 'y':
            
            folder_name = "output"
            save_dir = os.path.isdir(folder_name)
            current_dir = os.getcwd()

            if not save_dir:
                os.makedirs(folder_name)
                
            fig.write_image(f"{current_dir}/{folder_name}/{symbol}_return-distribution_{first_date}-{end}.png")
            fig.write_html(f"{current_dir}/{folder_name}/{symbol}_return-distribution_{first_date}-{end}.html")
            print(f"Image saved to {current_dir}/{folder_name}.")
            
        return df
    
    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg


if __name__ == '__main__':
    
    plot_return_hist("AAPL", "1950-01-01", "2020-01-01")
