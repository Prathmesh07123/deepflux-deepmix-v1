# Day 01 — Audio Signals (Learning Notes)

> Purpose of this note:
> This is a **personal learning recap note**, not product documentation.
> The goal is that even after months or years, opening this file should
> quickly rebuild my understanding of Day 01 concepts.

---

## 1. What is an Audio Signal?

An audio signal is simply:
**a voltage that changes with time and represents sound.**

Sound in air = pressure changes  
Microphone converts these pressure changes into **voltage changes**

So audio is nothing magical.
It is just:
- Voltage
- Changing with time

---

## 2. Three Things That Define Any Audio Signal

Every audio signal can be understood using only **three parameters**.

### 2.1 Amplitude (How Strong the Signal Is)

- Amplitude = signal strength
- Measured in **volts (V)** or **millivolts (mV)**
- Higher voltage → louder sound

Examples:
- Microphone signal: ~1 mV to 10 mV
- Line-level signal: ~0.3 V to 1.2 V

Important idea:
> If amplitude is too small → noise dominates  
> If amplitude is too large → clipping happens

---

### 2.2 Frequency (How Fast It Vibrates)

- Frequency = how fast the signal repeats
- Measured in **Hertz (Hz)**

Human hearing range:
- 20 Hz → very low bass
- 20 kHz → very high treble

Examples:
- Bass note: ~50 Hz
- Human voice: 300 Hz – 3 kHz
- Sharp treble: ~10 kHz

---

### 2.3 Time

- Audio exists continuously over time
- Later, ADC will sample this continuous signal

At this stage:
> Think **voltage vs time**, not samples yet

---

## 3. Basic Audio Waveforms

All complex sounds are built from simple waveforms.

---

### 3.1 Sine Wave

- Smooth and clean
- Contains only one frequency
- No harmonics

Why sine waves are important:
- Best signal for testing audio systems
- Used for SNR and distortion measurement

Key idea:
> Sine wave = reference signal in audio engineering

---

### 3.2 Square Wave

- Sharp transitions
- Contains many harmonics
- Very hard for DACs and filters

Why square waves matter:
- They expose bandwidth limitations
- They reveal slow edges and filtering effects

Key idea:
> If system handles square waves well, it is usually robust

---

### 3.3 Triangle Wave

- Smoother than square wave
- Fewer harmonics
- Easier to reproduce

Used to:
- Observe linearity
- Study filter behavior

---

## 4. Real Audio is a Combination of Sine Waves

Important mental model:
> Any real sound can be broken into many sine waves of different frequencies and amplitudes

This idea leads to:
- Fourier analysis
- FFT
- Frequency-domain DSP

(No math today — only intuition)

---

## 5. Mic Level vs Line Level (Very Important)

### 5.1 Microphone Level

- Very small signal
- Typically 1–10 mV RMS
- Easily affected by noise

Because it is small:
- Needs **preamplifier**
- Needs **low-noise design**

---

### 5.2 Line Level

- Much stronger signal
- Consumer: −10 dBV (~0.316 V RMS)
- Professional: +4 dBu (~1.23 V RMS)

Used between:
- Mixer
- ADC
- DAC
- Amplifier

---

### 5.3 Common Beginner Mistake

Connecting microphone directly to ADC input.

Result:
- Very noisy signal
- Poor quality
- Wrong conclusion that ADC is bad

Correct approach:
> Mic → Preamp → ADC

---

## 6. Embedded Audio Signal Chain

Typical audio path in embedded systems:

Microphone → Preamp → ADC → DSP → DAC → Amplifier → Speaker

Each block matters.
Mistake in one block affects entire system.

---

## 7. Key Takeaways (Quick Recap)

- Audio = voltage vs time
- Amplitude controls loudness
- Frequency controls pitch
- Sine wave is the cleanest test signal
- Signal level matching is critical
- Audio systems fail more due to level issues than DSP bugs

---

## 8. Self-Check Questions

Answer these from memory:
1. Why are sine waves used for audio testing?
2. Why does mic audio need amplification?
3. Why are square waves difficult for DACs?

If I can answer these confidently,
Day 01 concepts are clear.
