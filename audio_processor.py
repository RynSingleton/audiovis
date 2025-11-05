import numpy as np
import soundfile as sf

class AudioProcessor:
    def __init__(self, filename):
        """
        Load the audio file and store its data.
        
        Args:
            filename: Path to the audio file (.wav)
        """
        
        data, samplerate = sf.read(filename)
        if len(data.shape) == 2: #stereo, we got a 2d array for data instead of a list that is 2 tall (left and right)
            data = data.mean(axis=1) #average along the vertical axis (mean of left and right)
        self.data, self.samplerate = data, samplerate
        
        
    
    def get_fft_data(self, chunk):
        """
        Perform FFT on a chunk of audio data.
        
        Args:
            chunk: Array of audio samples
            
        Returns:
            Array of frequency magnitudes
        """
        #get the 1dim fft for a sample of time "chunk". we just care about magnitude, so we take the absolute value
        fft_result = np.fft.fft(chunk)
        magnitudes = np.abs(fft_result)
        magnitudes = magnitudes[:len(magnitudes)//2]
        return magnitudes
        