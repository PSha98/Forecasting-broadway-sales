# Forecasting Broadway Sales
![image](https://user-images.githubusercontent.com/36928110/172037580-05229692-dbbf-482b-9352-8256f5ae192b.png)

## Project Summary

![image](https://user-images.githubusercontent.com/36928110/172037700-89a16dd3-68fe-4e69-a62d-43d31f3e2999.png)

Broadway, are the theatrical performances presented in the 41 professional theaters, each with
500 or more seats, located in the Theater District and the Lincoln Center along Broadway, in
Midtown Manhattan, New York City. Broadway is one of the highest commercial sites for live
theater in the English-speaking world. According to The Broadway League, for the 2018–2019
season (which ended May 26, 2019) total attendance was 14,768,254 and Broadway shows had
US$1,829,312,140 in grosses, with attendance up 9.5%, grosses up 10.3%, and playing weeks
up 9.3%. Most Broadway shows are musicals.

Our project predicts how the Broadway industry can maximize profit on ticket sales and grosses.

Motivation:
Money for Broadway shows is typically raised by a small group of producers. Besides the initial
costs of producing the show, the producers are also responsible for the weekly wages of the cast
and crew as well as the rent for the theater in which the show is played. It typically takes investors
1 year to 18 months to break even. Broadway shows are a high risk/ high reward investment -
less than 1 in 5 shows make a profit, however when there is a hit like lion king or Hamilton,
the returns are enormous. Our project predicts how the Broadway industry can maximize profit
on ticket sales and theater attendance.

Stakeholders:

• Primary stakeholders: Producers of shows and Investors

• Secondary stakeholders: Theater owners & managers, Donors and Crew
Main Question: What are the trends in Broadway show attendance, ticket sales, playing
weeks/months and expected profits given historical data of Broadway shows?

Our Approaches:

• Trial: Linear Regression

• 5 Forecast Models:
ARIMA – Forecasting and Dynamic Forecasting
LSTM
Multiple Linear Regression
FB Prophet
(NB: These 5 models were used in order to recommend the best model for time-series
forecasting of the data to check for future trends and seasonality.)

Findings / Key Takeaways:

1. The best theater that contributes the highest gross in the Broadway Industry is the
Broadhurst Theater.

2. The best show that contributes the highest gross is “The Phantom of the Opera”

3. The show “The Phantom of the Opera” is the only show performed in the Majestic
Theater. This makes the Majestic Theater one of the top five highest grossing theaters.

4. The theaters that make up more than 2% of potential gross accounts for 68.318% of
weekly actual gross of ticket sales in the Broadway Industry.

Future Direction:

1. Improve Broadway dataset for large scale analysis

2. Be able to predict how the winning of a Tony award improves the business of investors

Results:
1. Scrapped data from Playbill website to structured format
![image](https://user-images.githubusercontent.com/36928110/172037889-666ab48d-1fab-4c3b-b3a8-bf26cf0a37a1.png)

2. Visualization
![image](https://user-images.githubusercontent.com/36928110/172037926-0bea5a4b-4b5a-4255-9694-407b6fd89862.png)
![image](https://user-images.githubusercontent.com/36928110/172037934-b915e367-c790-41a4-922b-7406fc0ade44.png)
![image](https://user-images.githubusercontent.com/36928110/172037944-6b3330ba-2466-48e7-a537-dc2c1f01e839.png)
![image](https://user-images.githubusercontent.com/36928110/172037954-c3b02e1a-7d18-45c7-b87f-74e73af57387.png)
![image](https://user-images.githubusercontent.com/36928110/172038029-bea62a19-bd29-4372-aba8-cc379678571c.png)
![image](https://user-images.githubusercontent.com/36928110/172038039-dbfd2609-f795-4812-8919-d0d21ab6436a.png)
![image](https://user-images.githubusercontent.com/36928110/172038055-34356e3b-1f57-4931-87c2-b5d7f86d4427.png)
![image](https://user-images.githubusercontent.com/36928110/172038063-c3f41640-9032-4189-a37c-151cc6cf00de.png)

3. Linear Regression
![image](https://user-images.githubusercontent.com/36928110/172038322-1955ae13-d5a8-4d9e-b3ad-80d0812d7ed9.png)


4. Prediction for Total Gross/Potential Gross
(a) ARIMA FORECASTING
![image](https://user-images.githubusercontent.com/36928110/172038152-33559bfa-2ef6-4b94-99d4-826510bfce0f.png)
(b) ARIMA DYNAMIC FORECASTING
![image](https://user-images.githubusercontent.com/36928110/172038166-1addc722-cd3b-42d8-86bb-895283ced99d.png)

ARIMA PREDICTION
![image](https://user-images.githubusercontent.com/36928110/172038192-5f56a019-7135-41ae-ba75-c698cf4a34fd.png)

(c) LSTM+Multiple Linear Regression
![image](https://user-images.githubusercontent.com/36928110/172038248-0c8ca128-7196-4cfd-932f-cb52aeacaf90.png)

(d) Prophet

![image](https://user-images.githubusercontent.com/36928110/172038261-71d9b831-0e6b-451a-923f-563fefd2c26f.png)

![image](https://user-images.githubusercontent.com/36928110/172038310-fdf6aed4-94d7-46d1-af76-4226a46632e3.png)

![image](https://user-images.githubusercontent.com/36928110/172038333-05c4a045-bf99-443e-9dd4-10926153a72d.png)








