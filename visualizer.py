import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    def __init__(self, audio_processor, chunk_size=1024, num_bars=64):
        """
        Initialize the visualizer.
        
        Args:
            audio_processor: AudioProcessor instance
            chunk_size: Number of samples per FFT
            num_bars: Number of frequency bars to display
        """
        self.processor = audio_processor
        self.chunk_size = chunk_size
        self.num_bars = num_bars
        self.total_chunks = len(self.processor.data)//self.chunk_size
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        x = range(self.num_bars)
        self.bars = self.ax.bar(x, [0] * self.num_bars)
        self.ax.set_ylim(0, 100)
        
    def update_frame(self, frame_num):
        """
        Update function called for each animation frame.
        
        Args:
            frame_num: Current frame number
        """
        start = frame_num * self.chunk_size
        end = start + self.chunk_size
        chunk = self.processor.data[start:end]
        
        magnitudes = self.processor.get_fft_data(chunk)
        magnitudes = magnitudes[:self.num_bars]
        
        for bar, height in zip(self.bars, magnitudes):
            bar.set_height(height)
        
        return self.bars
    
    def run(self):
        """Start the visualization animation."""
        anim = animation.FuncAnimation(self.fig, self.update_frame, frames=self.total_chunks, interval=50)
        anim.save("visuals.gif", writer='pillow')
        plt.show()