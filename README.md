# Streamflow Forecasting Using Recurrent Neural Networks and Transfer Learning

Brody Uehara (1), Trista McKenzie (2), Henrietta Dulai (2)

1 Department of Information and Computer Science, University of Hawaiʻi at Mānoa, Honolulu, HI, 96822, USA
2 Department of Earth Science, University of Hawaiʻi at Mānoa, Honolulu, HI, 96822, USA

## Abstract
Many streams across Hawaiʻi lack stream discharge monitoring due to technical and financial constraints. Yet, stream discharge information is critical for island water budgets, understanding pollution transport, and studying stream ecosystems. Within the field of artificial intelligence, deep learning methods have become a popular tool for forecasting and modeling these natural processes. Deep learning methods allow us to estimate the discharge of streams that lack gages and corresponding data. In this work, we implement and test several variations of recurrent neural networks to predict stream discharge on the island of Oʻahu, Hawaiʻi. Recurrent neural networks were selected based on their advantages over other data-driven artificial neural networks and statistical models. Each model was fed observed precipitation data along with other meteorological data such as temperature and humidity in combination with existing stream discharge records. These models were used to forecast the daily streamflow discharge of Mānoa, Makiki, and Pālolo Streams. Our results demonstrate that deep learning can be successfully used to predict stream discharge in tropical island settings. Modeling the streamflows of Mānoa, Makiki, and Pālolo Streams will serve as the basis for transfer-learning techniques for other streams that lack credible stream discharge records, providing vital stream discharge information for these locations and proof of concept for locations beyond Oʻahu. 

### Models
Three models were trained, tested, and tuned for optimal results. The deep learning models we used were:
- Long Short-term Memory (LSTM)
- Bidirectional LSTM
- Gated Recurrent Unit (GRU)

### Results
After tuning the model parameters for optimal results, we found the Gated Recurrent Unit (GRU) model performed the best in terms of minimizing loss and reducing overfitting. Below are the loss, actual forecast, and scatterpolt graphs for the GRU model. 

More model info: 
- 5 backward steps
- each model trained on 64 units and 25 epochs
- GRU model acheieved a 8.253 RMSE on testing data

![alt text](https://github.com/brodyu/streamflow-forecasting-deep-learning/blob/main/reduced_visuals/lossgraphs3.jpg)

![alt text](https://github.com/brodyu/streamflow-forecasting-deep-learning/blob/main/reduced_visuals/actual-forecastplot3.jpg)

![alt text](https://github.com/brodyu/streamflow-forecasting-deep-learning/blob/main/reduced_visuals/scatterplot3.jpg)
