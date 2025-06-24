import numpy as np

# Load the predictions
predictions = np.load("results\weather_48_96_DLinear_custom_nq5_ftM_sl48_ll48_pl96_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0\pred.npy")

# Check shape
print("Shape of predictions:", predictions.shape)

# Print some predictions
print("Sample predictions:", predictions[:10])  # Print first 10 values
