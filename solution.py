import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def count_steps(csv_file):
    """Count steps from accelerometer data
    Input: CSV with columns: time, x, y, z
    Output: Number of steps detected
    """
    # Load data
    data = pd.read_csv(csv_file)
    
    # Calculate magnitude (students improve this)
    data['mag'] = np.sqrt(data['x']**2 + data['y']**2 + data['z']**2)
    
    # Basic peak detection (students tune this)
    peaks, _ = find_peaks(data['mag'], height=10, distance=50)
    
    return len(peaks)

if __name__ == "__main__":
    # Test on sample data
    steps = count_steps('data/sample_walk.csv')
    print(f"Steps detected: {steps}")
