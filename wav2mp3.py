import os
import torch
import torchaudio

def convert_wav_to_mp3(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.wav'):
                wav_path = os.path.join(dirpath, filename)
                mp3_path = os.path.join(dirpath, filename[:-4] + '.mp3')
                # Load the wav file
                waveform, sample_rate = torchaudio.load(wav_path)
                # Trim to 10-40 seconds
                start_frame = 10 * sample_rate
                end_frame = 40 * sample_rate
                if waveform.shape[1] > end_frame:
                    waveform = waveform[:, start_frame:end_frame]
                elif waveform.shape[1] > start_frame:
                    waveform = waveform[:, start_frame:]
                # Save as mp3
                torchaudio.save(mp3_path, waveform, sample_rate, format="mp3")
                # Remove the original wav file
                os.remove(wav_path)
                print(f"Converted and removed: {wav_path}")

# Usage
convert_wav_to_mp3('./audio')  # Start from the current directory
