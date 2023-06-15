# -*- coding: utf-8 -*-
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(prices):
    max_profit_so_far = 0
    lowest_price_seen = prices[0]
    for price_today in prices:
        if price_today < lowest_price_seen:
            lowest_price_seen = price_today
        profit_today = price_today - lowest_price_seen 
        if profit_today > max_profit_so_far:
            max_profit_so_far = profit_today
    return(max_profit_so_far)

