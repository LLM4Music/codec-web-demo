⚠️ *Warning: This website may not function properly on Safari. For the best experience, please use Google Chrome.*
⚠️ Main Reference: [Stable Codec Demo](https://github.com/Stability-AI/stable-codec-demo)

## Autoencoder reconstructions

We compare the performance of various codecs using the Song Describer Dataset.


## Baseline Models

| SongDescriber ID | Ground truth | DAC (9) | DAC (1) | Encodec | Wav Tokenizer |
| ---------------- | ------------ | -------- | -------- | -------- | -------- |
| 364090 | <audio controls preload=False><source src="audio/364090/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/dac_44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/dac_44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| 973498 | <audio controls preload=False><source src="audio/973498/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/dac_44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/dac_44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |
| 1007274 | <audio controls preload=False><source src="audio/1007274/original.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/dac_44100_9.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/dac_44100_1.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/encodec_4.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/wavtok.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> |


## Stable Audio Variations

| SongDescriber ID | Stable Audio Open | + Kmeans | + ProductQuantizer | + VQVAE | 
| ---------------- | ------------ | -------- | -------- | -------- | -------- |
| 364090 | <audio controls preload=False><source src="audio/364090/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/364090/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | 
| 973498 | <audio controls preload=False><source src="audio/973498/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/973498/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | 
| 1007274 | <audio controls preload=False><source src="audio/1007274/stable_audio_open_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/kmeans_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/pq_8192_44100.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | <audio controls preload=False><source src="audio/1007274/vqvae.mp3" type="audio/mpeg">Audio not supported by your browser.</audio> | 
