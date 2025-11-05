from audio_processor import AudioProcessor

processor = AudioProcessor('wav_sample.wav')

#get first 1024 samples for now and grab that fft data (each bin represents amount of that magnitude range)
chunk = processor.data[:1024]
fft_data = processor.get_fft_data(chunk)

print(f"Original chunk size: {len(chunk)}")
print(f"FFT output size: {len(fft_data)}")
print(f"First 10 frequency magnitudes: {fft_data[:10]}")