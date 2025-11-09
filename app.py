import time
import market
import trader
import config
import json
from datetime import datetime
import trade_logger
from flask import Flask, render_template, jsonify

# ÖNCE trade modülünü import et
import trade

# Initialize portfolio ONCE at startup
portfolio = None
if config.SIMULATION_MODE:
    from simulation import SimulatedPortfolio
    portfolio = SimulatedPortfolio()
    # Şimdi portfolio'yu trade modülüne set et
    trade.set_portfolio(portfolio)
    print(f"[INIT] Portfolio initialized and shared with trade module.")

# --- Flask Web Server ---
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/portfolio_summary')
def api_portfolio_summary():
    if portfolio:
        return jsonify(portfolio.get_portfolio_summary())
    return jsonify({})

@app.route('/api/open_positions')
def api_open_positions():
    if portfolio:
        return jsonify(portfolio.get_all_open_positions())
    return jsonify({})

@app.route('/api/trade_log')
def api_trade_log():
    try:
        with open(trade_logger.LOG_FILE, 'r') as f:
            return jsonify({"log_content": f.read()})
    except FileNotFoundError:
        return jsonify({"log_content": "Log file not found."})

@app.route('/api/portfolio_history')
def api_portfolio_history():
    if portfolio:
        return jsonify(portfolio.get_equity_history())
    return jsonify([])

# --- End Flask Web Server ---
