# Fixed Income Index Calculator

## Overview
A Python-based financial engine that constructs a **market-value-weighted bond index** from raw CSV data. This project simulates the core infrastructure used by index providers to ingest market data, validate financial instruments, and dynamically calculate aggregate portfolio metrics.

## Project Architecture
The codebase is strictly separated by concern, demonstrating clean Object-Oriented Programming (OOP) principles:

* `bonds.py`: Contains the abstract base `Bonds` class and concrete subclasses. Demonstrates inheritance and polymorphism (e.g., overriding risk level calculations based on bond type).
* `index.py`: The core aggregation engine. Contains the `FixedIncomeIndex` class which handles the mathematical weighting, yield calculations, and sector mapping.
* `validator.py`: A dedicated data validation class that ensures "garbage in, garbage out" does not occur. Validates ISIN checksums, rating formats, and numeric logic.
* `main.py`: The entry point. Acts as the data pipeline and Factory, reading the `bonds.csv` file, applying rules, and building the final Index object.

## Financial Methodology
This index is **Market-Value Weighted**. 
1. **Market Value Calculation:** `(Price / 100) * Outstanding Amount`
2. **Constituent Weighting:** `Individual Market Value / Total Index Market Value`
3. **Index Yield:** The aggregate cash payout (Coupon * Outstanding) divided by the Total Index Market Value.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/fixed-income-index.git](https://github.com/yourusername/fixed-income-index.git)
   cd fixed-income-index
