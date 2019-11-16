# CSEP Testing Results: ComCat M7.1 (ci38457511), 28 Days After, ShakeMap Surfaces  
**Forecast Name:** UCERF3-ETAS  
**Simulation Start Time:** 2019-08-03 03:19:54.040000+00:00  
**Evaluation Time:** 2019-08-10 03:19:54.040000+00:00  
**Catalog Source:** ComCat  
**Number Simulations:** 100000
# Table of Contents
1. [Visual Overview of Forecast](#visual_overview_of_forecast)
   1. [Cumulative Event Counts](#cumulative_event_counts)
   1. [Magnitude Histogram](#magnitude_histogram)
   1. [Approximate Rate Density with Observations](#approximate_rate_density_with_observations)
   1. [Conditional Rate Density](#conditional_rate_density)
1. [CSEP Consistency Tests](#csep_consistency_tests)
   1. [Number Test](#number_test)
   1. [Magnitude Test](#magnitude_test)
   1. [Likelihood Test](#likelihood_test)
   1. [Spatial Test](#spatial_test)
1. [One-point Statistics](#one-point_statistics)
   1. [B-Value Test](#b-value_test)
# Visual Overview of Forecast <a name="visual_overview_of_forecast"></a>

These plots show qualitative comparisons between the forecast and the target catalog obtained from ComCat. Plots contain events within 7.0 days of the forecast start time and within 143.0 kilometers from the epicenter of the mainshock.  
  
All catalogs are processed using a time-dependent magnitude of completeness from Helmstetter et al., 2006.

## Cumulative Event Counts  <a name="cumulative_event_counts"></a>

Percentiles for cumulative event counts are aggregated within one-day bins.  


| | |
| --- | --- |
|  ![](plots/cum_counts_mw_2p5.png) | ![](plots/cum_counts_mw_3p0.png) |
|  ![](plots/cum_counts_mw_3p5.png) | ![](plots/cum_counts_mw_4p0.png) |
![](plots/cum_counts_mw_4p5.png)
## Magnitude Histogram  <a name="magnitude_histogram"></a>



![](plots/mag_hist_mw_2p5.png)
## Approximate Rate Density with Observations  <a name="approximate_rate_density_with_observations"></a>



| | |
| --- | --- |
|  ![](plots/crd_obs_mw_2p5.png) | ![](plots/crd_obs_mw_3p0.png) |
|  ![](plots/crd_obs_mw_3p5.png) | ![](plots/crd_obs_mw_4p0.png) |
![](plots/crd_obs_mw_4p5.png)
## Conditional Rate Density  <a name="conditional_rate_density"></a>

Plots are conditioned on number of target events ± 5%


| | |
| --- | --- |
|  ![](plots/cond_rates_mw_2p5.png) | ![](plots/cond_rates_mw_3p0.png) |
# CSEP Consistency Tests <a name="csep_consistency_tests"></a>

<b>Note</b>: These tests are explained in detail by Savran et al. (In prep).

## Number Test  <a name="number_test"></a>

The number test compares the earthquake counts within the forecast region aginst observations from the target catalog.


| | | |
| --- | --- | --- |
|  ![](plots/n_test_mw_2p5.png) | ![](plots/n_test_mw_3p0.png) | ![](plots/n_test_mw_3p5.png) |
|  ![](plots/n_test_mw_4p0.png) | ![](plots/n_test_mw_4p5.png) | ![](plots/n_test_mw_5p0.png) |
|  ![](plots/n_test_mw_5p5.png) | ![](plots/n_test_mw_6p0.png) |
## Magnitude Test  <a name="magnitude_test"></a>

The magnitude test computes the sum of squared residuals between normalized incremental Magnitude-Number distributions. The test distribution is built from statistics scored between individal catalogs and the expected Magnitude-Number distribution of the forecast.


| | |
| --- | --- |
|  ![](plots/m-test_mw_2p5.png) | ![](plots/m-test_mw_3p0.png) |
## Likelihood Test  <a name="likelihood_test"></a>

The likelihood tests uses a statistic based on the continuous point-process likelihood function. We approximate the rate-density of the forecast by stacking synthetic catalogs in spatial bins. The rate-density represents the probability of observing an event selected at random from the forecast. Event log-likelihoods are aggregated for each event in the catalog. This approximation to the continuous rate-density is unconditional in the sense that it does not consider the number of target events.


| | | |
| --- | --- | --- |
|  ![](plots/l-test_mw_2p5.png) | ![](plots/l-test_mw_3p0.png) | ![](plots/l-test_mw_3p5.png) |
|  ![](plots/l-test_mw_4p0.png) | ![](plots/l-test_mw_4p5.png) |
## Spatial Test  <a name="spatial_test"></a>

The spatial test is based on the same likelihood statistic from above. However, the scores are normalized so that differences in earthquake rates are inconsequential. As above, this statistic is unconditional.


| | |
| --- | --- |
|  ![](plots/s-test_mw_2p5.png) | ![](plots/s-test_mw_3p0.png) |
# One-point Statistics <a name="one-point_statistics"></a>


## B-Value Test  <a name="b-value_test"></a>

This test compares the estimated b-value from the observed catalog along with the b-value distribution from the forecast. This test can be considered an alternate form to the Magnitude Test.


![](plots/bv_test_mw_2p5.png)
