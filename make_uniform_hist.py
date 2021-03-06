import os
import json

import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns

from csep.core.evaluations import EvaluationResult
from csep.core.repositories import FileSystem
from csep.utils.constants import SECONDS_PER_DAY
from csep.utils.documents import MarkdownReport
from csep.utils.file import mkdirs

sns.set()

mkdirs('plots')

# this obvious hard-coding won't cut it for an "operational" prospective system. these needs to be part of an experiment manifest
eval_basename = 'results/{}-test_mw_2p5.json'
u3etas_files = [
"2019_07_16-ComCatM7p1_ci38457511_7DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_07_27-ComCatM7p1_ci38457511_21DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_03-ComCatM7p1_ci38457511_28DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_19-ComCatM7p1_ci38457511_14DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_19-ComCatM7p1_ci38457511_35DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_19-ComCatM7p1_ci38457511_42DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_24-ComCatM7p1_ci38457511_49DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14",
"2019_08_31-ComCatM7p1_ci38457511_56DaysAfter_ShakeMapSurfaces",
"2019_09_04-ComCatM7p1_ci38457511_ShakeMapSurfaces",
"2019_09_09-ComCatM7p1_ci38457511_63DaysAfter_ShakeMapSurfaces",
"2019_09_16-ComCatM7p1_ci38457511_70DaysAfter_ShakeMapSurfaces"
]

nofaults_files = [
"2019_07_16-ComCatM7p1_ci38457511_7DaysAfter_ShakeMapSurfaces-noSpont-NoFaults",
"2019_07_27-ComCatM7p1_ci38457511_21DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14-NoFaults",
"2019_08_03-ComCatM7p1_ci38457511_28DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14-NoFaults",
"2019_08_19-ComCatM7p1_ci38457511_14DaysAfter_ShakeMapSurfaces-noSpont-NoFaults",
"2019_08_19-ComCatM7p1_ci38457511_35DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14-NoFaults",
"2019_08_19-ComCatM7p1_ci38457511_42DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14-NoFaults",
"2019_08_24-ComCatM7p1_ci38457511_49DaysAfter_ShakeMapSurfaces-noSpont-full_td-scale1.14-NoFaults",
"2019_08_31-ComCatM7p1_ci38457511_56DaysAfter_ShakeMapSurfaces-NoFaults",
"2019_09_04-ComCatM7p1_ci38457511_ShakeMapSurfaces-NoFaults",
"2019_09_09-ComCatM7p1_ci38457511_63DaysAfter_ShakeMapSurfaces-NoFaults",
"2019_09_16-ComCatM7p1_ci38457511_70DaysAfter_ShakeMapSurfaces-NoFaults"
]

tests = ['n', 'm', 'l', 's', 'iedd', 'ietd', 'prob', 'terd', 'bv']

md = MarkdownReport('README.md')
md.add_sub_heading('Comprehensive Evaluations', 1,
        "The following plots compare U3ETAS forecasts with the NoFaults version for about ten weeks of forecasts following the Ridgecrest sequence. "
        "For each test considered we will compare the results against the quantiles from a uniform distribution under the assumption that "
        "the p-values from independent samples of the test distribution are uniformly distributed. We also plot the p-values for each simulation "
        "in time to observe possible temporal trends.  "
        "\n \n"
        "Target events with M2.5+ are collected for seven days following the origin time of the forecast. Events are selected only if they occur within "
        "three fault radii from the epicenter of the mainshock of the sequence. We apply the Mc(t) model from Helmstetter et al., to account for "
        " catalog incompleteness during the sequence.")
