# S3PRL-VC: A Voice Conversion Toolkit based on S3PRL

## Introduction and motivation

[S3PRL](https://github.com/s3prl/s3prl) stands for "Self-Supervised Speech/Sound Pre-training and Representation Learning Toolkit". It is a toolkit for benchmarking self-supervised speech representations (S3Rs) models using a collection of so-called "downstream" tasks. S3PRL-VC was originally built under S3PRL, which implements voice conversion (VC) as one of the downstream tasks. However, as S3PRL grows bigger and bigger, it is getting harder to integrate the various VC recipes into the main S3PRL repository. Therefore, this repository aims to isolate the VC downstream task from S3PRL to become an independently-maintained toolkit (hopefully).

## What can this repo do?

This repo aims to provide **a platform for frame-based recognition-synthesis voice conversion**.

### Pipeline

Given a source speech, we first use a recognizer (or upstream) to extract intermediate representations, which are then mapped to the acoustic feature space (log melspectrograms) with a synthesizer (or downstream). Finally a waveform synthesizer (some call it vocoder) is used to convert the acoustic feature to waveform.

### Supported upstream

Currently the supported S3R upstream completely depend on the official S3PRL repository. In addition, we also support PPG (phonetic posteriorgram, which is sometimes referred to as BNF, bottleneck feature).

## Instsallation 

### 1. pip

```
pip install s3prl-vc
```

### 2. Editable installation with virtualenv
```
git clone https://github.com/unilight/s3prl-vc.git
cd s3prl-vc/tools
make
```

## Complete training, decoding and benchmarking

Same as many speech processing based repositories ([ESPNet](https://github.com/espnet/espnet), [ParallelWaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN), etc.), we formulate our recipes in kaldi-style. They can be found in the `egs` folder. Please check the detailed usage in each recipe.

## Citation

```
@inproceedings{huang2021s3prl,
  title={S3PRL-VC: Open-source Voice Conversion Framework with Self-supervised Speech Representations},
  author={Huang, Wen-Chin and Yang, Shu-Wen and Hayashi, Tomoki and Lee, Hung-Yi and Watanabe, Shinji and Toda, Tomoki},
  booktitle={Proc. ICASSP},
  year={2022}
}
```