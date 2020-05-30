# CSEP Testing Results: ComCat M7.1 (ci38457511), ShakeMap Surfaces  
**Forecast Name:** UCERF3-ETAS  
**Simulation Start Time:** 2019-07-06 03:19:54.040000+00:00  
**Evaluation Time:** 2019-07-13 03:19:54.040000+00:00  
**Catalog Source:** ComCat  
**Number Simulations:** 100000
# Table of Contents
1. [Visual Overview of Forecast](#visual_overview_of_forecast)
   1. [Cumulative Event Counts](#cumulative_event_counts)
   1. [Magnitude Histogram](#magnitude_histogram)
   1. [Approximate Rate Density with Observations](#approximate_rate_density_with_observations)
   1. [Conditional Rate Density](#conditional_rate_density)
   1. [Spatial Probability Plot](#spatial_probability_plot)
1. [CSEP Consistency Tests](#csep_consistency_tests)
   1. [Number Test](#number_test)
   1. [Magnitude Test](#magnitude_test)
   1. [Likelihood Test](#likelihood_test)
   1. [Probability Test](#probability_test)
   1. [Spatial Test](#spatial_test)
1. [One-point Statistics](#one-point_statistics)
   1. [B-Value Test](#b-value_test)
1. [Distribution-based Tests](#distribution-based_tests)
   1. [Inter-event Time Distribution](#inter-event_time_distribution)
   1. [Inter-event Distance Distribution](#inter-event_distance_distribution)
   1. [Total Earthquake Rate Distribution](#total_earthquake_rate_distribution)
# Visual Overview of Forecast <a name="visual_overview_of_forecast"></a>

These plots show qualitative comparisons between the forecast and the target data obtained from ComCat. Plots contain events within 7.0 days of the forecast start time and within 143.0 kilometers from the epicenter of the mainshock.  
  
All catalogs (synthetic and observed) are processed using the time-dependent magnitude of completeness model from Helmstetter et al., (2006).

## Cumulative Event Counts  <a name="cumulative_event_counts"></a>

Percentiles for cumulative event counts are aggregated within one-day bins. 


| | |
| --- | --- |
|  ![](plots/cum_counts_mw_2p5.png) | ![](plots/cum_counts_mw_3p0.png) |
|  ![](plots/cum_counts_mw_3p5.png) | ![](plots/cum_counts_mw_4p0.png) |
![](plots/cum_counts_mw_4p5.png)



## Magnitude Histogram  <a name="magnitude_histogram"></a>

Forecasted magnitude number distribution compared with the observed magnitude number distribution from ComCat. The forecasted number distribution in each magnitude bin is shown using a box and whisker plot. The box indicates the 95th percentile range and the whiskers indicate the minimum and maximum values. The horizontal line indicates the median.


![](plots/mag_hist_mw_2p5.png)



## Approximate Rate Density with Observations  <a name="approximate_rate_density_with_observations"></a>

The approximate rate density is computed from the expected number of events within a spatial cell and normalized over the time horizon of the forecast and the area of the spatial cell.


| | |
| --- | --- |
|  ![](plots/crd_obs_mw_2p5.png) | ![](plots/crd_obs_mw_3p0.png) |
|  ![](plots/crd_obs_mw_3p5.png) | ![](plots/crd_obs_mw_4p0.png) |
![](plots/crd_obs_mw_4p5.png)



## Conditional Rate Density  <a name="conditional_rate_density"></a>

Plots are conditioned on number of target events ± 5%, and can be used to create statistical tests conditioned on the number of observed events. In general, these plots will tend to be undersampled with respect to the entire distribution from the forecast.


| | |
| --- | --- |
|  ![](plots/cond_rates_mw_2p5.png) | ![](plots/cond_rates_mw_3p0.png) |
|  ![](plots/cond_rates_mw_3p5.png) | ![](plots/cond_rates_mw_4p0.png) |
![](plots/cond_rates_mw_4p5.png)



## Spatial Probability Plot  <a name="spatial_probability_plot"></a>

Probability of one or more events occuring in an individual spatial cell. This figure shows another way of visualizing the spatial distribution of a forecast.

| | |
| --- | --- |
|  ![](plots/prob_obs_mw_2p5.png) | ![](plots/prob_obs_mw_3p0.png) |
|  ![](plots/prob_obs_mw_3p5.png) | ![](plots/prob_obs_mw_4p0.png) |
![](plots/prob_obs_mw_4p5.png)



# CSEP Consistency Tests <a name="csep_consistency_tests"></a>

<b>Note</b>: These tests are explained in detail by Savran et al., (In review).

## Number Test  <a name="number_test"></a>

The number test compares the earthquake counts within the forecast region aginst observations from the target catalog.


| | | |
| --- | --- | --- |
|  ![](plots/n_test_mw_2p5.png) | ![](plots/n_test_mw_3p0.png) | ![](plots/n_test_mw_3p5.png) |
|  ![](plots/n_test_mw_4p0.png) | ![](plots/n_test_mw_4p5.png) | ![](plots/n_test_mw_5p0.png) |
|  ![](plots/n_test_mw_5p5.png) | ![](plots/n_test_mw_6p0.png) |



## Magnitude Test  <a name="magnitude_test"></a>

The magnitude test computes the sum of squared residuals between normalized incremental magnitude number distributions. The test distribution is built from statistics scored between individal catalogs and the expected magnitude number distribution of the forecast.


| | | |
| --- | --- | --- |
|  ![](plots/m-test_mw_2p5_dmag0p1.png) | ![](plots/m-test_mw_3p0_dmag0p1.png) | ![](plots/m-test_mw_3p5_dmag0p1.png) |
![](plots/m-test_mw_4p0_dmag0p1.png)



## Likelihood Test  <a name="likelihood_test"></a>

The likelihood tests uses a statistic based on the continuous point-process likelihood function. We approximate the rate-density of the forecast by stacking synthetic catalogs in spatial bins. The rate-density represents the probability of observing an event selected at random from the forecast. Event log-likelihoods are aggregated for each event in the catalog. This approximation to the continuous rate-density is unconditional in the sense that it does not consider the number of target events. Additionally, we do not include the magnitude component of the forecast to minimize the amount of undersampling present in these simulations.


| | | |
| --- | --- | --- |
|  ![](plots/l-test_mw_2p5.png) | ![](plots/l-test_mw_3p0.png) | ![](plots/l-test_mw_3p5.png) |
|  ![](plots/l-test_mw_4p0.png) | ![](plots/l-test_mw_4p5.png) |



## Probability Test  <a name="probability_test"></a>

This test uses a probability map to build the test distribution and the observed statistic. Unlike the pseudo-likelihood based tests, the test statistic is built by summing probabilities associated with cells where earthquakes occurred once. In effect,two simulations that have the exact same spatial distribution, but different numbers of events will product the same statistic.

| | | |
| --- | --- | --- |
|  ![](plots/prob-test_mw_2p5.png) | ![](plots/prob-test_mw_3p0.png) | ![](plots/prob-test_mw_3p5.png) |
|  ![](plots/prob-test_mw_4p0.png) | ![](plots/prob-test_mw_4p5.png) |



## Spatial Test  <a name="spatial_test"></a>

The spatial test is based on the same likelihood statistic from above. However, the scores are normalized so that differences in earthquake rates are inconsequential. As above, this statistic is unconditional.


| | | |
| --- | --- | --- |
|  ![](plots/s-test_mw_2p5.png) | ![](plots/s-test_mw_3p0.png) | ![](plots/s-test_mw_3p5.png) |
|  ![](plots/s-test_mw_4p0.png) | ![](plots/s-test_mw_4p5.png) |



# One-point Statistics <a name="one-point_statistics"></a>


## B-Value Test  <a name="b-value_test"></a>

This test compares the estimated b-value from the observed catalog along with the b-value distribution from the forecast. This test can be considered an alternate form to the Magnitude Test.


![](plots/bv_test_mw_2p5.png)



# Distribution-based Tests <a name="distribution-based_tests"></a>


## Inter-event Time Distribution  <a name="inter-event_time_distribution"></a>

This test compares inter-event time distributions based on a Kilmogorov-Smirnov type statistic computed from the empiricial CDF.


![](plots/ietd_test_mw_2p5.png)



## Inter-event Distance Distribution  <a name="inter-event_distance_distribution"></a>

This test compares inter-event distance distributions based on a Kilmogorov-Smirnov type statistic computed from the empiricial CDF.


![](plots/iedd_test_mw_2p5.png)



## Total Earthquake Rate Distribution  <a name="total_earthquake_rate_distribution"></a>

The total earthquake rate distribution provides another form of insight into the spatial consistency of the forecast with observations. The total earthquake rate distribution is computed from the cumulative probability distribution of earthquake occurrence against the earthquake rate per spatial bin.


![](plots/terd_test_mw_2p5.png)



