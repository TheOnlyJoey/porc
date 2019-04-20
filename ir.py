import math
import numpy as np

def gen_ess(T, f1, f2, sample_rate):
    """Generate an Exponential Sine Sweep signal and its inverse.

    T is time in seconds
    f1 is starting frequency in Hz
    f2 is ending frequency in Hz
    """
    samples = int(sample_rate * T + 0.5)
    # Avoid low or hi-freq energy at the begin/end of the filter by fading for up to 50ms.
    fadesamples = min(sample_rate * 0.050, samples * 0.05)
    twopi = math.pi * 2
    w1 = f1 * twopi
    w2 = f2 * twopi
    L = T / math.log(w2 / w1)
    K = w1 * L
    x = np.zeros(samples)
    A = 0.8  # amplitude
    for i in range(samples):
        t = i / float(sample_rate)
        fadeout = min(1.0, ((samples - i) / float(fadesamples)))
        fadein = min(1.0, i / float(fadesamples))
        fadefactor = min(1.0, i / float(fadesamples), (samples - 1 - i) / float(fadesamples))
        x[i] = A * fadefactor * fadefactor * math.sin(K * (math.exp(t / L) - 1))
    
    f = np.zeros(samples)
    for i in range(samples):
        t = i / float(sample_rate)
        f[i] = x[samples - 1 - i] * w1 / (w1 * math.exp(t/L))

    return (x, f)


def generate_ess(duration, f1, f2):
    ess, inv = gen_ess(duration, f1, f2, 48000)
    return (ess, inv)

def compute_ir(ess, inv, ir_filename):
    sl, sr, rate = readwav(ess)
    f, _, rate2 = readwav(inv)
    if rate != rate2:
        raise ("sweep recording sample rate %s must match inverse sweep signal "
               "sample rate %s!" % (rate, rate2))
    print("Convolving left, please be patient!")
    irl = np.convolve(sl, f)
    print ("Now convolving right...")
    irr = np.convolve(sr, f)
    max_value = max(np.amax(irl), -np.amin(irl), np.amax(irr), -np.amin(irr))
    scale = 0.5 / max_value
    irl *= scale
    irr *= scale
    return (irl, irr)

def write_ir(irl, irr, ir_filename):
    writewav(ir_filename, irl, irr, 48000)