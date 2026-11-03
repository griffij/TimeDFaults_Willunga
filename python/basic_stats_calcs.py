#Basic script for calculating basic stats from OxCal MCMC outputs
import numpy as np

data = np.loadtxt("../data/chronologies/Willunga_earthquakes_red_soils_E7_rev2_mcmc_2022ref.csv", delimiter=',')
data=data[:,1:]
diffs = np.diff(data,axis=1)
mm=np.mean(diffs,axis=1)
print('Mean of estimates of mean interevent time', np.mean(mm))
print('Standard deviation of estimates of mean interevent time', np.std(mm))

ss=np.std(diffs,axis=1)
print('Mean of estimates of standard deviation of interevent times', np.mean(ss))
print('Standard deviation of estimates of standard deviation of interevent times', np.std(ss))

cov = (np.std(diffs,axis=1) / np.mean(diffs,axis=1))
print('Mean estimate of COV', np.mean(cov))
print('Standard deviation of estimates of COV', np.std(cov))
