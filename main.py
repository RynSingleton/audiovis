from audio_processor import AudioProcessor
from visualizer import Visualizer

def main():
    fn = input("Input filename: ")
    processer = AudioProcessor(fn)
    visuals = Visualizer(processer)
    visuals.run()
    
if __name__ == "__main__":
    main()