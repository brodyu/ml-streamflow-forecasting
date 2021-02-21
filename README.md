# Streamflow Forecasting with Deep Learning

This is a data research project that leverages deep learning to accurately predict daily streamflow discharge of various streams on Oahu.

## Manoa Stream

Manoa stream is the primary stream that flows through the town of Manoa and the University of Hawaii's main campus. The task of modeling Manoa stream's discharge is of primary concern due to previous flood history in the Manoa area. On October 30, 2004, Manoa stream overflowed causing millions of dollars in damanges to residential homes and educational buildings. With the addition of climate change, water levels on the river will become more variable. 

### Data 

To model the discharge of Manoa stream, weather data was aggregated using the weather-api script in this repository. Additional streamflow data from Waihi and Waiakeakua stream were joined. Both Waihi and Waiakeakua streams flow into Manoa stream at the top of Manoa town. The data is cleansed for outliers and missing values before being normalized and transformed for time series forecasting. 

## Models
Three models were trained, tested, and tuned for optimal results. The deep learning models we used were:
- Long Short-term Memory (LSTM)
- Bidirectional LSTM
- Gated Recurrent Unit (GRU)
