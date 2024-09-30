⚠️ *Warning: This website may not function properly on Safari. For the best experience, please use Google Chrome.*

⚠️ *Main Reference: [Stable Codec Demo](https://github.com/Stability-AI/stable-codec-demo)*

## Autoencoder reconstructions

| Model                     | SR / Channel  | Token/sec | Vocab Size | STFT Distance ↓ | MEL Distance ↓ |
|----------------------------|---------------|-----------|------------|-----------------|----------------|
| DAC (9)                    | 44.1kHz / 1   | 774       | 9216       | 0.96            | 0.53           |
| DAC (1)                    | 44.1kHz / 1   | 86        | 1024       | 1.46            | 1.18           |
| WavTokenizer               | 24kHz / 1     | 75        | 4096       | 1.26            | 0.90           |
| EnCodec (4)                | 32kHz / 1     | 200       | 8192       | 1.24            | 0.88           |
| Stable Audio Open          | 44.1kHz / 2   | 22        | -          | 1.30            | 0.78           |
| - Add Kmeans               | 44.1kHz / 2   | 22        | 8192       | 2.76            | 2.34           |
| - Add Product Quantization | 44.1kHz / 2   | 22        | 8192       | 2.07            | 1.66           |
| - Add Vector Quantization  | 44.1kHz / 2   | 22        | 8192       | 2.05            | 1.68           |


We compare the performance of various codecs using the Song Describer Dataset.

| Model | 364090 | 973498 | 1007274 |
| ----- | ------ | ------ | ------- |
| Ground truth | <audio controls preload=False><source src="audio/364090/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| DAC (9) | <audio controls preload=False><source src="audio/364090/dac44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/dac44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/dac44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| DAC (1) | <audio controls preload=False><source src="audio/364090/dac44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/dac44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/dac44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| Encodec | <audio controls preload=False><source src="audio/364090/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| Wav Tokenizer | <audio controls preload=False><source src="audio/364090/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| Stable Audio Open | <audio controls preload=False><source src="audio/364090/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| + Kmeans | <audio controls preload=False><source src="audio/364090/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| + ProductQuantizer | <audio controls preload=False><source src="audio/364090/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| + VQVAE | <audio controls preload=False><source src="audio/364090/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
