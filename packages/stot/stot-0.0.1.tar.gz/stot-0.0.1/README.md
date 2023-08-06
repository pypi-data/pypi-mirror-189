# stot

Speech to Text (stot) is a fork of the [davabase/whisper_real_time](https://github.com/davabase/whisper_real_time)
command line tool that provides real-time transcription of speech to text using [openai/whisper](https://github.com/openai/whisper),
with additional functionality.

## Getting Started

To install run the following command:

```bash
pip install stot
```

For CUDA enabled Nvidia GPU:

```bash
pip install stot --extra-index-url https://download.pytorch.org/whl/cu116
```

## Command-line usage

Run stot:
```bash
stot --help
```

Alternatively run as a package:
```bash
python -m stot --help
```

Speech to text in real-time using the small whisper model:
```bash
stot --model small
```
