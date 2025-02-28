# STT and TTS

# Important URLs
1. [TTS - A Lazy Data Science Guide](http://mohitmayank.com/a_lazy_data_science_guide/audio_intelligence/tts/)
2. [Speech synthesis: A review of the best text to speech architectures with Deep Learning](https://theaisummer.com/text-to-speech/)


## 1. Important Terms
### Few important linguistic terms
- **`Grapheme`**  
  A grapheme is the smallest unit of writing system in a language.

- **`Phonemes`**  
  The smallest sound units that can distinguish meaning.

- **`Prosody`**  
  The patterns of rhythm and sound used in poetry.

- **`Pitch`**  
  Highness or lowness of voice.
  
- **`Rhythm`**  
  Timing patterns in speech.
  
- **`Stress Patterns`**  
  Emphasis on certain syllables or words.

- **`Pauses`**  
  Breaks in speech for emphasis or naturalness.


### Differences Between Graphemes and Phonemes
| Aspect | Grapheme | Phoneme |
|-|-|-|
| **Definition**    | Written representation (letters, symbols).  | Spoken sound representation.                   |
| **Example (English)** | The word "knight" has 6 graphemes.       | The word "knight" has 3 phonemes: /n/, /aɪ/, /t/. |
| **Example (Hindi)**  | The word "काम" has 3 graphemes.          | The word "काम" has 3 phonemes: /k/, /aː/, /m/. |
| **Relationship**  | Graphemes are mapped to phonemes (via rules or patterns). | Phonemes are the sound units derived from graphemes. |


### Vocoder
Early neural vocoders such as WaveNet, Char2Wav, WaveRNN directly take linguistic features as input and generate waveform. Later versions take mel-spectrograms as input and generate waveform. Since speech waveform is very long, autoregressive waveform generation takes much inference time. Thus, generative models such as Flow, GAN, VAE, and DDPM (Denoising Diffusion Probabilistic Model, Diffusion for short) are used in waveform generation.

## 2. Resources
1. [Benchmarking open source and paid services for speech to text: an analysis of quality and input variety](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2023.1210559/full)



## 3. Quick Notes | Summary
                                                     