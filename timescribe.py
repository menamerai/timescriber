import json
import os
import whisper_timestamped as whisper


class TimeScribe:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def transcribe_folder(self, input_path=None, output_path=None, model_size="medium") -> None:
        if input_path == None and output_path == None:
            input_path = self.input_path
            output_path = self.output_path

        # if output path doesn't exist, create it
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # get all files in input path
        files = os.listdir(input_path)

        speaker_segments = dict()

        # iterate through files
        for file in files:
            # if file is a folder, call this function recursively
            if os.path.isdir(os.path.join(input_path, file)):
                self.transcribe_folder(os.path.join(input_path, file), os.path.join(output_path, file))
            # if file is an audio file, transcribe it
            elif file.endswith(".wav") or file.endswith(".flac"):
                # self.transcribe_file(os.path.join(input_path, file), os.path.join(output_path, file))
                audio = whisper.load_audio(os.path.join(input_path, file))
                model = whisper.load_model(model_size)
                result = whisper.transcribe(model, audio, language="en", vad=True)
                speaker_segments[file] = result["segments"]

            # otherwise, ignore it
            else:
                print(f"Skipping {file}")

        
        with open(f"{output_path}/data.json", "w") as f:
            f.write(json.dumps(speaker_segments, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    timescribe = TimeScribe("./input", "./output")
    timescribe.transcribe_folder(model_size="tiny")