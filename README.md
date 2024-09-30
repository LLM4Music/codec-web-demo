⚠️ *Warning: This website may not function properly on Safari. For the best experience, please use Google Chrome.*

⚠️ *Main Reference: [Stable Codec Demo](https://github.com/Stability-AI/stable-codec-demo)*

## Autoencoder reconstructions

We compare the performance of various codecs using the Song Describer Dataset.


## Audio Codec Comparison

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
