import sounddevice as sd
from pydub import AudioSegment
import os

seconds = 5
fs = 44100



def record_audio(seconds=seconds, fs=fs):
    audioIndex = 0
    output_dir = "records"
    os.makedirs(output_dir, exist_ok=True)


    try:
        record = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
        sd.wait()

        audioIndex += 1
    except KeyboardInterrupt:
        pass

    # If there are no records, there's nothing to save
    if record is not None:
        # Convert numpy array to pydub AudioSegment
        audio_segment = AudioSegment(
            data=record.tobytes(),
            sample_width=record.dtype.itemsize,
            frame_rate=fs,
            channels=2
        )
        # Export the AudioSegment as an MP3 file
        output_path = os.path.join(output_dir, "records.mp3")
        audio_segment.export(output_path, format="mp3")
        print(f"Saved recording as {output_path}")
    else:
        print("No audio recorded to save.")

record_audio(1)