# Dummy static market data (can be upgraded later to live API)
market_data = [
    ("USD/EUR", "1.09", "blue"),
    ("BTC/USD", "$66,500", "orange"),
    ("ETH/USD", "$3,200", "purple"),
    ("GOLD", "$2,350", "gold"),
    ("OIL", "$89.30", "black"),
    ("KSE-100", "47,300 ↑", "green"),
    ("NYSE", "17,100 ↑", "green"),
    ("NASDAQ", "14,250 ↓", "red")
]

ticker_items = [
    f'<span style="color:{color};font-weight:bold;">{name}: {value}</span>'
    for name, value, color in market_data
]

html_content = f'''
<div style="background-color:#003300;color:white;padding:10px;font-size:18px;">
    <marquee behavior="scroll" direction="left" scrollamount="4">
        {"  •  ".join(ticker_items)}
    </marquee>
</div>
'''

with open("market_ticker.html", "w", encoding="utf-8") as f:
    f.write(html_content)
