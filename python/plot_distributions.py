import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import gamma, expon, weibull_min, lognorm, norm

x = np.arange(0.01, 10, 0.01)

# Desired mean and standard deviation
#Willunga
mu_x = 1.2
sig_x = 0.35

mu_xs = [mu_x] #2.1 #2.3
sig_xs = [sig_x] #0.75 #0.7
#Convert to parameters
#mu = np.log(median)

# Data from each fault to add to plot
willunga_throws_rc = [1.20+0.1, 0.35, 1.06, 1.20, 1.20+0.1] # Add a bit to express uncertainty in second obs]
willunga_throws_ge = [True, True, False, False, True] # Flag for whether measurement is a minimum

for i, mu_x in enumerate(mu_xs):
    sig_x = sig_xs[i]
    mu = np.log(mu_x**2/np.sqrt(mu_x**2 + sig_x**2))
    sig2 = np.log(1  + sig_x**2/mu_x**2)
    sig = np.sqrt(sig2)
    
    print('mu', mu)
    print('sigma', sig)
    print('1/sigma', 1/sig)
    tau = 1/(sig2)
    print('tau', tau)
    lnorm = lognorm(s=sig, scale=np.exp(mu))
    y =lnorm.pdf(x)
    norm2 = norm()
    y2 = np.exp(norm2.pdf(x))
    plt.plot(x,y)

# Add measured throws
plt.bar(willunga_throws_rc, [ 0.8, 0.4, 0.4, 0.4, 0.8], width=[0.25, 0.1, 0.1, 0.1, 0.25],
        facecolor='cornflowerblue', edgecolor='mediumblue',
        linewidth=1, alpha=0.5)
#dunstan_density_value = 1./(dunstan_throws_devonshire[1] - dunstan_throws_devonshire[0])
#plt.bar(np.mean(dunstan_throws_devonshire), dunstan_density_value,
#        width=dunstan_throws_devonshire[1] - dunstan_throws_devonshire[0],
#        facecolor='sandybrown', edgecolor='darkorange', linewidth=1, alpha=0.5)
plt.xlim([0,3])
plt.xlabel('Single-event vertical displacement (m)')
plt.ylabel('Density')
figname = 'lognorm_%.2f_%.2f.png' % (mu_x, sig_x)
#figname = 'lognorm_median%.2f_%.2f.png' % (median, sig_x)
plt.savefig(figname, dpi=300)
