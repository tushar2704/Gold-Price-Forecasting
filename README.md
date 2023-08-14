# Gold Price Forecasting



![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Microsoft Office](https://img.shields.io/badge/Microsoft_Office-D83B01?style=for-the-badge&logo=microsoft-office&logoColor=white)
![Microsoft Word](https://img.shields.io/badge/Microsoft_Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)

## Problem Description

The Gold Price Forecasting project is dedicated to predicting future gold prices using historical daily price data and other related financial indicators. Gold, a precious metal of enduring value, has been utilized as both an investment vehicle and a safe-haven asset for centuries. The price of gold is influenced by a myriad of factors, encompassing economic conditions, geopolitical events, inflation rates, and market sentiment. Accurate forecasting of gold prices is pivotal for investors, traders, and financial institutions to make informed choices and adeptly manage risks.
## Project Structure

The project repository is organized as follows:

```

├── LICENSE
├── README.md           <- README .
├── notebooks           <- Folder containing the final reports/results of this project.
│   │
│   └── gold_price.py   <- Final notebook for the project.
├── reports            <- Folder containing the final reports/results of this project.
│   │
│   └── Report.pdf     <- Final analysis report in PDF.
│   
├── src                <- Source for this project.
│   │
│   └── data           <- Datasets used and collected for this project.
|   └── model          <- Model.

```

## Dataset Information

The dataset for this project encompasses historical daily price data for diverse financial instruments, with a special focus on features linked to gold. Notable features include Open, High, Low, Close, Adjusted Close prices, and trading volume for gold (symbol: GLD), along with other pertinent financial instruments like the S&P 500 (SPY), Dow Jones (DJI), Euro Currency Index (EUR/USD), and Oil (USO), among others. Spanning several years, this dataset provides ample scope for time series analysis.

## Background Information

Throughout history, gold has garnered reverence for its scarcity, durability, and aesthetics. It has served as a store of value and a means of exchange in diverse civilizations. In contemporary times, gold plays a pivotal role in global financial markets. Its price is shaped by macroeconomic elements such as interest rates, inflation, geopolitical occurrences, and microeconomic factors including supply and demand dynamics. Gold frequently serves as a hedge against inflation and economic uncertainties.

## Objective

The primary objective of the Gold Price Forecasting project is to construct a predictive model that can prognosticate gold prices using historical price data and pertinent financial indicators. By training the model on past price patterns, it aspires to furnish accurate predictions about future price trends. This endeavor aims to furnish indispensable insights to investors and traders, enabling them to refine their gold-related investment strategies and adroitly manage their risk exposure.

## Methodology

1. **Data Preprocessing**: The initial step entails loading the dataset, converting the "Date" column into a datetime format for time series analysis, and gauging the correlation of each feature with the "Adjusted Close" price. Features exhibiting low correlation will be pruned to spotlight the salient ones.

2. **Exploratory Data Analysis (EDA)**: Employing data visualization techniques, the project will unravel insights into time series patterns and interrelations among various features. Line plots will visually elucidate time series data for diverse attributes.

3. **Time Series Split**: Employing TimeSeriesSplit, a specialized cross-validation technique for time series data, the dataset will be partitioned into training and testing subsets.

4. **Model Selection and Evaluation**: The forecasting model of choice is the LightGBM Regressor, a potent gradient boosting machine learning algorithm. Model performance evaluation will entail repeated k-fold cross-validation.

5. **Forecasting**: The LightGBM model will be trained on the training data to distill insights from historical price trends and feature relationships.

6. **Model Evaluation**: Performance assessment will involve metrics like Mean Absolute Error (MAE) and R-Squared, gauging accuracy and goodness of fit.

7. **Visualization**: Actual vs. predicted values will be juxtaposed through bar plots, facilitating a lucid contrast and comprehension of the model's predictive prowess.

## Conclusion

The Gold Price Forecasting project endeavors to devise a dependable and precise predictive model for anticipating gold prices, drawing from historical price data and relevant financial indicators. The successful creation and evaluation of this model will empower investors and traders with invaluable foresight into future price trends, equipping them to make judicious decisions and refine their gold market investment strategies. This undertaking's ultimate aspiration is to augment risk management efficacy and elevate investment outcomes within the dynamic realm of gold trading.
## License

This project is licensed under the [MIT License](LICENSE).
## Author
- <ins><b>©2023 Tushar Aggarwal. All rights reserved</b></ins>
- <b>[LinkedIn](https://www.linkedin.com/in/tusharaggarwalinseec/)</b>
- <b>[Medium](https://medium.com/@tushar_aggarwal)</b> 
- <b>[Tushar-Aggarwal.com](https://www.tushar-aggarwal.com/)</b>
- <b>[New Kaggle](https://www.kaggle.com/tagg27)</b> 

## Contact me!
If you have any questions, suggestions, or just want to say hello, you can reach out to us at [Tushar Aggarwal](mailto:info@tushar-aggarwal.com). We would love to hear from you!
