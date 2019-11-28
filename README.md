# Timeserie analysis API

## Installation
It is strongly recommended to use an Anaconda virtual env (Python=3.7) to run this API

Once the Anaconda env is set up run the following commands:
```bash
pip install -r requirements.txt
conda install gcc
conda install -c conda-forge fbprophet
```

## Available routes:

```bash
POST "/forecast"
  
Expected request body:
{
	"fileinfo": ( file csv in format:  ds, y [column] yyyy-mm-dd) 
    "periods": ( interval for predict in days )
    "season_type": ( frequency ("S", "M", "H", "D"))
}

timeserie: represents your ts in terms of <key: value>
future_ahead: represents the number of frequencies ahead in the future you to want to predict
frequency: represents the frequency of future data you want to predict. E.g. "S" -> seconds or "D" -> days
```
 


