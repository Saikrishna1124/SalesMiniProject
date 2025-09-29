from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Load CSV
    df = pd.read_csv("sales.csv")

    # Total Sales
    total_sales = df["Sales"].sum()

    # Sales by Product
    product_sales = df.groupby("Product")["Sales"].sum().to_dict()

    return render_template("index.html",
                           total_sales=total_sales,
                           product_sales=product_sales)

if __name__ == "__main__":
    app.run(debug=True)
