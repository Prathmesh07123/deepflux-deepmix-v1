# Day 02 — Waveforms & Frequency (Learning Notes)

> Purpose of this note:
> This is a **personal learning recap note** for Day 02.
> Reading this file in the future should quickly rebuild my understanding
> of waveforms, frequency, and harmonics used in audio engineering.

---

## 1. What is a Waveform?

A waveform is simply:
**how voltage changes with time.**

When we plot:
- X-axis → Time
- Y-axis → Voltage

we get a waveform.

Different waveforms behave differently in audio systems,
even if they sound similar at first.

---

## 2. Common Audio Waveforms

### 2.1 Sine Wave

- Smooth and continuous
- Single frequency
- No harmonics

Key properties:
- Cleanest possible waveform
- Easy for ADC and DAC to handle

Why sine waves matter:
> They are the reference signal for audio testing and measurements.

---

### 2.2 Square Wave

- Abrupt transitions (fast edges)
- Alternates between high and low voltage
- Contains many harmonics

Important insight:
> A perfect square wave needs infinite bandwidth (impossible in real systems).

Why square waves are useful:
- Reveal bandwidth limitations
- Show filtering effects clearly

---

### 2.3 Triangle Wave

- Linear rising and falling edges
- Smoother than square wave
- Contains fewer harmonics

Why triangle waves are used:
- Easier on DACs
- Useful for checking linearity

---

## 3. Frequency — The Speed of Vibration

Frequency tells us:
**how fast a waveform repeats.**

- Measured in Hertz (Hz)
- 1 Hz = 1 cycle per second

Examples:
- 10 Hz → very slow oscillation
- 1 kHz → 1000 cycles per second

---

## 4. Period and Frequency Relationship

Frequency and period are inverses:

Period (T) = 1 / Frequency (f)

Examples:
- 1 kHz → period = 1 ms
- 100 Hz → period = 10 ms

Key idea:
> Higher frequency = shorter period

---

## 5. What Are Harmonics?

Harmonics are:
**extra frequencies present along with the fundamental frequency.**

- Fundamental frequency = main tone
- Harmonics = multiples of the fundamental

Example:
- Fundamental = 100 Hz
- Harmonics = 200 Hz, 300 Hz, 400 Hz, ...

---

## 6. Harmonics in Different Waveforms

### 6.1 Sine Wave
- Only fundamental frequency
- No harmonics

---

### 6.2 Square Wave
- Fundamental + odd harmonics
- Strong harmonic content

This is why square waves:
- Sound harsh
- Stress audio systems

---

### 6.3 Triangle Wave
- Fundamental + odd harmonics
- Harmonics decrease faster than square wave

Result:
> Triangle waves sound smoother than square waves.

---

## 7. Visualizing Waveforms (Mental Model)

When visualizing waveforms:
- Smooth curve → limited bandwidth
- Sharp corners → high-frequency content

Important rule:
> Sharper edges = more high-frequency harmonics

---

## 8. Why This Matters in Embedded Audio

- ADC sampling rate limits highest frequency
- DAC and filters remove high harmonics
- Square waves expose system weaknesses

This explains why:
- Square waves get rounded
- High frequencies disappear
- Filters affect sound character

---

## 9. Key Takeaways (Quick Recap)

- Waveform = voltage vs time
- Frequency defines pitch
- Period and frequency are inversely related
- Harmonics define waveform shape
- Sharp edges require high bandwidth

---

## 10. Self-Check Questions

Answer without notes:
1. Why does a square wave contain harmonics?
2. Why does a sine wave have no harmonics?
3. Why do sharp edges require high bandwidth?

If these answers are clear,
Day 02 concepts are solid.