x = np.arange(0,1,0.1)
y = x
for t in tests:
    u3_quantiles = []
    nf_quantiles = []
    origin_times = []
    for f, fn in zip(u3etas_files, nofaults_files):
        # start times are the same
        with open(os.path.join(f, 'config.json'), 'r') as conf_file:
            config = json.load(conf_file)

        origin_times.append(config['startTimeMillis'])
        eval_basename.format(t)

        u3_result = FileSystem(url=os.path.join(f, eval_basename.format(t))).load(EvaluationResult())
        nf_result = FileSystem(url=os.path.join(fn, eval_basename.format(t))).load(EvaluationResult())

        n_test_scoring = False
        try:
            n_test_scoring = True
            u3_quantiles.append(u3_result.quantile[1])
            nf_quantiles.append(nf_result.quantile[1])
        except:
            u3_quantiles.append(u3_result.quantile)
            nf_quantiles.append(nf_result.quantile)

    origin_times = np.array(origin_times)
    u3_quantiles = np.array(u3_quantiles)
    nf_quantiles = np.array(nf_quantiles)
    origin_times = (origin_times - np.min(origin_times)) / 1000 / SECONDS_PER_DAY

    u3_combined = np.column_stack([u3_quantiles, origin_times])
    u3_combined_sorted = u3_combined[u3_combined[:,0].argsort()]

    nf_combined = np.column_stack([nf_quantiles, origin_times])
    nf_combined_sorted = nf_combined[nf_combined[:,0].argsort()]

    # set up QQ plots and KS test
    n = len(nf_quantiles)
    k = np.arange(1, n+1)
    # plotting points for uniform quantiles
    pp = k / (n+1)
    # compute confidence intervals for order statistics using beta distribution
    ulow = scipy.stats.beta.ppf(0.025, k, n-k+1)
    uhigh = scipy.stats.beta.ppf(0.975, k, n-k+1)
    # format k-s test on the uniform quantiles
    ks, p_u3 = scipy.stats.kstest(u3_combined_sorted[:,0], 'uniform')
    ks, p_nf = scipy.stats.kstest(nf_combined_sorted[:,0], 'uniform')


    fig, ax = plt.subplots()
    im = plt.scatter(u3_combined_sorted[:,0], pp, c='tab:blue', label='U3ETAS')
    im = plt.scatter(nf_combined_sorted[:,0], pp, c='tab:orange', label='NoFaults')
    ax.set_ylim([0,1.05])
    ax.set_xlim([0,1.05])
    ax.set_xlabel('Quantile Scores')
    ax.set_ylabel('Standard uniform quantiles')
    ax.plot(pp, pp, '-k')
    ax.plot(ulow, pp, ':k')
    ax.plot(uhigh, pp, ':k')
    ax.legend(loc='lower right')
    uc_fname = os.path.join('plots', f'uniform_distr-{t}-test-mw_2p5.pdf')
    fig.savefig(uc_fname)
    uc_fname = os.path.join('plots', f'uniform_distr-{t}-test-mw_2p5.png')
    fig.savefig(uc_fname)

    nf_combined_sorted_time = nf_combined[nf_combined[:,1].argsort()]
    u3_combined_sorted_time = u3_combined[u3_combined[:,1].argsort()]
    fig, ax = plt.subplots()
    plt.plot(nf_combined_sorted_time[:,1], nf_combined_sorted_time[:,0], '-ok', clip_on=False, zorder=10, color='tab:orange')
    plt.plot(u3_combined_sorted_time[:,1], u3_combined_sorted_time[:,0], '-ok', clip_on=False, zorder=10, color='tab:blue')
    u3_combined_sorted_time = u3_combined[u3_combined[:,1].argsort()]

    ax.set_xlim([0, np.max(nf_combined_sorted_time[:,1])])
    ax.set_ylim([0,1.0])
    if t == 'n':
        ax.fill_between(nf_combined_sorted_time[:,1], 0.025, color='gray', alpha=0.4)
    else:
        ax.fill_between(nf_combined_sorted_time[:,1], 0.05, color='gray', alpha=0.4)
    ax.set_xlabel('Test day (days since mw 7.1 mainshock)')
    ax.set_ylabel('Quantile score')
    pvt_fname = os.path.join('plots', f'cumulative-{t}-test_mw_2p5.pdf')
    fig.savefig(pvt_fname)
    pvt_fname = os.path.join('plots', f'cumulative-{t}-test_mw_2p5.png')
    fig.savefig(pvt_fname)
    md.add_result_figure(f"Cumulative {t.upper()}-Test Result", 2, [uc_fname[:-4], pvt_fname[:-4]], ncols=2,
            caption="(Left) Evaluation p-values compared against uniform distribution quantiles. If observations are consistent "
                 "with the test-distribution (assuming the forecast is true) the quantile scores should follow an exponential distribution. "
                 "(Right) Quantile scores plotted progressively during the Ridgecrest sequence. The shaded gray regions indicate critical "
                 "regions assuming α = 5%.")
md.finalize('./')
