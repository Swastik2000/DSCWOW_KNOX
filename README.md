# Future and Present Weather Predictor DSC Wow
## For DSC WOW Hackathon 2020
## Contributors
- Swastik Mishra
- Ayush Agrawal
- Sourav Bera

[implemented by Scikit-learn]  

**Summary**  
Predicted daily temperature using multiple Linear Regression models & MLP with Scikit-learn, score = 0.85  
**Goal:**    
Using local weather station data of Bhubaneswar from SMHI Open Data to predict temperature for the next 24 hours by using  
different Machine Learning Algo

**Raw Data:**   
SMHI Open Data of Bhubaneswar, Odisha, India weather station (2007.01.01 - 2020.12.13)

**ML Algorithms (`Scikit-learn`):**  
linear_model.LinearRegression  
linear_model.Lasso  
linear_model.Ridge  
neural_network.MLPRegressor  

**Plotting:**  
matplotlib  

**Envs:**  
Anaconda and Python 2.7  

**Packages:**  
conda create -n weather_prediction_py27 python=2.7  
conda install numpy pandas matplotlib scikit-learn  
conda install spyder  

**Run Steps:**  
% git clone https://github.com/Swastik2000/DSCWOW_KNOX  
% python weather_prediction.py  
or
using `spyder` to run weather_prediction.py (Recommended)  

**Sample Outputs:**  
   * Command Line Outputs:  
<img src="./sample_outputs/sample_out_partial.png" width="400" height="400">

   * Plotting Outputs:  
![sample_plot_1](./sample_outputs/sample_plot_1.png)  
![sample_plot_2](./sample_outputs/sample_plot_2.png)  
![sample_plot_3](./sample_outputs/sample_plot_3.png)  
