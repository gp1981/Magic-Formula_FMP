import requests
from tqdm import tqdm
import pandas as pd


def fetch_stock_list(api_key):
    stock_list_path = (
        f"https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}"
    )
    response = requests.get(stock_list_path)

    if response.status_code == 200:
        stock_list_data = response.json()
        stock_list_df = pd.DataFrame(stock_list_data)
        return stock_list_df
    else:
        print("Failed to fetch stock list data from the API")
        return None


def fetch_financial_statement_symbol_list(api_key):
    symbol_list_path = f"https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey={api_key}"
    response = requests.get(symbol_list_path)

    if response.status_code == 200:
        symbol_list_data = response.json()
        symbol_list_df = pd.DataFrame(symbol_list_data)
        return symbol_list_df
    else:
        print("Failed to fetch financial statement symbol list data from the API")
        return None


def fetch_symbol_profile(api_key, symbol):
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        return data
    else:
        return None


def filter_and_merge_data(filtered_data, api_key):
    filtered_profiles = []

    with tqdm(
        total=len(filtered_data["symbol"]), desc="Fetching and Filtering Data"
    ) as pbar:
        for symbol in filtered_data["symbol"]:
            profile_data = fetch_symbol_profile(api_key, symbol)
            if profile_data:
                filtered_profiles.append(profile_data)
            pbar.update(1)

    profile_df = pd.DataFrame(filtered_profiles)

    # Apply filtering conditions
    filtered_df = profile_df[
        (profile_df["mktCap"] < 1000000000)
        & (
            ~profile_df["sector"].isin(
                ["Financial Services", "Utilities - Regulated", "Utilities"]
            )
        )
        & (~profile_df["industry"].isin(["Bank", "Insurance", "Mortgage", "REIT"]))
        & (~profile_df["companyName"].str.contains("Depositary", case=False))
        & (profile_df["country"].isin(["US", "CA"]))
    ]

    return filtered_df


def fetch_income_statement(api_key, symbol):
    url = f"https://financialmodelingprep.com/api/v3/income-statement-as-reported/{symbol}?period=quarter&limit=50&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch income statement for symbol {symbol}")
        return []


def fetch_balance_sheet(api_key, symbol):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{symbol}?period=quarter&limit=50&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch balance sheet for symbol {symbol}")
        return []


def fetch_cash_flow(api_key, symbol):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{symbol}?period=quarter&limit=50&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch cash flow for symbol {symbol}")
        return []


def fetch_all_financial_statements(api_key, symbol_list):
    income_statement_data = []
    balance_sheet_data = []
    cash_flow_data = []

    with tqdm(total=len(symbol_list), desc="Fetching Financial Data") as pbar:
        for symbol in symbol_list:
            income_statement = fetch_income_statement(api_key, symbol)
            if isinstance(income_statement, list) and income_statement:
                income_statement_data.append(pd.DataFrame(income_statement))

            balance_sheet = fetch_balance_sheet(api_key, symbol)
            if isinstance(balance_sheet, list) and balance_sheet:
                balance_sheet_data.append(pd.DataFrame(balance_sheet))

            cash_flow = fetch_cash_flow(api_key, symbol)
            if isinstance(cash_flow, list) and cash_flow:
                cash_flow_data.append(pd.DataFrame(cash_flow))

            pbar.update(1)  # Update the progress bar

    if income_statement_data:
        income_statement_df = pd.concat(income_statement_data, ignore_index=True)
    else:
        income_statement_df = pd.DataFrame()

    if balance_sheet_data:
        balance_sheet_df = pd.concat(balance_sheet_data, ignore_index=True)
    else:
        balance_sheet_df = pd.DataFrame()

    if cash_flow_data:
        cash_flow_df = pd.concat(cash_flow_data, ignore_index=True)
    else:
        cash_flow_df = pd.DataFrame()

    return income_statement_df, balance_sheet_df, cash_flow_df
